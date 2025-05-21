import itertools


def main():
    # Duplicate an iterator and iterate independently on both copies
    original = itertools.count(start=1)
    iter1, iter2 = itertools.tee(original, 2)

    # Consume the first few elements in iter1 and iter2 independently
    print("Iter1:")
    for _ in range(3):
        print(next(iter1))

    print("Iter2:")
    for _ in range(3):
        print(next(iter2))


if __name__ == "__main__":
    main()
