if __name__ == "__main__":
    len = 5
    try:
        print(len("hello"))  # Will raise TypeError
    except TypeError as e:
        print("Error:", e)

    del len
    print(len("hello"))  # Now works
