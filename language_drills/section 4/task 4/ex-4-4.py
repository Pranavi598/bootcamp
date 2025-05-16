import itertools


def main():
    # Flatten multiple iterators into a single iterator
    flattened = itertools.chain([1, 2], [3, 4], [5])

    for val in flattened:
        print(val)


if __name__ == "__main__":
    main()
