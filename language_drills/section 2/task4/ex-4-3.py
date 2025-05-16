# custom_context_manager_class_example.py

class MyContextManager:
    def __enter__(self):
        print("Entering the context.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context.")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return True  # Suppress exception


def main():
    with MyContextManager() as cm:
        print("Inside the context.")
        # Uncomment to test exception handling
        # raise ValueError("Test exception")


if __name__ == "__main__":
    main()
