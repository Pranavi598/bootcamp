from datetime import datetime

def main():
    # Format today's date as "YYYY-MM-DD"
    current_time = datetime.now()
    formatted_date = current_time.strftime("%Y-%m-%d")
    print("Formatted date:", formatted_date)

if __name__ == "__main__":
    main()
