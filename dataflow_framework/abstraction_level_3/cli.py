# abstraction_level_3/cli.py
import typer
from abstraction_level_3.main import main

app = typer.Typer()

@app.command()
def run(
    input: str = typer.Option(..., "--input", "-i", help="Path to input file"),
    output: str = typer.Option(..., "--output", "-o", help="Path to output file"),
    config: str = typer.Option(..., "--tracing", "-c", help="Path to pipeline YAML")
):
    main(input, output, config)

if __name__ == "__main__":
    app()
