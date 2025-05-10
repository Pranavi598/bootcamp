import time

def timer(func):
    """Decorator to time the function execution"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function executed in {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    return "Done"

def main():
    print(slow_function())

if __name__ == "__main__":
    main()
