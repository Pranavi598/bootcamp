# Using a generator to read a large file line by line

def read_large_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line

def main():
    filename = "large_file.txt"  # Ensure this file exists or change path
    for line in read_large_file(filename):
        print(line.strip())  # Do something with the line

if __name__ == "__main__":
    main()
