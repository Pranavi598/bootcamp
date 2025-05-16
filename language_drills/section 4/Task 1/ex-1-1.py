def apply(func, value):
    """Applies a function to a value"""
    return func(value)

def main():
    result = apply(abs, -5)
    print(result)  # Output: 5

if __name__ == "__main__":
    main()
