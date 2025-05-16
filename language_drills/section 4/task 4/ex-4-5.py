import itertools


def main():
    # Skip the first 3 elements, then take the next 4 from range(10)
    sliced = itertools.islice(range(10), 3, 7)

    for val in sliced:
        print(val)


if __name__ == "__main__":
    main()
