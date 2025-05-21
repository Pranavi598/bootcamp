import logging

# Setting up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def example_function():
    try:
        1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        error_code = 1001  # Example error code
        logger.error(f"Error occurred. Error ID: {error_code}, Message: {e}")
        raise

def main():
    try:
        example_function()
    except Exception:
        pass

if __name__ == "__main__":
    main()
