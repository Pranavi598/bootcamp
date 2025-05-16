from functools import reduce


def set_operations(a, b):
    """
    Perform set operations (intersection, union, and difference) using built-in set methods.
    """
    intersection = a & b  # Intersection
    union = a | b  # Union
    difference = a - b  # Difference

    # Using functools to reduce and apply a union on multiple sets
    all_sets = [a, b]
    union_all = reduce(lambda x, y: x | y, all_sets)

    return intersection, union, difference, union_all


if __name__ == "__main__":
    # 6. Set Operations
    a_set = {1, 2, 3}
    b_set = {3, 4}
    intersection, union, difference, union_all = set_operations(a_set, b_set)
    print(f"Intersection: {intersection}, Union: {union}, Difference: {difference}, Union All: {union_all}")
