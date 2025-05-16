import functools

def main():
    # Use reduce and lambda to compute the factorial of 5
    factorial = functools.reduce(lambda x, y: x * y, range(1, 6))
    print(factorial)  # Should print 120

if __name__ == "__main__":
    main()
