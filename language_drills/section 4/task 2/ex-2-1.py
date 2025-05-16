def simple_logger(func):
    """Decorator to log function start and end"""
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper

@simple_logger
def greet(name):
    return f"Hello, {name}!"

def main():
    print(greet("Alice"))

if __name__ == "__main__":
    main()
