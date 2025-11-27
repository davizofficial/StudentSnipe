import time
import sys
import os

# Warn if running under wrong Python version
if sys.version_info.major < 3:
    print("\n\033[91m[!] ERROR: You are running this script with Python 2.\033[0m")
    print("    Please run it using: \033[93mpython3 main.py\033[0m\n")
    sys.exit(1)
elif sys.version_info < (3, 6):
    print("\n\033[91m[!] ERROR: Your Python version is too old.\033[0m")
    print("    This program requires Python 3.6 or newer.")
    print("    Please run it using: \033[93mpython3 main.py\033[0m\n")
    sys.exit(1)

# Check for missing dependencies
required_modules = ["data.display", "data.api_client", "rich", "inquirer"]
missing_modules = []

for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        missing_modules.append(module)

if missing_modules:
    print("\n\033[91m[!] Missing required dependencies.\033[0m")
    print("    Please install them by running:")
    print("    \033[93mpip install -r requirements.txt\033[0m\n")
    sys.exit(1)

# Safe to import now
import inquirer
from rich.console import Console
from rich.panel import Panel
from data.display import (
    tampilkan_header, tampilkan_data, tampilkan_multiple_data,
    tampilkan_tidak_ditemukan, tampilkan_history, console
)
from data.api_client import cari_mahasiswa, cari_mahasiswa_by_nim
from data.cache import get_cached_result, save_to_cache, add_to_history, load_history, clear_cache
from data.export import export_to_json, export_to_csv, export_to_txt
from data.batch import read_batch_file, process_batch

def main_menu():
    """Tampilkan main menu"""
    questions = [
        inquirer.List('action',
                     message="Pilih menu",
                     choices=[
                         (' Search by Name', 'search_name'),
                         (' Search by NIM', 'search_nim'),
                         (' Batch Search', 'batch'),
                         (' View History', 'history'),
                         ('  Clear Cache', 'clear_cache'),
                         (' Exit', 'exit')
                     ],
                     carousel=True
                     ),
    ]
    
    answers = inquirer.prompt(questions)
    return answers['action'] if answers else 'exit'

def search_by_name():
    """Search mahasiswa by name"""
    console.print("\n[cyan] Search by Name[/cyan]")
    nama = console.input("[yellow]Enter student name:[/yellow] ").strip()
    
    if not nama:
        console.print("[red]Name cannot be empty![/red]")
        return
    
    # Check cache first
    cached = get_cached_result(nama, "nama")
    if cached:
        console.print("[green]✓ Data loaded from cache[/green]")
        data = cached
    else:
        console.print("[yellow] Searching...[/yellow]")
        data = cari_mahasiswa(nama, return_all=True)
        
        if data:
            save_to_cache(nama, "nama", data)
    
    if data:
        if isinstance(data, list) and len(data) > 1:
            # Multiple results
            tampilkan_multiple_data(data)
            add_to_history(nama, "nama", len(data))
            
            # Ask if user wants to see details or export
            post_search_menu(data, nama)
        else:
            # Single result
            if isinstance(data, list):
                data = data[0]
            tampilkan_data(data)
            add_to_history(nama, "nama", 1)
            
            # Ask if user wants to export
            export_menu([data])
    else:
        tampilkan_tidak_ditemukan()
        add_to_history(nama, "nama", 0)

def search_by_nim():
    """Search mahasiswa by NIM"""
    console.print("\n[cyan] Search by NIM[/cyan]")
    nim = console.input("[yellow]Enter student NIM:[/yellow] ").strip()
    
    if not nim:
        console.print("[red]NIM cannot be empty![/red]")
        return
    
    # Check cache first
    cached = get_cached_result(nim, "nim")
    if cached:
        console.print("[green]✓ Data loaded from cache[/green]")
        data = cached
    else:
        console.print("[yellow] Searching...[/yellow]")
        data = cari_mahasiswa_by_nim(nim)
        
        if data:
            save_to_cache(nim, "nim", data)
    
    if data:
        tampilkan_data(data)
        add_to_history(nim, "nim", 1)
        
        # Ask if user wants to export
        export_menu([data])
    else:
        tampilkan_tidak_ditemukan()
        add_to_history(nim, "nim", 0)

def post_search_menu(data_list, query):
    """Menu setelah search dengan multiple results"""
    questions = [
        inquirer.List('action',
                     message="What do you want to do?",
                     choices=[
                         ('  View Details', 'details'),
                         (' Export Results', 'export'),
                         (' Back to Menu', 'back')
                     ],
                     ),
    ]
    
    answers = inquirer.prompt(questions)
    if not answers:
        return
    
    action = answers['action']
    
    if action == 'details':
        # Let user select which student to view
        choices = [(f"{d['Nama']} - {d['NIM']}", idx) for idx, d in enumerate(data_list)]
        choices.append((' Back', -1))
        
        detail_q = [
            inquirer.List('student',
                         message="Select student to view details",
                         choices=choices,
                         carousel=True
                         ),
        ]
        
        detail_ans = inquirer.prompt(detail_q)
        if detail_ans and detail_ans['student'] != -1:
            tampilkan_data(data_list[detail_ans['student']])
            console.input("\n[yellow]Press Enter to continue...[/yellow]")
    
    elif action == 'export':
        export_menu(data_list)

def export_menu(data):
    """Menu untuk export data"""
    questions = [
        inquirer.List('format',
                     message="Select export format",
                     choices=[
                         (' JSON', 'json'),
                         (' CSV', 'csv'),
                         (' TXT', 'txt'),
                         (' Skip', 'skip')
                     ],
                     ),
    ]
    
    answers = inquirer.prompt(questions)
    if not answers or answers['format'] == 'skip':
        return
    
    format_type = answers['format']
    
    if format_type == 'json':
        filepath = export_to_json(data)
    elif format_type == 'csv':
        filepath = export_to_csv(data)
    elif format_type == 'txt':
        filepath = export_to_txt(data)
    
    if filepath:
        console.print(f"[green]✓ Data exported to: {filepath}[/green]")
    else:
        console.print("[red]✗ Failed to export data[/red]")
    
    console.input("\n[yellow]Press Enter to continue...[/yellow]")

def batch_search():
    """Batch search from file"""
    console.print("\n[cyan] Batch Search[/cyan]")
    console.print("[yellow]Supported formats: TXT (one name per line) or CSV (first column)[/yellow]")
    
    filepath = console.input("[yellow]Enter file path:[/yellow] ").strip()
    
    if not os.path.exists(filepath):
        console.print("[red]File not found![/red]")
        console.input("\n[yellow]Press Enter to continue...[/yellow]")
        return
    
    queries = read_batch_file(filepath)
    if not queries:
        console.print("[red]No valid queries found in file![/red]")
        console.input("\n[yellow]Press Enter to continue...[/yellow]")
        return
    
    console.print(f"[green]Found {len(queries)} queries to process[/green]")
    
    # Ask search type
    type_q = [
        inquirer.List('type',
                     message="Search by",
                     choices=[
                         ('Name', 'nama'),
                         ('NIM', 'nim')
                     ],
                     ),
    ]
    
    type_ans = inquirer.prompt(type_q)
    if not type_ans:
        return
    
    search_type = type_ans['type']
    
    # Procesh
    results = process_batch(queries, search_type)
    
    if results:
        console.print(f"\n[green]✓ Found {len(results)} results[/green]")
        tampilkan_multiple_data(results)
        
        # Auto export
        export_menu(results)
    else:
        console.print("[red]No results found[/red]")
    
    console.input("\n[yellow]Press Enter to continue...[/yellow]")

def view_history():
    """View search history"""
    console.print("\n[cyan] Search History[/cyan]")
    history = load_history()
    tampilkan_history(history)
    console.input("\n[yellow]Press Enter to continue...[/yellow]")

def clear_cache_menu():
    """Clear cache"""
    confirm = [
        inquirer.Confirm('confirm',
                        message="Are you sure you want to clear cache?",
                        default=False),
    ]
    
    answers = inquirer.prompt(confirm)
    if answers and answers['confirm']:
        clear_cache()
        console.print("[green]✓ Cache cleared successfully[/green]")
    else:
        console.print("[yellow]Cache clear cancelled[/yellow]")
    
    console.input("\n[yellow]Press Enter to continue...[/yellow]")

def main():
    try:
        while True:
            tampilkan_header()
            action = main_menu()
            
            if action == 'exit':
                console.print("\n[cyan] Thanks for using StudentSnipe![/cyan]")
                break
            elif action == 'search_name':
                search_by_name()
            elif action == 'search_nim':
                search_by_nim()
            elif action == 'batch':
                batch_search()
            elif action == 'history':
                view_history()
            elif action == 'clear_cache':
                clear_cache_menu()
    
    except KeyboardInterrupt:
        console.print("\n\n[red]Operation canceled by user.[/red]")
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")

if __name__ == "__main__":
    main()
