import os
from abstraction_level_4.util.file_utils import read_input, write_output
from abstraction_level_4.processors.fan_in import join_two_lines
from abstraction_level_4.processors.fan_out import split_lines


def main():
    # Dynamically resolve file paths based on current script location
    base_dir = os.path.dirname(__file__)
    input_path = os.path.join(base_dir, "input.txt")
    output_path = os.path.join(base_dir, "out.txt")

    # Read input
    input_lines = read_input(input_path)
    print(f"Input lines: {input_lines}")

    # List of stream processors
    processors = [join_two_lines, split_lines]

    for processor in processors:
        print(f"Processing with {processor.__name__}")
        processed_lines = []
        for result in processor(input_lines):
            processed_lines.append(result)
        input_lines = processed_lines
        print(f"Processed output: {input_lines}")

    # Write output
    write_output(output_path, input_lines)


if __name__ == "__main__":
    main()
