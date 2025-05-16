def make_doubler():
    """Returns a function that doubles its input"""
    return lambda x: x * 2

def main():
    doubler = make_doubler()
    result = doubler(5)
    print(result)  # Output: 10

if __name__ == "__main__":
    main()
