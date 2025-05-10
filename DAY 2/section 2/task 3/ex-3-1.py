# inline_conditional_example.py

def main():
    age = int(input("Enter your age: "))

    category = "Adult" if age >= 18 else "Minor"
    print(f"Category: {category}")


if __name__ == "__main__":
    main()
