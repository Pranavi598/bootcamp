# main.py

from typing import List
from abstraction_level_3.types import ProcessorFn
from abstraction_level_3.core import process_lines
from abstraction_level_3.pipeline import load_pipeline

def main(input_path: str, output_path: str, config_path: str):
    # Load pipeline from YAML tracing
    processors: List[ProcessorFn] = load_pipeline(config_path)

    # Read input
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Process lines
    processed_lines = process_lines(lines, processors)

    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in processed_lines:
            f.write(line + '\n')

if __name__ == "__main__":
    # Example usage if you want to run it directly without CLI
    main('input.txt', 'out.txt', 'pipeline.yaml')
