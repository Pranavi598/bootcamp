# ensure_cleanup_example.py

class CleanupContextManager:
    def __enter__(self):
        print("Entering the context.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context, ensuring cleanup.")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return False  # Propagate exception


def main():
    with CleanupContextManager() as cm:
        print("Inside the context.")
        # Uncomment to test exception propagation
        # raise ValueError("Test exception")


if __name__ == "__main__":
    main()
