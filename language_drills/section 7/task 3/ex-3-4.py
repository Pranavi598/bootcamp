import logging

# Setting up logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def example_function(x, y):
    logger.debug(f"Entering function with x={x} and y={y}")
    result = x + y
    logger.debug(f"Exiting function with result={result}")
    return result

def main():
    x = 5
    y = 10
    print(example_function(x, y))

if __name__ == "__main__":
    main()
