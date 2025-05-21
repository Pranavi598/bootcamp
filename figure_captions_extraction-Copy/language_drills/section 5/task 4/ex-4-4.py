import csv


def main():
    # Write a list of dicts to a CSV file with headers
    data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"}
    ]

    with open('output.csv', mode='w', newline='') as file:
        fieldnames = ["name", "age", "city"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write data
        writer.writerows(data)

    print("CSV file written successfully.")


if __name__ == "__main__":
    main()
