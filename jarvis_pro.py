"""
JARVIS PRO - DEEP INTEGRATION
- WhatsApp (pywhatkit)
- Research (Google)
- Automation (PyAutoGUI + Subprocess)
"""

import os
import sys
import time
import subprocess
import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
from googlesearch import search as gsearch
from openai import OpenAI
from AppOpener import open as open_app_by_name
from dotenv import load_dotenv

load_dotenv()

# CONFIGURATION
# ------------------------------------------------------------------
API_KEY = os.getenv("OPENAI_API_KEY")
WAKE_WORD = "jarvis"

# OpenRouter Config
client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)
MODEL_NAME = "openai/gpt-3.5-turbo"

engine = pyttsx3.init()
engine.setProperty('rate', 165)

def speak(text):
    print(f"\n[JARVIS]: {text}")
    try:
        engine.say(text)
        engine.runAndWait()
    except:
        pass

def listen():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("\n[  MIC ACTIVE  ] Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
                text = recognizer.recognize_google(audio).lower()
                print(f"[  HEARD       ] '{text}'")
                return text
            except:
                return ""
    except:
        return ""

# ------------------------------------------------------------------
# SPECIAL SKILLS
# ------------------------------------------------------------------

def task_whatsapp(command):
    speak("Preparing WhatsApp messaging...")
    # Extract "to WHO" and "message WHAT"
    # This is tricky with regex, so we use AI to parse parameters
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "Extract phone_number (or contact name) and message from user command. Return format: CONTACT|MESSAGE. If no message, assume 'Hello'."},
                {"role": "user", "content": command}
            ]
        )
        parsed = response.choices[0].message.content.strip()
        
        if "|" in parsed:
            contact, msg = parsed.split("|", 1)
            speak(f"Sending to {contact}: {msg}")
            
            # Note: pywhatkit needs 24H time to schedule. 
            # We schedule for 1 minute from now.
            # However, for instant sending, pywhatkit.sendwhatmsg_instantly is better if phone number is known
            
            # Since we often just have a NAME ("Ritik"), and pywhatkit needs a PHONE NUMBER,
            # we will resort to opening WhatsApp Web and Searching.
            
            # OR better: Use 'open_app' to open WhatsApp App/Web and type manually if number unknown.
            # But the user wants "SEND MESSAGE".
            
            # LIMITATION: We need phone numbers for true automation.
            # Workaround: Open WhatsApp Web, type name, press enter, type message.
            
            speak("Opening WhatsApp...")
            webbrowser.open("https://web.whatsapp.com")
            time.sleep(10) # Wait for load
            
            import pyautogui
            # Search contact
            pyautogui.click(200, 200) # Click somewhat top left (adjust for screen)
            speak(f"Searching for {contact}")
            pyautogui.hotkey('ctrl', 'alt', '/') # Search shortcut often
            time.sleep(1)
            pyautogui.write(contact)
            time.sleep(2)
            pyautogui.press('enter')
            
            # Type message
            speak("Typing message...")
            pyautogui.write(msg)
            pyautogui.press('enter')
            speak("Sent.")
            
    except Exception as e:
        speak("I failed to send the message.")
        print(e)

def task_research(command):
    speak("Starting research...")
    query = command.replace("research", "").replace("for", "").strip()
    
    results = []
    try:
        for j in gsearch(query, num_results=3):
            results.append(j)
            
        speak(f"I found {len(results)} sources. Analyzing...")
        
        # Here we would normally scrape content, but for now we open them
        for url in results:
            webbrowser.open(url)
            
        speak("I have opened the top research results for you.")
    except Exception as e:
        speak("Research failed.")
        print(e)

def task_cmd_email(command):
    # Sends email assuming Outlook/Mail app or just writes to CMD
    # Since user said "Send email message to command prompt task", maybe they mean
    # "Execute a command prompt task"?
    
    # Let's interpret "Command Prompt Task" as running a shell command
    speak("Executing shell instruction...")
    cmd = command.replace("command prompt", "").replace("run", "").strip()
    os.system(f"start cmd /k {cmd}")
    speak("Executed.")

def task_ai_coding(command):
    speak("Working on your task...")
    
    system_prompt = """
    You are JARVIS. User wants you to PERFORM A TASK on their computer.
    
    1. WRITE PYTHON CODE to do the task.
    2. Use 'pyautogui' for UI control.
    3. Use 'subprocess' for commands.
    4. Use 'webbrowser' for URLs.
    
    Return ONLY Python code inside ```python blocks.
    """
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": command}
            ]
        )
        content = response.choices[0].message.content
        
        if "```python" in content:
            code = content.split("```python")[1].split("```")[0].strip()
            
            # Save and Run
            with open("pro_task.py", "w", encoding="utf-8") as f:
                f.write(code)
            
            speak("Executing solution...")
            subprocess.Popen([sys.executable, "pro_task.py"])
        else:
            speak(content)
            
    except Exception as e:
        speak("Connection error.")

# ------------------------------------------------------------------
# MAIN LOOP
# ------------------------------------------------------------------

def main():
    speak("JARVIS PRO Online. Dedicated to your commands.")
    
    while True:
        text = listen()
        if not text:
            continue
            
        # Direct parsing
        print(f"[COMMAND]: {text}")
        
        if "whatsapp" in text:
            task_whatsapp(text)
            
        elif "research" in text:
            task_research(text)
            
        elif "command prompt" in text:
            task_cmd_email(text)
            
        elif "open" in text:
            app = text.replace("open ", "").strip()
            speak(f"Opening {app}")
            try:
                open_app_by_name(app, match_closest=True)
            except:
                os.system(f"start {app}")
                
        elif "stop" in text:
            speak("Goodbye Sir.")
            break
            
        else:
            task_ai_coding(text)

if __name__ == "__main__":
    main()
