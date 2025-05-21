import itertools


def main():
    # Group a list of dicts by the 'category' key
    data = [
        {'name': 'apple', 'category': 'fruit'},
        {'name': 'carrot', 'category': 'vegetable'},
        {'name': 'banana', 'category': 'fruit'},
        {'name': 'spinach', 'category': 'vegetable'}
    ]

    # Sort data by category before applying groupby
    data.sort(key=lambda x: x['category'])

    # Group by category
    grouped = itertools.groupby(data, key=lambda x: x['category'])

    # Print the grouped items
    for category, items in grouped:
        print(f"Category: {category}")
        for item in items:
            print(f"  {item}")


if __name__ == "__main__":
    main()
