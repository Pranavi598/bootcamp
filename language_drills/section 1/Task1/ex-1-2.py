from itertools import islice

def list_slicing(lst):
    """
    Extract the middle 3 elements using itertools.islice.
    """
    start = len(lst) // 2 - 1
    end = start + 3
    return list(islice(lst, start, end))

if __name__ == "__main__":
    # 2. List Slicing
    lst = [1, 2, 3, 4, 5, 6, 7]
    middle_elements = list_slicing(lst)
    print("Middle 3 elements:", middle_elements)
