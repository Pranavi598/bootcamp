import numpy as np

def list_comprehension_with_condition(lst):
    """
    Using list comprehension with a condition to create a new list of squares.
    """
    return [x ** 2 for x in lst if x % 2 == 0]

if __name__ == "__main__":
    # 2. List Comprehension with Condition
    lst = [1, 2, 3, 4]
    result = list_comprehension_with_condition(lst)
    print("List Comprehension with Condition Result:", result)
