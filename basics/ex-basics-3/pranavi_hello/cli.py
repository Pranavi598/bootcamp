import typer
from rich import print
from pranavi_hello import say_hello

app = typer.Typer()

@app.command()
def hello(name: str = "world"):
    print(f"[bold green]Hello, {name}![/bold green]")

if __name__ == "__main__":
    app()
