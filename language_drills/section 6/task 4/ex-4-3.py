import logging

def main():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("ContextLogger")

    user = {"name": "Pranavi", "age": 24}
    logger.debug(f"User: {user['name']}, Age: {user['age']}")

if __name__ == "__main__":
    main()
