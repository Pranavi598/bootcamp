from datetime import datetime


def main():
    # Round the current time to the top of the hour
    current_time = datetime.now()
    rounded_time = current_time.replace(minute=0, second=0, microsecond=0)
    if current_time.minute > 0:
        rounded_time = rounded_time.replace(hour=current_time.hour + 1)

    print("Rounded time:", rounded_time)


if __name__ == "__main__":
    main()
