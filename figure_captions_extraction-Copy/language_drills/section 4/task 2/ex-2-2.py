def prefix_printer(prefix):
    """Decorator that prints a prefix before calling the function"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix}: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@prefix_printer("Calling")
def greet(name):
    return f"Hello, {name}!"

def main():
    print(greet("Bob"))

if __name__ == "__main__":
    main()
