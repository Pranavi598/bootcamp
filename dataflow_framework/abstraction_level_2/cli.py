import typer
from abstraction_level_2.main import process

app = typer.Typer()

@app.command()
def run(input: str, output: str = None, mode: str = "uppercase"):
    """Process the input file and apply the selected mode."""
    print(f"Received input: {input}, output: {output}, mode: {mode}")
    process(input=input, output=output, mode=mode)


if __name__ == "__main__":
    app()
