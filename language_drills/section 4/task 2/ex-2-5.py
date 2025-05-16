def debug_info(func):
    """Decorator to print function name, arguments, and return value"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@debug_info
def add(a, b):
    return a + b

def main():
    print(add(2, 3))

if __name__ == "__main__":
    main()
