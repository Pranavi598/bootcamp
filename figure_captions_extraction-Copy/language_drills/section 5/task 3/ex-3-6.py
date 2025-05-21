from datetime import datetime


def main():
    # Compare two dates and print which is earlier
    date1 = datetime(2024, 1, 1)
    date2 = datetime(2025, 5, 7)

    if date1 < date2:
        print(f"{date1} is earlier than {date2}")
    elif date1 > date2:
        print(f"{date1} is later than {date2}")
    else:
        print(f"{date1} is the same as {date2}")


if __name__ == "__main__":
    main()
