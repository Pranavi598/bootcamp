def example_function():
    try:
        1 / 0  # Division by zero to trigger an error
    except Exception as e:
        print(type(e), e)  # Print exception type and message

def main():
    example_function()

if __name__ == "__main__":
    main()
