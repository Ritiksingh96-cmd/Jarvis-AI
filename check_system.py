"""
JARVIS System Check
Verifies all dependencies are installed correctly
"""

import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def check_module(module_name, import_name=None):
    """Check if a module is installed"""
    if import_name is None:
        import_name = module_name
    
    try:
        __import__(import_name)
        return True, "✅ Installed"
    except ImportError:
        return False, "❌ Not installed"

def main():
    """Run system check"""
    console.print("\n[bold cyan]JARVIS System Check[/bold cyan]\n")
    
    # Check Python version
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    console.print(f"[yellow]Python Version:[/yellow] {python_version}")
    
    if sys.version_info >= (3, 9):
        console.print("[green]✅ Python version compatible[/green]\n")
    else:
        console.print("[red]❌ Python 3.9+ required[/red]\n")
    
    # Create table
    table = Table(title="Dependency Check")
    table.add_column("Package", style="cyan")
    table.add_column("Status", style="magenta")
    table.add_column("Required For", style="yellow")
    
    # Check dependencies
    dependencies = [
        ("SpeechRecognition", "speech_recognition", "Voice input"),
        ("pyttsx3", "pyttsx3", "Text-to-speech"),
        ("rich", "rich", "Terminal UI"),
        ("openai", "openai", "AI responses (Lite)"),
        ("pyautogui", "pyautogui", "System control"),
    ]
    
    all_installed = True
    for package, import_name, purpose in dependencies:
        installed, status = check_module(package, import_name)
        table.add_row(package, status, purpose)
        if not installed:
            all_installed = False
    
    console.print(table)
    console.print()
    
    # Summary
    if all_installed:
        console.print(Panel(
            "[bold green]✅ All dependencies installed![/bold green]\n\n"
            "You can run JARVIS with:\n"
            "  [cyan]python jarvis_lite.py[/cyan]\n\n"
            "Or use the launcher:\n"
            "  [cyan]run_jarvis.bat[/cyan]",
            title="System Ready",
            border_style="green"
        ))
    else:
        console.print(Panel(
            "[bold red]❌ Missing dependencies![/bold red]\n\n"
            "Install missing packages with:\n"
            "  [cyan]pip install SpeechRecognition pyttsx3 rich openai pyautogui[/cyan]\n\n"
            "Or run the setup script:\n"
            "  [cyan]setup_jarvis.bat[/cyan]",
            title="Action Required",
            border_style="red"
        ))
    
    # Additional checks
    console.print("\n[bold cyan]Additional Information:[/bold cyan]\n")
    
    # Check for API key
    import os
    if os.getenv("OPENAI_API_KEY"):
        console.print("[green]✅ OPENAI_API_KEY environment variable is set[/green]")
    else:
        console.print("[yellow]⚠️  OPENAI_API_KEY not set (you'll be prompted when running JARVIS)[/yellow]")
    
    # Check for microphone
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        mic_list = sr.Microphone.list_microphone_names()
        if mic_list:
            console.print(f"[green]✅ Found {len(mic_list)} microphone(s)[/green]")
            console.print(f"[dim]   Default: {mic_list[0]}[/dim]")
        else:
            console.print("[yellow]⚠️  No microphones detected[/yellow]")
    except:
        console.print("[yellow]⚠️  Could not check microphone status[/yellow]")
    
    console.print()

if __name__ == "__main__":
    main()
