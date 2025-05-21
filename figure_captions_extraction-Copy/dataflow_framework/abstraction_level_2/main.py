import os
from dotenv import load_dotenv
from abstraction_level_2.core import to_uppercase, to_snakecase
from abstraction_level_2.pipeline import build_pipeline
from abstraction_level_2.types import ProcessorFn

# Load environment variables from .env
load_dotenv()


def read_lines(path: str):
    """Read lines from a file."""
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


def write_output(lines, output_path: str):
    """Write processed lines to the output."""
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line + '\n')
    else:
        for line in lines:
            print(line)


def process(input: str, output: str = None, mode: str = "uppercase"):
    """Process the input based on the selected mode and write output."""
    selected_mode = mode or os.getenv("MODE", "uppercase")

    pipeline = build_pipeline(selected_mode)
    lines = read_lines(input)

    for processor in pipeline:
        lines = (processor(line) for line in lines)

    write_output(lines, output)
