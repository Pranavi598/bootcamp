def main():
    even_numbers = filter(lambda x: x % 2 == 0, range(10))
    print(list(even_numbers))  # Output: [0, 2, 4, 6, 8]

if __name__ == "__main__":
    main()
