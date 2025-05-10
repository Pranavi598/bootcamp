import typer
from typing import Optional, Iterator
from dotenv import load_dotenv
import os

app = typer.Typer()

# Load environment variables
load_dotenv()

def read_lines(path: str) -> Iterator[str]:
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line

def transform_line(line: str, mode: str) -> str:
    if mode == "snakecase":
        return line.strip().replace(" ", "_").lower()
    else:  # Default to uppercase
        return line.strip().upper()

def write_output(lines: Iterator[str], output_path: Optional[str]) -> None:
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line + '\n')
    else:
        for line in lines:
            print(line)

@app.command()
def process(
    input: str = typer.Option(..., help="Input file path"),
    output: Optional[str] = typer.Option(None, help="Output file path"),
    mode: Optional[str] = typer.Option(None, help="Processing mode: uppercase or snakecase")
):
    selected_mode = mode or os.getenv("MODE", "uppercase")
    lines = read_lines(input)
    transformed = (transform_line(line, selected_mode) for line in lines)
    write_output(transformed, output)

if __name__ == "__main__":
    app()
