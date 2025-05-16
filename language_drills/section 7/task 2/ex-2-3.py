import csv

def csv_filter(filename, condition):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if condition(row):
                yield row

def main():
    filename = "data.csv"  # Ensure this file exists or change path
    condition = lambda row: int(row[2]) > 100  # Example condition: third column value > 100
    for row in csv_filter(filename, condition):
        print(row)

if __name__ == "__main__":
    main()
