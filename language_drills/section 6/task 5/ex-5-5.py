def is_valid_number(n):
    return n > 0

def process_numbers(numbers):
    for num in numbers:
        if is_valid_number(num):
            print(f"Processing: {num}")

def main():
    numbers = [1, -3, 4, 0, 7]
    process_numbers(numbers)

if __name__ == "__main__":
    main()
