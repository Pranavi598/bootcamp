import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """This function greets a person"""
    return f"Hello, {name}!"

def main():
    # Use the decorated function
    print(greet("Alice"))
    print(greet.__name__)  # Should print greet
    print(greet.__doc__)   # Should print "This function greets a person"

if __name__ == "__main__":
    main()
