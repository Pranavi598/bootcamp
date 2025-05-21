from pathlib import Path

def main():
    # Show absolute path using pathlib.Path.resolve()
    relative_path = Path("myfile.txt")
    absolute_path = relative_path.resolve()
    print(f"Absolute path: {absolute_path}")

if __name__ == "__main__":
    main()
