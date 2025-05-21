def custom_logger(log_message):
    """Decorator that logs before and after function execution"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"LOG: {log_message} - Before calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"LOG: {log_message} - After calling {func.__name__}")
            return result
        return wrapper
    return decorator

@custom_logger("Test log")
def multiply(a, b):
    return a * b

def main():
    print(multiply(2, 3))

if __name__ == "__main__":
    main()
