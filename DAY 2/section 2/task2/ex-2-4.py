# sorted_with_key_example.py

def main():
    tuples = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]

    sorted_tuples = sorted(tuples, key=lambda x: x[1])  # Sort by second item
    print(f"Sorted tuples: {sorted_tuples}")


if __name__ == "__main__":
    main()
