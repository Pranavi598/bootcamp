# basic_file_context_example.py

def main():
    with open('sample.txt', 'w') as f:
        f.write("Hello, this is a test file.")

    with open('sample.txt', 'r') as f:
        content = f.read()
        print(f"File content: {content}")


if __name__ == "__main__":
    main()
