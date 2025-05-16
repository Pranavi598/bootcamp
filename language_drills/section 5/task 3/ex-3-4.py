from datetime import datetime

def main():
    # Parse "2024-01-01" into a datetime object
    date_string = "2024-01-01"
    parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
    print("Parsed date:", parsed_date)

if __name__ == "__main__":
    main()
