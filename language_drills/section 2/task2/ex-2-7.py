# map_filter_example.py

def main():
    numbers = [1, 2, 3, 4, 5]

    doubled_numbers = list(map(lambda x: x * 2, numbers))
    print(f"Doubled numbers: {doubled_numbers}")

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {even_numbers}")


if __name__ == "__main__":
    main()

