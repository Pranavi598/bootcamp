from collections import defaultdict


def main():
    # Build a defaultdict with another defaultdict to represent hierarchical data
    nested_dict = defaultdict(lambda: defaultdict(int))

    # Increment values in nested defaultdict
    nested_dict['fruit']['apple'] += 1
    nested_dict['fruit']['banana'] += 2
    nested_dict['vegetable']['carrot'] += 1

    # Print nested defaultdict
    for category, items in nested_dict.items():
        print(f"{category}: {dict(items)}")


if __name__ == "__main__":
    main()
