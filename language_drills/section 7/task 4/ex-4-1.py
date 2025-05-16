import logging

# Setting up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def example_function(user_id):
    logger.info(f"Function started. User ID: {user_id}")
    result = 5 + 3  # Some operation
    logger.info(f"Function ended. User ID: {user_id}")
    return result

def main():
    user_id = 123
    print(example_function(user_id))

if __name__ == "__main__":
    main()
