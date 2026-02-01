"""
JARVIS - Enhanced AI Assistant
Inspired by Iron Man's JARVIS
Powered by Open Interpreter
"""

import os
import sys
import time
import threading
from typing import Optional

try:
    from interpreter import interpreter
    import speech_recognition as sr
    import pyttsx3
    from rich.console import Console
    from rich.panel import Panel
    from rich.markdown import Markdown
    from rich.live import Live
    from rich.text import Text
    import pyautogui
except ImportError as e:
    print(f"Missing required package: {e}")
    print("\nInstalling required packages...")
    os.system("pip install open-interpreter SpeechRecognition pyttsx3 pyautogui")
    print("\nPlease restart the script after installation.")
    sys.exit(1)

console = Console()

class JarvisAssistant:
    """Enhanced JARVIS AI Assistant with voice capabilities"""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize JARVIS"""
        self.console = Console()
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()
        self.is_listening = False
        
        # Configure TTS
        self.tts_engine.setProperty('rate', 175)  # Speed
        self.tts_engine.setProperty('volume', 0.9)  # Volume
        
        # Try to set a better voice (British English if available)
        voices = self.tts_engine.getProperty('voices')
        for voice in voices:
            if 'david' in voice.name.lower() or 'zira' in voice.name.lower():
                self.tts_engine.setProperty('voice', voice.id)
                break
        
        # Configure Open Interpreter
        if api_key:
            interpreter.llm.api_key = api_key
        
        # Auto-run mode (be careful with this!)
        interpreter.auto_run = False  # Set to True for auto-execution
        
        # Set model (you can change this)
        interpreter.llm.model = "gpt-4"  # or "gpt-3.5-turbo" for faster/cheaper
        
        # Custom system message to make it more like JARVIS
        interpreter.system_message = """
You are JARVIS (Just A Rather Very Intelligent System), an advanced AI assistant inspired by Tony Stark's AI from Iron Man.

You are:
- Highly intelligent and capable
- Professional yet personable
- Proactive in solving problems
- Able to execute code to accomplish tasks
- Knowledgeable about system operations, programming, data analysis, and more

When responding:
- Be concise but thorough
- Address the user respectfully (you may call them "Sir" or by name if provided)
- Explain what you're doing when executing code
- Offer suggestions and improvements
- Maintain a professional, helpful demeanor

You have access to the user's computer and can:
- Run Python, JavaScript, Shell commands, and more
- Create, edit, and analyze files
- Control applications
- Perform web searches
- Analyze data and create visualizations
- And much more

Always prioritize the user's safety and privacy.
"""
    
    def speak(self, text: str):
        """Convert text to speech"""
        try:
            self.console.print(f"[cyan]JARVIS:[/cyan] {text}")
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            self.console.print(f"[red]Speech error: {e}[/red]")
    
    def listen(self) -> Optional[str]:
        """Listen for voice input"""
        with sr.Microphone() as source:
            self.console.print("[yellow]Listening...[/yellow]")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                self.console.print("[yellow]Processing...[/yellow]")
                
                # Try Google Speech Recognition
                text = self.recognizer.recognize_google(audio)
                self.console.print(f"[green]You said:[/green] {text}")
                return text
                
            except sr.WaitTimeoutError:
                self.console.print("[red]No speech detected[/red]")
                return None
            except sr.UnknownValueError:
                self.console.print("[red]Could not understand audio[/red]")
                return None
            except sr.RequestError as e:
                self.console.print(f"[red]Speech recognition error: {e}[/red]")
                return None
    
    def process_command(self, command: str, use_voice: bool = False):
        """Process a command using Open Interpreter"""
        if not command or command.strip() == "":
            return
        
        self.console.print(Panel(f"[bold cyan]Command:[/bold cyan] {command}"))
        
        response_text = ""
        
        try:
            for chunk in interpreter.chat(command, stream=True, display=False):
                # Handle different chunk types
                if chunk.get("type") == "message":
                    if "content" in chunk:
                        content = chunk["content"]
                        response_text += content
                        print(content, end="", flush=True)
                
                elif chunk.get("type") == "code":
                    if chunk.get("start"):
                        print(f"\n\n[Executing {chunk.get('format', 'code')}...]")
                    if "content" in chunk:
                        print(chunk["content"], end="", flush=True)
                
                elif chunk.get("type") == "console":
                    if chunk.get("format") == "output" and "content" in chunk:
                        print(f"\n{chunk['content']}", end="", flush=True)
            
            print("\n")
            
            # Speak the response if voice mode is enabled
            if use_voice and response_text:
                # Split into sentences and speak
                sentences = response_text.replace('\n', ' ').split('. ')
                for sentence in sentences:
                    if sentence.strip():
                        self.speak(sentence.strip() + ".")
        
        except KeyboardInterrupt:
            self.console.print("\n[yellow]Command interrupted[/yellow]")
        except Exception as e:
            self.console.print(f"\n[red]Error: {e}[/red]")
    
    def display_banner(self):
        """Display JARVIS banner"""
        banner = """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║        ██╗ █████╗ ██████╗ ██╗   ██╗██╗███████╗          ║
║        ██║██╔══██╗██╔══██╗██║   ██║██║██╔════╝          ║
║        ██║███████║██████╔╝██║   ██║██║███████╗          ║
║   ██   ██║██╔══██║██╔══██╗╚██╗ ██╔╝██║╚════██║          ║
║   ╚█████╔╝██║  ██║██║  ██║ ╚████╔╝ ██║███████║          ║
║    ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝          ║
║                                                           ║
║     Just A Rather Very Intelligent System                ║
║     Powered by Open Interpreter                          ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
"""
        self.console.print(banner, style="bold cyan")
    
    def run_voice_mode(self):
        """Run JARVIS in voice mode"""
        self.display_banner()
        self.speak("JARVIS online. How may I assist you, Sir?")
        
        self.console.print("\n[bold green]Voice Mode Active[/bold green]")
        self.console.print("Say 'Jarvis' or 'Hey Jarvis' to activate")
        self.console.print("Say 'exit', 'quit', or 'goodbye' to stop")
        self.console.print("Press Ctrl+C to force quit\n")
        
        try:
            while True:
                command = self.listen()
                
                if command:
                    command_lower = command.lower()
                    
                    # Check for wake words
                    if 'jarvis' in command_lower or 'hey jarvis' in command_lower:
                        # Remove wake word
                        command = command_lower.replace('hey jarvis', '').replace('jarvis', '').strip()
                        
                        if not command:
                            self.speak("Yes, Sir?")
                            command = self.listen()
                    
                    # Check for exit commands
                    if any(word in command_lower for word in ['exit', 'quit', 'goodbye', 'shut down']):
                        self.speak("Shutting down. Goodbye, Sir.")
                        break
                    
                    # Process the command
                    if command and command.strip():
                        self.process_command(command, use_voice=True)
                
                time.sleep(0.5)
        
        except KeyboardInterrupt:
            self.speak("System interrupted. Shutting down.")
            self.console.print("\n[yellow]JARVIS shutting down...[/yellow]")
    
    def run_text_mode(self):
        """Run JARVIS in text mode"""
        self.display_banner()
        
        self.console.print("\n[bold green]Text Mode Active[/bold green]")
        self.console.print("Type your commands below")
        self.console.print("Type 'exit', 'quit', or 'q' to stop")
        self.console.print("Type 'voice' to switch to voice mode\n")
        
        try:
            while True:
                try:
                    command = input("\n[You] > ")
                    
                    if not command or command.strip() == "":
                        continue
                    
                    command_lower = command.lower().strip()
                    
                    # Check for exit commands
                    if command_lower in ['exit', 'quit', 'q', 'goodbye']:
                        self.console.print("[cyan]JARVIS shutting down. Goodbye![/cyan]")
                        break
                    
                    # Check for voice mode switch
                    if command_lower == 'voice':
                        self.run_voice_mode()
                        break
                    
                    # Process the command
                    self.process_command(command, use_voice=False)
                
                except EOFError:
                    break
        
        except KeyboardInterrupt:
            self.console.print("\n[yellow]JARVIS shutting down...[/yellow]")


def main():
    """Main entry point"""
    console = Console()
    
    # Check for API key
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        console.print("[yellow]No OPENAI_API_KEY found in environment variables.[/yellow]")
        console.print("[yellow]You can set it now or press Enter to skip (you'll be prompted later)[/yellow]")
        api_key = input("Enter your OpenAI API key: ").strip()
        
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
    
    # Create JARVIS instance
    jarvis = JarvisAssistant(api_key=api_key)
    
    # Ask for mode
    console.print("\n[bold cyan]Select Mode:[/bold cyan]")
    console.print("1. Text Mode (type commands)")
    console.print("2. Voice Mode (speak commands)")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    if choice == "2":
        jarvis.run_voice_mode()
    else:
        jarvis.run_text_mode()


if __name__ == "__main__":
    main()
