import logging
from functools import wraps

# Setting up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def trace_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Function {func.__name__} started with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Function {func.__name__} ended with result: {result}")
        return result
    return wrapper

@trace_function
def example_function(x, y):
    return x + y

def main():
    print(example_function(3, 4))

if __name__ == "__main__":
    main()
