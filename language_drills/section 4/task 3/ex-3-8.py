import functools

def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    """Adds two numbers"""
    return a + b

def main():
    # Test the decorated function
    print(add(2, 3))  # Should print log messages before and after the function call

if __name__ == "__main__":
    main()
