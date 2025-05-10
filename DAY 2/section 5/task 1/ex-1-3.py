from collections import Counter


def main():
    # Use Counter to find the 2 most common elements in a list of numbers
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    num_counter = Counter(numbers)

    # Print the 2 most common elements
    print(num_counter.most_common(2))


if __name__ == "__main__":
    main()
