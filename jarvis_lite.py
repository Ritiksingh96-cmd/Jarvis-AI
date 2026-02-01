"""
JARVIS Lite - Simplified AI Assistant
Works with Python 3.13+
Uses OpenAI API directly without Open Interpreter
"""

import os
import sys
import time
from typing import Optional

try:
    import speech_recognition as sr
    import pyttsx3
    from rich.console import Console
    from rich.panel import Panel
    from openai import OpenAI
except ImportError as e:
    print(f"Missing required package: {e}")
    print("\nInstalling required packages...")
    os.system("pip install SpeechRecognition pyttsx3 rich openai")
    print("\nPlease restart the script after installation.")
    sys.exit(1)

console = Console()

class JarvisLite:
    """Simplified JARVIS AI Assistant"""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize JARVIS Lite"""
        self.console = Console()
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()
        
        # Configure TTS
        self.tts_engine.setProperty('rate', 175)
        self.tts_engine.setProperty('volume', 0.9)
        
        # Try to set a better voice
        voices = self.tts_engine.getProperty('voices')
        for voice in voices:
            if 'david' in voice.name.lower() or 'zira' in voice.name.lower():
                self.tts_engine.setProperty('voice', voice.id)
                break
        
        # Initialize OpenAI client
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.conversation_history = []
        
        # System message
        self.system_message = {
            "role": "system",
            "content": """You are JARVIS (Just A Rather Very Intelligent System), an advanced AI assistant inspired by Tony Stark's AI from Iron Man.

You are:
- Highly intelligent and capable
- Professional yet personable
- Concise but thorough in responses
- Helpful and proactive

When responding:
- Address the user respectfully (you may call them "Sir" or by name if provided)
- Be clear and direct
- Offer helpful suggestions
- Maintain a professional, helpful demeanor similar to the JARVIS from Iron Man

Keep responses conversational and not too long unless asked for detailed information."""
        }
        self.conversation_history.append(self.system_message)
    
    def speak(self, text: str):
        """Convert text to speech"""
        try:
            self.console.print(f"\n[cyan]JARVIS:[/cyan] {text}\n")
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            self.console.print(f"[red]Speech error: {e}[/red]")
    
    def listen(self) -> Optional[str]:
        """Listen for voice input"""
        with sr.Microphone() as source:
            self.console.print("[yellow]🎤 Listening...[/yellow]")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                self.console.print("[yellow]⚙️  Processing...[/yellow]")
                
                text = self.recognizer.recognize_google(audio)
                self.console.print(f"[green]You said:[/green] {text}")
                return text
                
            except sr.WaitTimeoutError:
                self.console.print("[red]⏱️  No speech detected[/red]")
                return None
            except sr.UnknownValueError:
                self.console.print("[red]❌ Could not understand audio[/red]")
                return None
            except sr.RequestError as e:
                self.console.print(f"[red]❌ Speech recognition error: {e}[/red]")
                return None
    
    def chat(self, message: str, use_voice: bool = False) -> str:
        """Send a message and get response"""
        if not message or message.strip() == "":
            return ""
        
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": message
        })
        
        try:
            # Get response from OpenAI
            self.console.print("[yellow]🤔 Thinking...[/yellow]")
            
            response = self.client.chat.completions.create(
                model="gpt-4",  # or "gpt-3.5-turbo" for faster/cheaper
                messages=self.conversation_history,
                temperature=0.7,
                max_tokens=500
            )
            
            assistant_message = response.choices[0].message.content
            
            # Add assistant response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            # Display response
            if use_voice:
                self.speak(assistant_message)
            else:
                self.console.print(f"\n[cyan]JARVIS:[/cyan] {assistant_message}\n")
            
            return assistant_message
            
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            self.console.print(f"[red]{error_msg}[/red]")
            return error_msg
    
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
║     Just A Rather Very Intelligent System - Lite         ║
║     Powered by OpenAI GPT-4                              ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
"""
        self.console.print(banner, style="bold cyan")
    
    def run_voice_mode(self):
        """Run JARVIS in voice mode"""
        self.display_banner()
        self.speak("JARVIS online. How may I assist you, Sir?")
        
        self.console.print("\n[bold green]🎙️  Voice Mode Active[/bold green]")
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
                        self.chat(command, use_voice=True)
                
                time.sleep(0.5)
        
        except KeyboardInterrupt:
            self.speak("System interrupted. Shutting down.")
            self.console.print("\n[yellow]JARVIS shutting down...[/yellow]")
    
    def run_text_mode(self):
        """Run JARVIS in text mode"""
        self.display_banner()
        
        self.console.print("\n[bold green]💬 Text Mode Active[/bold green]")
        self.console.print("Type your messages below")
        self.console.print("Type 'exit', 'quit', or 'q' to stop")
        self.console.print("Type 'voice' to switch to voice mode")
        self.console.print("Type 'clear' to clear conversation history\n")
        
        try:
            while True:
                try:
                    command = input("\n[You] > ")
                    
                    if not command or command.strip() == "":
                        continue
                    
                    command_lower = command.lower().strip()
                    
                    # Check for exit commands
                    if command_lower in ['exit', 'quit', 'q', 'goodbye']:
                        self.console.print("[cyan]JARVIS shutting down. Goodbye, Sir![/cyan]")
                        break
                    
                    # Check for voice mode switch
                    if command_lower == 'voice':
                        self.run_voice_mode()
                        break
                    
                    # Check for clear command
                    if command_lower == 'clear':
                        self.conversation_history = [self.system_message]
                        self.console.print("[yellow]Conversation history cleared.[/yellow]")
                        continue
                    
                    # Process the command
                    self.chat(command, use_voice=False)
                
                except EOFError:
                    break
        
        except KeyboardInterrupt:
            self.console.print("\n[yellow]JARVIS shutting down...[/yellow]")


def main():
    """Main entry point"""
    console = Console()
    
    console.print("\n[bold cyan]JARVIS Lite - AI Assistant[/bold cyan]\n")
    
    # Check for API key
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        console.print("[yellow]⚠️  No OPENAI_API_KEY found in environment variables.[/yellow]")
        console.print("[yellow]Please enter your OpenAI API key:[/yellow]")
        api_key = input("API Key: ").strip()
        
        if not api_key:
            console.print("[red]❌ API key is required to run JARVIS.[/red]")
            sys.exit(1)
        
        os.environ["OPENAI_API_KEY"] = api_key
    
    try:
        # Create JARVIS instance
        jarvis = JarvisLite(api_key=api_key)
        
        # Ask for mode
        console.print("\n[bold cyan]Select Mode:[/bold cyan]")
        console.print("1. 💬 Text Mode (type commands)")
        console.print("2. 🎙️  Voice Mode (speak commands)")
        
        choice = input("\nEnter choice (1 or 2): ").strip()
        
        if choice == "2":
            jarvis.run_voice_mode()
        else:
            jarvis.run_text_mode()
    
    except Exception as e:
        console.print(f"\n[red]❌ Error: {e}[/red]")
        console.print("\n[yellow]Make sure you have a valid OpenAI API key and internet connection.[/yellow]")


if __name__ == "__main__":
    main()
