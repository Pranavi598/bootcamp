from pathlib import Path

def main():
    # Write 'hello' to a file using pathlib
    file_path = Path("output.txt")
    file_path.write_text("hello")
    print("Text written to 'output.txt'")

if __name__ == "__main__":
    main()
