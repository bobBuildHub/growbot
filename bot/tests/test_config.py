
from utils.config_loader import ConfigLoader
from rich.console import Console

console = Console()

def test_load_valid_config():
    loader = ConfigLoader()
    config = loader.get_config()
    if "database" in config and "logging" in config:
        console.print("[bold green]✅ test_load_valid_config passed.[/bold green]")
    else:
        console.print("[bold red]❌ test_load_valid_config failed.[/bold red]")

def test_missing_config_file():
    loader = ConfigLoader()
    loader.config_path = "nonexistent.json"
    try:
        loader.get_config()
        console.print("[bold red]❌ test_missing_config_file failed.[/bold red]")
    except FileNotFoundError:
        console.print("[bold green]✅ test_missing_config_file passed.[/bold green]")

if __name__ == "__main__":
    test_load_valid_config()
    test_missing_config_file()
