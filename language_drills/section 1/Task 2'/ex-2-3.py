import argparse

def dict_comprehension(lst):
    """
    Converts a list of strings into a dictionary with each string as a key and 1 as value.
    """
    return {x: 1 for x in lst}

def main():
    # Command Line Task 3
    lst = ["a", "b"]
    result = dict_comprehension(lst)
    print("Dict Comprehension Result:", result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dict Comprehension")
    args = parser.parse_args()
    main()
