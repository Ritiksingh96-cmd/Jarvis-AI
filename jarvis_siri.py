"""
JARVIS SYSTEM CONTROLLER
Direct Control over Windows Apps and Browsers
"""

import os
import sys
import time
import speech_recognition as sr
import pyttsx3
import webbrowser
from AppOpener import open as open_app_by_name
from openai import OpenAI
from dotenv import load_dotenv

# ------------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------------
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
WAKE_WORD = "jarvis"

# OpenRouter Config
client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)
MODEL_NAME = "openai/gpt-3.5-turbo"

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print(f"\n[JARVIS]: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n[Listening]... (Say 'Jarvis open chrome' or 'Jarvis search...')")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            text = recognizer.recognize_google(audio).lower()
            print(f"[Heard]: {text}")
            return text
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except Exception as e:
            print(f"Mic Error: {e}")
            return ""

# ------------------------------------------------------------------
# ACTIONS
# ------------------------------------------------------------------

def do_search(query):
    speak(f"Searching for {query}")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def do_open_app(app_name):
    speak(f"Opening {app_name}")
    try:
        # Try AppOpener first (smart search)
        open_app_by_name(app_name, match_closest=True)
    except:
        # Fallback to os.system for common apps
        if "chrome" in app_name:
            os.system("start chrome")
        elif "notepad" in app_name:
            os.system("start notepad")
        elif "calc" in app_name:
            os.system("start calc")
        else:
            speak(f"I couldn't find {app_name}, Sir.")

def do_ai_task(command):
    speak("Processing...")
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are Jarvis. Be concise."},
                {"role": "user", "content": command}
            ]
        )
        reply = response.choices[0].message.content
        speak(reply)
    except Exception as e:
        speak("I cannot connect to the AI brain right now.")
        print(e)

# ------------------------------------------------------------------
# MAIN LOOP
# ------------------------------------------------------------------

def main():
    speak("System Control Online. Ready.")
    
    while True:
        text = listen()
        
        if not text:
            continue
            
        if WAKE_WORD in text:
            # Clean command
            command = text.replace(WAKE_WORD, "").strip()
            
            if not command:
                speak("Yes?")
                continue
            
            # --- DIRECT CONTROL MAP ---
            
            # 1. OPEN APPS
            if command.startswith("open "):
                app_name = command.replace("open ", "").strip()
                do_open_app(app_name)
                
            # 2. SEARCH
            elif "search" in command or "google" in command:
                query = command.replace("search", "").replace("google", "").replace("for", "").strip()
                do_search(query)
            
            # 3. YOUTUBE
            elif "youtube" in command:
                query = command.replace("youtube", "").replace("play", "").strip()
                speak(f"Playing {query} on YouTube")
                webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
            
            # 4. STOP
            elif "stop" in command or "exit" in command:
                speak("Shutting down.")
                break
            
            # 5. EVERYTHING ELSE -> AI
            else:
                do_ai_task(command)

if __name__ == "__main__":
    main()
