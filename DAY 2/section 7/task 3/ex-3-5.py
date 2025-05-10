import warnings

def example_function(x):
    if x < 0:
        warnings.warn("x is negative, this might cause issues", UserWarning)
    return x * 2

def main():
    result = example_function(-5)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
