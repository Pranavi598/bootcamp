import os
import shutil
from pathlib import Path


def main():
    # Create a directory and file inside it
    temp_dir = Path("temp_dir")
    temp_dir.mkdir(exist_ok=True)  # Create directory if not exists
    file_path = temp_dir / "temp_file.txt"
    file_path.write_text("Temporary file content")

    # Print the file content
    print(f"Content of {file_path}: {file_path.read_text()}")

    # Delete the temporary directory and all its contents
    shutil.rmtree(temp_dir)
    print(f"Deleted {temp_dir}")


if __name__ == "__main__":
    main()
