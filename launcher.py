"""
JARVIS Launcher Menu
Easy way to start any version of JARVIS
"""

import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def display_banner():
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
║              Launcher Menu                               ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
"""
    console.print(banner, style="bold cyan")

def main():
    """Main launcher menu"""
    display_banner()
    
    console.print("\n[bold cyan]Welcome to JARVIS AI Assistant![/bold cyan]\n")
    
    # Create options table
    table = Table(title="Available Options", show_header=True, header_style="bold magenta")
    table.add_column("Option", style="cyan", width=8)
    table.add_column("Name", style="yellow", width=20)
    table.add_column("Description", style="green")
    
    table.add_row("1", "JARVIS Dashboard", "Web interface control center (New!)")
    table.add_row("2", "JARVIS Demo", "Test without API key (pre-programmed)")
    table.add_row("3", "JARVIS Lite", "Full AI with voice (requires API key)")
    table.add_row("4", "JARVIS Enhanced", "Advanced with code execution")
    table.add_row("5", "System Check", "Verify installation")
    table.add_row("6", "Help", "View documentation")
    table.add_row("7", "Exit", "Close launcher")
    
    console.print(table)
    console.print()
    
    # Get user choice
    while True:
        try:
            choice = input("\n[bold yellow]Select an option (1-7):[/bold yellow] ").strip()
            
            if choice == "1":
                console.print("\n[cyan]Starting JARVIS Dashboard Server...[/cyan]\n")
                console.print("[yellow]The dashboard will open in your browser automatically.[/yellow]")
                os.system("python dashboard_server.py")
                break
                
            elif choice == "2":
                console.print("\n[cyan]Starting JARVIS Demo...[/cyan]\n")
                os.system("python jarvis_demo.py")
                break
            
            elif choice == "3":
                console.print("\n[cyan]Starting JARVIS Lite...[/cyan]\n")
                os.system("python jarvis_lite.py")
                break
            
            elif choice == "4":
                console.print("\n[cyan]Starting JARVIS Enhanced...[/cyan]\n")
                if sys.version_info >= (3, 13):
                    console.print("[red]⚠️  JARVIS Enhanced requires Python 3.9-3.12[/red]")
                    console.print("[yellow]You have Python 3.13+[/yellow]")
                    console.print("[yellow]Please use JARVIS Lite or Dashboard instead[/yellow]\n")
                    continue
                os.system("python jarvis_enhanced.py")
                break
            
            elif choice == "5":
                console.print("\n[cyan]Running System Check...[/cyan]\n")
                os.system("python check_system.py")
                input("\nPress Enter to continue...")
                main()  # Return to menu
                break
            
            elif choice == "6":
                console.print("\n[bold cyan]Documentation Files:[/bold cyan]\n")
                console.print("📖 [yellow]START_HERE.md[/yellow] - Quick overview")
                console.print("📖 [yellow]QUICK_START.md[/yellow] - Step-by-step guide")
                console.print("📖 [yellow]README_JARVIS.md[/yellow] - Complete documentation")
                console.print("📖 [yellow]SETUP_COMPLETE.md[/yellow] - Setup summary\n")
                
                doc_choice = input("Open START_HERE.md? (y/n): ").strip().lower()
                if doc_choice == 'y':
                    os.system("notepad START_HERE.md" if os.name == 'nt' else "cat START_HERE.md")
                
                input("\nPress Enter to continue...")
                main()  # Return to menu
                break
            
            elif choice == "7":
                console.print("\n[cyan]Goodbye![/cyan]\n")
                break
            
            else:
                console.print("[red]Invalid option. Please choose 1-7.[/red]")
        
        except KeyboardInterrupt:
            console.print("\n\n[yellow]Launcher interrupted. Goodbye![/yellow]\n")
            break
        except Exception as e:
            console.print(f"\n[red]Error: {e}[/red]\n")
            break

if __name__ == "__main__":
    main()
