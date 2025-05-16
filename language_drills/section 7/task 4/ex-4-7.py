import logging
import os
import psutil

# Setting up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def print_resource_usage():
    memory_info = psutil.virtual_memory()
    cpu_info = psutil.cpu_percent(interval=1)
    logger.info(f"Memory Usage: {memory_info.percent}%")
    logger.info(f"CPU Usage: {cpu_info}%")

def main():
    print_resource_usage()

if __name__ == "__main__":
    main()
