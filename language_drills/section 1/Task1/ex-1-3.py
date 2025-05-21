import copy


def list_copy_pitfall():
    """
    Demonstrates the difference between a = b and a = b[:] using the copy module.
    """
    a = [1, 2, 3]
    b = a
    b[0] = 9

    # Using deepcopy to demonstrate the difference
    a_copy = copy.copy(a)  # Shallow copy (same reference)
    a_copy_2 = a[:]  # Copy using slicing
    return a, b, a_copy, a_copy_2


if __name__ == "__main__":
    # 3. List Copying Pitfall
    a, b, a_copy, a_copy_2 = list_copy_pitfall()
    print(f"a: {a}, b: {b}, a_copy (copy): {a_copy}, a_copy_2 (slice): {a_copy_2}")
