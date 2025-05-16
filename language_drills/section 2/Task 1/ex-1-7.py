# eafp_safe_conversion.py

def main():
    user_input = input("Enter a number: ")

    try:
        number = int(user_input)
        print(f"[EAFP] You entered: {number}")
    except ValueError:
        print("[EAFP] Invalid number!")

if __name__ == "__main__":
    main()

