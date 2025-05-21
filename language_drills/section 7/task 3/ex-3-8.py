import logging

# Setting up logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def example_function(x, y):
    try:
        result = x / y
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        raise  # Re-raise the exception after logging it
    return result

def main():
    try:
        print(example_function(5, 0))
    except Exception as e:
        print(f"Handled exception: {e}")

if __name__ == "__main__":
    main()
