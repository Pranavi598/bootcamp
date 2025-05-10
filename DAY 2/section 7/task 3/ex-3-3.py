import traceback

def example_function():
    try:
        1 / 0  # Division by zero to trigger an error
    except Exception as e:
        print("An error occurred:", traceback.format_exc())  # Print detailed error trace

def main():
    example_function()

if __name__ == "__main__":
    main()
