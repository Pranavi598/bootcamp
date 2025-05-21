import calendar
from datetime import datetime

def main():
    # Get the name of the day for today's date
    current_time = datetime.now()
    weekday_name = calendar.day_name[current_time.weekday()]
    print("Today is:", weekday_name)

if __name__ == "__main__":
    main()
