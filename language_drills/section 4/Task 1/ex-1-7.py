def compose(f, g):
    """Compose two functions f and g: compose(f, g)(x) is f(g(x))"""
    return lambda x: f(g(x))

def main():
    add_one = lambda x: x + 1
    double = lambda x: x * 2
    composed_function = compose(add_one, double)
    result = composed_function(3)
    print(result)  # Output: 7 (because double(3) is 6, add_one(6) is 7)

if __name__ == "__main__":
    main()
