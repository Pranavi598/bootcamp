import itertools


def main():
    # Repeat None 10 times
    repeated_values = itertools.repeat(None, 10)

    for val in repeated_values:
        print(val)


if __name__ == "__main__":
    main()
