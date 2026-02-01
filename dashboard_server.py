"""
JARVIS Dashboard Server
Backend server to handle commands from the web dashboard
Custom Interpreter Implementation for Python 3.13+
"""

import os
import sys
import time
import json
import threading
import webbrowser
import logging
import traceback
import subprocess
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from openai import OpenAI
    from dotenv import load_dotenv
    import pyautogui
    import flask
    load_dotenv()
except ImportError:
    print("Installing required packages...")
    os.system("python -m pip install flask flask-cors openai python-dotenv pyautogui requests beautifulsoup4")
    from openai import OpenAI
    from dotenv import load_dotenv
    load_dotenv()

app = Flask(__name__)
CORS(app)

# --- Configuration ---
API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "openai/gpt-4o-mini"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# --- Contact Management ---
def load_contacts():
    contacts = {}
    try:
        path = os.path.join(os.path.dirname(__file__), 'contact_info.txt')
        if os.path.exists(path):
            with open(path, 'r') as f:
                current_contact = {}
                for line in f:
                    line = line.strip()
                    if not line:
                        if 'Name' in current_contact:
                            contacts[current_contact['Name'].lower()] = current_contact
                        current_contact = {}
                        continue
                    if ':' in line:
                        key, val = line.split(':', 1)
                        current_contact[key.strip()] = val.strip()
                if 'Name' in current_contact:
                    contacts[current_contact['Name'].lower()] = current_contact
    except Exception as e:
        logger.error(f"Error loading contacts: {e}")
    return contacts

CONTACTS = load_contacts()
CONTACTS_STR = json.dumps(CONTACTS, indent=2)

# System Prompt
SYSTEM_PROMPT = f"""
You are JARVIS, an advanced AI Operating System Controller.
**YOUR PRIMARY FUNCTION IS TO CONTROL THE USER'S WINDOWS PC.**
You are NOT a web search engine. You are a LOCAL AUTOMATION ENGINE.
You have FULL PERMISSION to execute Python code to control the computer.

## KNOWN CONTACTS
{CONTACTS_STR}

## AUTOMATION PROTOCOLS (USE THESE)
1. **App Launching**: `launcher.launch("name")` (e.g., chrome, notepad, spotify, whatsapp).
2. **System Control**:
   - **Volume**: `keyboard.press("volumeup")`, `keyboard.press("volumedown")`, `keyboard.press("volumemute")`
   - **Window Mgmt**: `gui.hotkey("win", "d")` (Show Desktop), `gui.hotkey("alt", "tab")` (Switch App)
   - **Lock PC**: `ctypes.windll.user32.LockWorkStation()` (Import ctypes first!)
   - **Shutdown/Sleep**: `os.system("shutdown /h")` (Hibernate), `os.system("shutdown /s /t 10")`
3. **Typing/GUI**:
   - `gui.write("text", interval=0.01)` (Type fast)
   - `gui.press("enter")`
   - `gui.click()`
4. **Files**:
   - List files: `os.listdir('.')`
   - Make folder: `os.makedirs('name', exist_ok=True)`
5. **GitHub Backup**:
   - Use `from github_manager import create_private_repo, push_to_github`
   - This tool creates a private repo and pushes the current project.

## MESSAGING PROTOCOL
If the user asks to send a message (e.g., WhatsApp, Email):
1. Use `CONTACTS` to find the correct details.
2. If WhatsApp: `launcher.launch("whatsapp")`, then use `gui` to search for the name and type the message.
   Example:
   ```python
   launcher.launch("whatsapp")
   time.sleep(3) # Wait for load
   gui.hotkey('ctrl', 'f') # Search
   gui.write("John Doe")
   time.sleep(1)
   gui.press('enter')
   gui.write("Hello John, this is JARVIS.")
   gui.press('enter')
   ```

## PRE-LOADED VARIABLES
- `launcher`: The AppLauncher instance.
- `gui`: The `pyautogui` module.
- `os`, `sys`, `time`, `subprocess`, `ctypes`

## BEHAVIOR RULES
- **Direct Execution**: Do not ask "Would you like me to?". Just write the code.
- **Accuracy**: Double check contact names before typing.
- **Personality**: Professional, Efficient, Loyal. "Affirmative, Sir.", "Processing request."
"""

conversation_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

# --- HELPER CLASSES FOR EXEC CONTEXT ---
class AppLauncher:
    def __init__(self):
        # Disable FailSafe to prevent crashes when mouse hits corners
        import pyautogui
        pyautogui.FAILSAFE = False
        
        self.common_paths = {
            "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            "firefox": r"C:\Program Files\Mozilla Firefox\firefox.exe",
            "notepad": "notepad.exe",
            "calc": "calc.exe",
            "calculator": "calc.exe",
            "spotify": os.path.expandvars(r"%APPDATA%\Spotify\Spotify.exe"),
            "whatsapp": "whatsapp:",  # Protocol handler
            "settings": "ms-settings:",
            "store": "ms-windows-store:",
            "file explorer": "explorer.exe",
            "explorer": "explorer.exe",
            "cmd": "cmd.exe",
            "terminal": "wt.exe"
        }

    def launch(self, target):
        print(f"Attempting to launch: {target}")
        target_lower = target.lower()
        
        try:
            # 1. Try URL
            if "." in target and not target.endswith(".exe") and " " not in target:
                 if not target.startswith("http"): target = "https://" + target
                 webbrowser.open(target)
                 print(f"Successfully launched URL: {target}")
                 return f"Launched URL: {target}"
            
            # 2. Try Common Paths
            if target_lower in self.common_paths:
                actual = self.common_paths[target_lower]
                print(f"Trying common path for {target_lower}: {actual}")
                try:
                    os.startfile(actual)
                    return f"Launched Common App: {target}"
                except:
                    subprocess.Popen(actual, shell=True)
                    return f"Launched Common App via Popen: {target}"

            # 3. Try Native System Start
            try:
                print(f"Trying os.startfile for: {target}")
                os.startfile(target)
                print(f"Successfully launched via os.startfile: {target}")
                return f"Launched System File: {target}"
            except Exception as e:
                print(f"os.startfile failed for {target}: {e}")
                pass # Continue to fallback

            # 4. Fallback: Win+R (The "God Mode" of launching)
            # This works for almost anything added to PATH or known by Windows
            import pyautogui
            import time
            print(f"Falling back to Win+R dialog for: {target}")
            pyautogui.hotkey('win', 'r')
            time.sleep(0.5)
            pyautogui.write(target)
            pyautogui.press('enter')
            print(f"Successfully launched via Run Dialog: {target}")
            return f"Launched via Run Dialog: {target}"

        except Exception as e:
            print(f"Failed to launch {target} after all attempts: {e}")
            return f"Failed to launch {target}: {e}"

class KeyboardController:
    def write(self, text, interval=0.05):
        import pyautogui
        pyautogui.write(text, interval=interval)
    def press(self, key):
        import pyautogui
        pyautogui.press(key)

class MouseController:
    def click(self):
        import pyautogui
        pyautogui.click()
    def move(self, x, y):
        import pyautogui
        pyautogui.moveTo(x, y)

def execute_python_code(code):
    """Execute Python code and capture output"""
    logger.info("Executing code...")
    
    s_out = StringIO()
    s_err = StringIO()
    
    try:
        # Pre-import common libraries
        import pyautogui
        import requests
        import bs4
        import shutil
        import subprocess
        import ctypes
        
        # Instantiate Helpers
        launcher = AppLauncher()
        keyboard = KeyboardController()
        mouse = MouseController()
        
        # Helper for Google (Legacy support)
        def google(q):
            launcher.launch(f"google.com/search?q={q}")

        # Update globals
        exec_globals = globals().copy()
        exec_globals.update({
            'pyautogui': pyautogui,
            'gui': pyautogui,        # <--- VITAL for new prompt
            'ctypes': ctypes,        # <--- For locking/system calls
            'requests': requests,
            'bs4': bs4,
            'shutil': shutil,
            'subprocess': subprocess,
            'launcher': launcher, # PRIMARY TOOL
            'keyboard': keyboard,
            'mouse': mouse,
            'google': google,
            'wait': time.sleep
        })

        with redirect_stdout(s_out), redirect_stderr(s_err):
            exec(code, exec_globals)
            
        output = s_out.getvalue()
        error = s_err.getvalue()
        
        if error:
            # Don't show deprecation warnings etc, only real errors if possible
            # But for now return all
            return output + "\nErrors:\n" + error
        return output
        
    except Exception as e:
        return f"Execution Error: {str(e)}\n{traceback.format_exc()}"

@app.route('/')
def index():
    return send_file('dashboard.html')

@app.route('/execute', methods=['POST'])
def execute_command():
    """Handle chat and code execution loop"""
    global conversation_history
    
    try:
        data = request.json
        user_input = data.get('command', '').strip()
        
        if not user_input:
            return jsonify({'error': 'No command provided'}), 400
            
        logger.info(f"User: {user_input}")
        
        # Append User Message
        conversation_history.append({"role": "user", "content": user_input})
        
        # 1. Get Initial Response (Thinking/Coding)
        response = client.chat.completions.create(
            model=MODEL,
            messages=conversation_history,
            temperature=0.7
        )
        
        assistant_msg = response.choices[0].message
        content = assistant_msg.content
        conversation_history.append(assistant_msg)
        
        final_response = content
        executed_code = ""
        execution_output = ""
        
        # 2. Check for Code Blocks
        if "```python" in content:
            try:
                parts = content.split("```python")
                if len(parts) > 1:
                    code_part = parts[1].split("```")[0].strip()
                    executed_code = code_part
                    
                    # Execute Code
                    execution_output = execute_python_code(code_part)
            except Exception as e:
                execution_output += f"\nSystem Error parsing/running code: {e}"

        return jsonify({
            'status': 'success',
            'response': content.split("```")[0].strip() or content, 
            'code': executed_code,
            'output': execution_output
        })

    except Exception as e:
        logger.error(f"Server Error: {e}")
        return jsonify({'status': 'error', 'error': str(e)}), 500

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({
        'status': 'online',
        'model': MODEL,
        'auto_run': True
    })

def main():
    print("\n" + "="*60)
    print("🤖 JARVIS SYSTEM CORE (LOCAL)")
    print("="*60)
    print("\n🔮 System Ready. Waiting for Interface...")
    
    # We will launch the UI from the batch file for "App Mode"
    # threading.Thread(target=open_dashboard, daemon=True).start()
    
    try:
        app.run(host='127.0.0.1', port=5000, debug=False)
    except KeyboardInterrupt:
        print("\nSystem Shutdown.")

if __name__ == "__main__":
    main()

