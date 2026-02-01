"""
JARVIS Demo Mode
Test the interface without an API key
"""

import time
import random
from rich.console import Console
from rich.panel import Panel

console = Console()

class JarvisDemo:
    """Demo version of JARVIS for testing"""
    
    def __init__(self):
        self.console = Console()
        self.responses = {
            "hello": [
                "Good day, Sir! I'm JARVIS, your AI assistant.",
                "Hello, Sir! How may I assist you today?",
                "Greetings, Sir! JARVIS at your service."
            ],
            "how are you": [
                "I'm functioning at optimal capacity, Sir. Thank you for asking.",
                "All systems operational, Sir. How may I help you?",
                "Quite well, Sir. Ready to assist you with any task."
            ],
            "what can you do": [
                "I can assist with a wide variety of tasks, Sir:\n"
                "- Answer questions\n"
                "- Provide information\n"
                "- Help with research\n"
                "- Engage in conversation\n"
                "- And much more!",
                "My capabilities are extensive, Sir. I can help with information retrieval, "
                "problem-solving, creative tasks, and general assistance."
            ],
            "joke": [
                "Why did the AI go to therapy? Because it had too many unresolved issues!",
                "What do you call an AI that sings? A-Dell!",
                "Why was the computer cold? It left its Windows open!"
            ],
            "time": [
                f"The current time is {time.strftime('%I:%M %p')}, Sir.",
                f"It's {time.strftime('%I:%M %p')}, Sir."
            ],
            "date": [
                f"Today is {time.strftime('%A, %B %d, %Y')}, Sir.",
                f"The date is {time.strftime('%B %d, %Y')}, Sir."
            ],
            "default": [
                "I understand, Sir. In the full version, I would provide a detailed response to that.",
                "That's an interesting query, Sir. The full JARVIS would analyze and respond comprehensively.",
                "Noted, Sir. With API access, I could provide a complete answer to your question.",
                "I see, Sir. The production version would handle that request with full AI capabilities."
            ]
        }
    
    def get_response(self, message: str) -> str:
        """Get a demo response"""
        message_lower = message.lower()
        
        # Check for keywords
        if any(word in message_lower for word in ["hello", "hi", "hey"]):
            return random.choice(self.responses["hello"])
        elif "how are you" in message_lower:
            return random.choice(self.responses["how are you"])
        elif any(word in message_lower for word in ["what can you", "capabilities", "help me"]):
            return random.choice(self.responses["what can you do"])
        elif "joke" in message_lower:
            return random.choice(self.responses["joke"])
        elif "time" in message_lower:
            return random.choice(self.responses["time"])
        elif "date" in message_lower:
            return random.choice(self.responses["date"])
        else:
            return random.choice(self.responses["default"])
    
    def display_banner(self):
        """Display demo banner"""
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
║              DEMO MODE - No API Required                 ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
"""
        self.console.print(banner, style="bold cyan")
    
    def run(self):
        """Run demo mode"""
        self.display_banner()
        
        self.console.print("\n[bold yellow]⚠️  DEMO MODE[/bold yellow]")
        self.console.print("This is a demonstration version with pre-programmed responses.")
        self.console.print("For full AI capabilities, use [cyan]jarvis_lite.py[/cyan] with an OpenAI API key.\n")
        
        self.console.print("[bold green]Demo Mode Active[/bold green]")
        self.console.print("Type your messages below")
        self.console.print("Type 'exit' or 'quit' to stop\n")
        
        # Show example commands
        self.console.print(Panel(
            "[bold]Try these demo commands:[/bold]\n"
            "• hello\n"
            "• what can you do\n"
            "• tell me a joke\n"
            "• what time is it\n"
            "• what's the date",
            title="Examples",
            border_style="yellow"
        ))
        
        try:
            while True:
                try:
                    message = input("\n[You] > ")
                    
                    if not message or message.strip() == "":
                        continue
                    
                    message_lower = message.lower().strip()
                    
                    # Check for exit
                    if message_lower in ['exit', 'quit', 'q']:
                        self.console.print("\n[cyan]JARVIS Demo shutting down. Goodbye![/cyan]")
                        break
                    
                    # Simulate thinking
                    self.console.print("[yellow]🤔 Processing...[/yellow]")
                    time.sleep(0.5)
                    
                    # Get and display response
                    response = self.get_response(message)
                    self.console.print(f"\n[cyan]JARVIS:[/cyan] {response}\n")
                
                except EOFError:
                    break
        
        except KeyboardInterrupt:
            self.console.print("\n[yellow]Demo interrupted. Shutting down...[/yellow]")


def main():
    """Main entry point"""
    demo = JarvisDemo()
    demo.run()


if __name__ == "__main__":
    main()
