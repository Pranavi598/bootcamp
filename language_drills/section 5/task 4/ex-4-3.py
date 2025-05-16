import csv

def main():
    # Read data.csv and print each row using csv.DictReader
    with open('data.csv', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row)

if __name__ == "__main__":
    main()
