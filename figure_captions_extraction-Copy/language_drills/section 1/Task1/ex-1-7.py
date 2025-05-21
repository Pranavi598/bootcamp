from operator import itemgetter

def tuple_unpacking(t):
    """
    Unpacks a tuple into individual elements using itemgetter.
    """
    x, y, z = itemgetter(0, 1, 2)(t)  # Unpacking tuple
    return x, y, z

if __name__ == "__main__":
    # 7. Tuple Unpacking
    t = (7, 8, 9)
    x, y, z = tuple_unpacking(t)
    print(f"Unpacked Tuple: x={x}, y={y}, z={z}")
