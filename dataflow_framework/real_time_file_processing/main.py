import argparse
import os
from utils.watch import process_file, watch_directory

# Define base directory relative to the location of this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define your directories
UNPROCESSED_DIR = os.path.join(BASE_DIR, "watch_directory", "unprocessed")
PROCESSED_DIR = os.path.join(BASE_DIR, "watch_directory", "processed")

def main():
    parser = argparse.ArgumentParser(description="File processing application.")
    parser.add_argument('--input', type=str, help='Path to a single file to process')
    parser.add_argument('--watch', action='store_true', help='Watch a directory for new files')

    args = parser.parse_args()

    if args.input:
        input_path = os.path.abspath(args.input)
        if not os.path.isfile(input_path):
            print(f"File not found: {input_path}")
            return
        process_file(input_path, PROCESSED_DIR)

    elif args.watch:
        os.makedirs(UNPROCESSED_DIR, exist_ok=True)
        os.makedirs(PROCESSED_DIR, exist_ok=True)
        print(f"Watching directory: {UNPROCESSED_DIR}")
        watch_directory(UNPROCESSED_DIR, PROCESSED_DIR)

    else:
        print("Please specify either --input <file> or --watch")

if __name__ == "__main__":
    main()
