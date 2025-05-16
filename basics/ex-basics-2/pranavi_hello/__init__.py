# pranavi_hello/__init__.py
from rich.console import Console

console = Console()

def say_hello(name: str = "world") -> str:
    message = f"Hello, [bold magenta]{name}[/bold magenta]!"
    console.print(message)
    return message
