import itertools


def main():
    # Generate all pairs (2-element permutations) from [1, 2, 3]
    pairs = itertools.permutations([1, 2, 3], 2)
    print("Permutations:")
    for pair in pairs:
        print(pair)

    # Generate all triples (3-element combinations) from [1, 2, 3]
    triples = itertools.combinations([1, 2, 3], 3)
    print("\nCombinations:")
    for triple in triples:
        print(triple)


if __name__ == "__main__":
    main()
