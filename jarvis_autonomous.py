"""
JARVIS AUTOMONOUS AGENT
Standalone implementation of an autonomous agent
"""

import os
import sys
import time
import subprocess
import threading
import speech_recognition as sr
import pyttsx3
from openai import OpenAI
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OPENAI_API_KEY not found in .env")
    sys.exit(1)

client = OpenAI(api_key=api_key)

# Configuration
WAKE_WORD = "jarvis"
current_working_dir = os.getcwd()

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty('rate', 175)

def speak(text):
    """Speak text"""
    print(f"\nJARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def execute_python_code(code):
    """Execute Python code and return output"""
    try:
        print("\n[Executing Code...]")
        # Write to temp file
        with open("temp_task.py", "w", encoding="utf-8") as f:
            f.write(code)
        
        # Run it
        result = subprocess.run([sys.executable, "temp_task.py"], capture_output=True, text=True)
        
        output = result.stdout
        if result.stderr:
            output += f"\nError: {result.stderr}"
            
        # Clean up
        if os.path.exists("temp_task.py"):
            os.remove("temp_task.py")
            
        return output
    except Exception as e:
        return f"Execution failed: {str(e)}"

def process_task(task):
    """Process a task using GPT-4 and execute code"""
    system_prompt = f"""
    You are an autonomous AI agent capable of running code on the user's computer.
    Current Directory: {current_working_dir}
    OS: Windows
    
    User Request: {task}
    
    Goal: Write a Python script to accomplish this request. 
    
    Rules:
    1. If the user wants to create a website/file, write the code to CREATE that file.
    2. Do not just show the HTML, write a Python script that writes the HTML to a file.
    3. Return ONLY the Python code block. No markdown, no explanations.
    4. If creating a web page, make it '3D' and 'modern' if requested.
    5. Assume you have common libraries like 'os', 'sys', 'random'.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": system_prompt}],
            temperature=0.7
        )
        
        content = response.choices[0].message.content
        
        # Extract code from markdown blocks if present
        if "```python" in content:
            code = content.split("```python")[1].split("```")[0].strip()
        elif "```" in content:
            code = content.split("```")[1].split("```")[0].strip()
        else:
            code = content.strip()
            
        return execute_python_code(code)
        
    except Exception as e:
        return f"AI Error: {str(e)}"

def listen():
    """Listen for commands"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5)
            return recognizer.recognize_google(audio).lower()
        except:
            return None

def main():
    speak("Autonomous systems online. Waiting for instructions.")
    
    while True:
        command = listen()
        if not command:
            continue
            
        print(f"Heard: {command}")
        
        if WAKE_WORD in command:
            task = command.replace(WAKE_WORD, "").strip()
            
            if "stop" in task or "exit" in task:
                speak("Shutting down.")
                break
                
            if not task:
                speak("Yes?")
                continue
            
            speak(f"Processing: {task}")
            
            # Execute
            result = process_task(task)
            
            print(f"Result: {result}")
            speak("Task completed.")

if __name__ == "__main__":
    main()
