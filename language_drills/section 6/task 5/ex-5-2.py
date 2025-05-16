MAX_RETRIES = 3  # Instead of magic number

def attempt_connection():
    for attempt in range(MAX_RETRIES):
        print(f"Attempt {attempt + 1}: Trying to connect...")

def main():
    attempt_connection()

if __name__ == "__main__":
    main()
