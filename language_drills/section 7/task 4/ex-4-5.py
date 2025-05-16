import logging

# Setting up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def health_check():
    # In a real scenario, this could check system resources, database connections, etc.
    logger.info("Health check passed: System is running fine.")
    return "Healthy"

def main():
    print(health_check())

if __name__ == "__main__":
    main()
