def main():
    numbers = [1, 2, 3]
    squared_numbers = map(lambda x: x ** 2, numbers)
    print(list(squared_numbers))  # Output: [1, 4, 9]

if __name__ == "__main__":
    main()
