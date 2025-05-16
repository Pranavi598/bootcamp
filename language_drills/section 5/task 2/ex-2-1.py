from pathlib import Path


def main():
    # Read content of 'myfile.txt' using pathlib
    file_path = Path("myfile.txt")

    # Ensure the file exists
    if file_path.exists() and file_path.is_file():
        content = file_path.read_text()
        print("File content:", content)
    else:
        print("File not found")


if __name__ == "__main__":
    main()
