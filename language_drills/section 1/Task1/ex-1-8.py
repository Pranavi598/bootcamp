def immutable_tuple_error():
    """
    Demonstrates the immutability of tuples by trying to modify an element.
    """
    t = (1, 2, 3)
    try:
        t[0] = 9
    except TypeError as e:
        return str(e)

if __name__ == "__main__":
    # 8. Immutable Tuple Error
    error_message = immutable_tuple_error()
    print("Immutable Tuple Error:", error_message)
