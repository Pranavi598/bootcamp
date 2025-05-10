def simple_logger(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function executed in {end - start:.4f} seconds")
        return result
    return wrapper

def debug_info(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@simple_logger
@timer
@debug_info
def process_data(x, y):
    return x + y

def main():
    print(process_data(2, 3))

if __name__ == "__main__":
    main()
