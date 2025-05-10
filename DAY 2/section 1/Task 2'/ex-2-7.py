import argparse

def filter_with_comprehension(lst):
    """
    Filter even-length strings from a list using list comprehension.
    """
    return [word for word in lst if len(word) % 2 == 0]

def main():
    # Command Line Task 7
    lst = ["hi", "hello", "bye"]
    result = filter_with_comprehension(lst)
    print("Filtered Even-Length Strings:", result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter Even-Length Strings")
    args = parser.parse_args()
    main()
