def add_all(*args: int) -> int:
    return sum(args)

if __name__ == "__main__":
    result = add_all()  # Calling with no arguments
    print(f"Result: {result}")  # Printing the result
