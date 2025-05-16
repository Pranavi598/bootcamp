# eafp_file_open.py

def main():
    filename = "nonexistent.txt"

    try:
        with open(filename, "r") as f:
            content = f.read()
            print("[EAFP] File content:", content)
    except FileNotFoundError:
        print("[EAFP] File not found!")

if __name__ == "__main__":
    main()
