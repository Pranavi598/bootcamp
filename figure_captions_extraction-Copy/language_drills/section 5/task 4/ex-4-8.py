import csv
from collections import namedtuple


def main():
    # Use csv.reader with namedtuple to read structured rows
    Person = namedtuple("Person", ["name", "age", "city"])

    with open('data.csv', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            person = Person(*row)  # Create a Person namedtuple
            print(person)


if __name__ == "__main__":
    main()
