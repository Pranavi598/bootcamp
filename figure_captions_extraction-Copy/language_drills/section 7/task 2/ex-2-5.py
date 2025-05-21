import itertools


def main():
    large_data = (i for i in range(1000000))
    first_10 = itertools.islice(large_data, 10)

    for item in first_10:
        print(item)


if __name__ == "__main__":
    main()
