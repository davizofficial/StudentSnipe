import time
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box
from rich.progress import Progress, SpinnerColumn, TextColumn
from datetime import datetime

console = Console()

# ANSI escape code untuk warna (backward compatibility)
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def tampilkan_header():
    clear_screen()
    banner = """

                                      ____    _     __     _    ____
                                     |####`--|#|---|##|---|#|--'##|#|
   _                                 |____,--|#|---|##|---|#|--.__|_|
 _|#)_____________________________________,--'EEEEEEEEEEEEEE'_=-.
((_____((_________________________,--------[JW](___(____(____(_==)        _________
                               .--|##,----o  o  o  o  o  o  o__|/`---,-,-'=========`=+==.
                               |##|_Y__,__.-._,__,  __,-.___/ J \ .----.#############|##|
                               |##|              `-.|#|##|#|`===l##\   _\############|##|
                              =======-===l          |_|__|_|     \##`-"__,=======.###|##|
                                                                  \__,"          '======'

     Doxing Student Indonesian Campus
"""
    
    console.print(banner, style="cyan")
    console.print(Panel(
        "[yellow]DISCLAIMER:[/yellow] This tool is for educational use only.\n"
        "I do not promote cybercrime or misuse.\n"
        "Use it responsibly for learning and ethical research only.",
        border_style="yellow"
    ))
    console.print()

def tampilkan_data(data):
    """Tampilkan single data mahasiswa dalam bentuk tabel"""
    table = Table(title=" Data Mahasiswa Ditemukan", box=box.ROUNDED, show_header=True, header_style="bold cyan")
    table.add_column("Field", style="cyan", width=20)
    table.add_column("Value", style="white")
    
    for key, value in data.items():
        table.add_row(key, str(value))
    
    console.print(table)

def tampilkan_multiple_data(data_list):
    """Tampilkan multiple data mahasiswa dalam bentuk tabel"""
    table = Table(
        title=f" Ditemukan {len(data_list)} Mahasiswa",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold cyan"
    )
    
    table.add_column("No", style="yellow", width=4)
    table.add_column("Nama", style="green", width=25)
    table.add_column("NIM", style="cyan", width=15)
    table.add_column("Program Studi", style="white", width=30)
    table.add_column("Perguruan Tinggi", style="magenta", width=30)
    
    for idx, data in enumerate(data_list, 1):
        table.add_row(
            str(idx),
            data.get("Nama", "-"),
            data.get("NIM", "-"),
            data.get("Program Studi", "-"),
            data.get("Perguruan Tinggi", "-")
        )
    
    console.print(table)

def tampilkan_tidak_ditemukan():
    console.print(Panel(
        "[red] Data mahasiswa tidak ditemukan atau tidak terdaftar.[/red]",
        border_style="red"
    ))

def tampilkan_history(history_list):
    """Tampilkan history pencarian"""
    if not history_list:
        console.print("[yellow]Belum ada history pencarian.[/yellow]")
        return
    
    table = Table(title=" History Pencarian", box=box.ROUNDED, show_header=True, header_style="bold cyan")
    table.add_column("No", style="yellow", width=4)
    table.add_column("Query", style="green", width=30)
    table.add_column("Type", style="cyan", width=10)
    table.add_column("Results", style="white", width=8)
    table.add_column("Timestamp", style="magenta", width=20)
    
    for idx, item in enumerate(history_list[:10], 1):  # Show last 10
        timestamp = datetime.fromisoformat(item['timestamp']).strftime("%Y-%m-%d %H:%M")
        table.add_row(
            str(idx),
            item['query'],
            item['search_type'],
            str(item['result_count']),
            timestamp
        )
    
    console.print(table)

def show_loading(message="Searching..."):
    """Show loading spinner"""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description=message, total=None)
        time.sleep(1)
