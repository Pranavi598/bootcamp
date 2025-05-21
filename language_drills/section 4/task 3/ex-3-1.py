import functools


def main():
    # Create a partial function for base 2 conversion (binary)
    int_base_2 = functools.partial(int, base=2)

    # Test the partial function
    print(int_base_2('1010'))  # Should print 10 (binary 1010)


if __name__ == "__main__":
    main()
