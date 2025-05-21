# cli.py
import argparse
from abstraction_level_4.main import main

def parse_arguments():
    parser = argparse.ArgumentParser(description="Stream Processing Pipeline")
    parser.add_argument('--input', type=str, required=True, help='Input file path')
    parser.add_argument('--output', type=str, required=True, help='Output file path')
    parser.add_argument('--tracing', type=str, required=True, help='Configuration YAML file path')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    main(args.input, args.output, args.config)
