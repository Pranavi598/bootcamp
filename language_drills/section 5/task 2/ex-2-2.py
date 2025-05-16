from pathlib import Path


def main():
    # List all Python files in the current directory
    py_files = Path(".").glob("*.py")

    # Print the Python files
    for py_file in py_files:
        print(py_file)


if __name__ == "__main__":
    main()
