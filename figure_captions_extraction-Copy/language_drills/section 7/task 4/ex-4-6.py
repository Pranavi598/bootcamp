import logging
import time

# Setting up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

metrics = {
    'counter': 0,
    'timer': 0
}

def example_function():
    metrics['counter'] += 1
    start_time = time.time()
    result = sum(range(100000))  # Some operation
    end_time = time.time()
    metrics['timer'] += end_time - start_time
    return result

def main():
    example_function()
    print(f"Metrics: {metrics}")

if __name__ == "__main__":
    main()
