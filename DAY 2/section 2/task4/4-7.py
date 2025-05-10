# database_style_locking_example.py

class DBConnection:
    def __enter__(self):
        print("Opening DB connection...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing DB connection...")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return True  # Suppress exception

def main():
    with DBConnection() as db:
        print("Performing database operations.")
        # Uncomment to test exception handling
        # raise ValueError("Test DB operation error")

if __name__ == "__main__":
    main()
