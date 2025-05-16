from datetime import datetime, timedelta

def main():
    # Add 7 days to the current date using timedelta
    current_time = datetime.now()
    new_time = current_time + timedelta(days=7)
    print("New time after adding 7 days:", new_time)

if __name__ == "__main__":
    main()
