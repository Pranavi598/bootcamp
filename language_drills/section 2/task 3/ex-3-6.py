# use_or_as_fallback_example.py

def main():
    name = input("Enter your name: ") or "Anonymous"
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
