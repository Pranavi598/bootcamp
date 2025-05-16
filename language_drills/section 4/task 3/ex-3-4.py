import functools


def main():
    # Create a partial function to print a message with a prefix
    partial_print = functools.partial(print, end=" ")

    # Apply the partial function multiple times to customize print
    custom_print = functools.partial(partial_print, "Custom:")

    # Test the chained partial function
    custom_print("Hello, World!")


if __name__ == "__main__":
    main()
