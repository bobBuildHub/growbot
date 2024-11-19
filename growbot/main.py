"""
main.py: Entry point for GrowBot system orchestration.
"""
import sys
import multiprocessing
import logging
import time  # Import the time module
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress
from rich.traceback import install
from bots.customer_bot import start_customer_bot
from bots.admin_bot import start_admin_bot
from utils.config_loader import ConfigLoader

# Enable pretty tracebacks
install(show_locals=True)

# Initialize Rich Console
console = Console()

def setup_rich_logger():
    """
    Configure logging with Rich integration.
    """
    rich_handler = logging.StreamHandler()
    logging.basicConfig(level=logging.INFO, handlers=[rich_handler])
    return logging.getLogger("GrowBot")

# Load configuration
config = ConfigLoader("config/config.json").get_config()
logger = setup_rich_logger()

def display_startup_sequence():
    """
    Display a pretty startup sequence.
    """
    table = Table(title="GrowBot Startup")
    table.add_column("Component", justify="left", style="cyan", no_wrap=True)
    table.add_column("Status", justify="right", style="green")
    table.add_row("Customer Bot", ":hourglass_flowing_sand: Initializing...")
    table.add_row("Admin Bot", ":hourglass_flowing_sand: Initializing...")
    console.print(table)

    # Simulate loading
    with Progress() as progress:
        task = progress.add_task("[cyan]Launching Bots...", total=100)
        for _ in range(5):
            progress.update(task, advance=20)
            time.sleep(0.5)  # Simulate delay for progress

def main():
    """
    Main entry point for GrowBot.
    """
    console.rule("[bold green]GrowBot System Initializing[/bold green]")
    display_startup_sequence()

    customer_process = multiprocessing.Process(
        target=start_customer_bot, args=(config["tokens"]["customer_bot"], config)
    )
    admin_process = multiprocessing.Process(
        target=start_admin_bot, args=(config["tokens"]["admin_bot"],)
    )

    customer_process.start()
    admin_process.start()
    console.print(Panel("[bold white on green] All Bots Online [/bold white on green]"))

    try:
        customer_process.join()
        admin_process.join()
    except KeyboardInterrupt:
        console.print(Panel("[bold white on red] System Shutdown Initiated [/bold white on red]"))
        customer_process.terminate()
        admin_process.terminate()
        console.print("[bold red]All processes terminated.[/bold red]")

if __name__ == "__main__":
    main()
