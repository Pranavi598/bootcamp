def divide(a, b):
    if b == 0:
        # Avoid division by zero
        return "Error: Division by zero"
    return a / b

def main():
    print(divide(10, 2))
    print(divide(10, 0))

if __name__ == "__main__":
    main()
