# suppressing_exceptions_example.py
import contextlib

def main():
    with contextlib.suppress(FileNotFoundError):
        with open('non_existent_file.txt', 'r') as f:
            content = f.read()
            print(content)

    print("The exception was suppressed.")

if __name__ == "__main__":
    main()
