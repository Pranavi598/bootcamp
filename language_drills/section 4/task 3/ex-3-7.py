import functools
import collections


def main():
    # Use partial to create a defaultdict with a default factory function
    default_dict = functools.partial(collections.defaultdict, int)

    # Create a defaultdict with default value of 0
    d = default_dict()

    # Adding elements to the dictionary
    d['a'] += 1
    d['b'] += 2

    print(d)  # Should print defaultdict(<class 'int'>, {'a': 1, 'b': 2})


if __name__ == "__main__":
    main()
