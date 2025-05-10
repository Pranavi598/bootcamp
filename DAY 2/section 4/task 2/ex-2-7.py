import time

def retry(max_attempts):
    """Decorator to retry a function if it raises an exception"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    time.sleep(1)
            return None
        return wrapper
    return decorator

@retry(max_attempts=3)
def risky_function():
    raise ValueError("Something went wrong")

def main():
    print(risky_function())  # Will retry 3 times

if __name__ == "__main__":
    main()
