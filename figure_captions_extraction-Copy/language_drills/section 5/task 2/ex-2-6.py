import shutil
from pathlib import Path


def main():
    # Copy a file using shutil
    source_file = Path("source.txt")
    destination_file = Path("destination.txt")

    # Create a sample file
    source_file.write_text("Sample file content")

    # Copy file
    shutil.copy(source_file, destination_file)
    print(f"File copied from {source_file} to {destination_file}")


if __name__ == "__main__":
    main()
