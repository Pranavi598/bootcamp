# custom_context_manager_decorator_example.py
import contextlib
import time

@contextlib.contextmanager
def timer():
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        print(f"Operation took {end_time - start_time} seconds.")

def main():
    with timer():
        print("Performing a task...")
        time.sleep(2)

if __name__ == "__main__":
    main()
