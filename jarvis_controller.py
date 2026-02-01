"""
JARVIS CONTROLLER - VOICE ONLY INTERFACE
Autonomous Agent with Speech-to-Speech interaction
"""

import os
import sys
import time
import threading
import speech_recognition as sr
import pyttsx3
from interpreter import interpreter

# Configuration
WAKE_WORD = "jarvis"
EXIT_WORDS = ["stop", "exit", "quit", "shut down", "goodbye"]

# Initialize Open Interpreter
interpreter.auto_run = True  # Full autonomy
interpreter.offline = False  # Needs internet for LLM
interpreter.llm.model = "gpt-4"
interpreter.system_message += """
You are JARVIS, a voice-controlled AI agent.
Your goal is to execute tasks on the user's computer immediately and efficiently.
You have FULL PERMISSION to run code, create files, and control the system.
Do not ask for confirmation. Just do it.
Keep your verbal responses short and concise (e.g., "On it, Sir", "Done", "Creating page now").
You are speaking to the user, so don't output markdown or code blocks in your speech, just natural language.
"""

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)

# Initialize Speech Recognition
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(text):
    """Speak text without blocking"""
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_for_command():
    """Listen for audio and convert to text"""
    with microphone as source:
        print("\nListening for command...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio).lower()
            print(f"You said: {text}")
            return text
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            speak("I'm having trouble connecting to speech services.")
            return None

def main():
    # Load API Key
    from dotenv import load_dotenv
    load_dotenv()
    
    if not os.getenv("OPENAI_API_KEY"):
        speak("I need an API key to function, Sir.")
        return

    speak("JARVIS systems online. Standing by.")
    
    while True:
        try:
            command = listen_for_command()
            
            if not command:
                continue
                
            # Check for wake word or direct command context
            if WAKE_WORD in command:
                # Remove wake word to get the actual task
                task = command.replace(WAKE_WORD, "").strip()
                
                if not task:
                    speak("Yes, Sir?")
                    continue
                    
                if any(word in task for word in EXIT_WORDS):
                    speak("Shutting down. Goodbye, Sir.")
                    break
                
                # Execute Task
                speak("Processing execute request.")
                
                # Send to Open Interpreter
                # We prioritize the Code Interpreter for execution
                messages = interpreter.chat(task, display=True, stream=True)
                
                # We want to capture the final response to speak it
                last_response = ""
                for chunk in messages:
                    if chunk['type'] == 'message':
                        if 'content' in chunk:
                            last_response += chunk['content']
                
                if last_response:
                    speak(last_response)
            
        except KeyboardInterrupt:
            speak("System interrupted.")
            break
        except Exception as e:
            print(f"Error: {e}")
            speak("I encountered an error, Sir.")

if __name__ == "__main__":
    main()
