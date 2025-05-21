import logging
import time

# Setting up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def example_function():
    start_time = time.time()
    result = sum(range(1000000))  # Some operation
    end_time = time.time()
    execution_time = end_time - start_time
    logger.info(f"Function executed in {execution_time:.5f} seconds.")
    return result

def main():
    print(example_function())

if __name__ == "__main__":
    main()
