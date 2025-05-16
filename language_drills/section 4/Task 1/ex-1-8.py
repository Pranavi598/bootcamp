def outer_function():
    multiplier = 2
    return lambda x: x * multiplier

def main():
    closure_function = outer_function()
    result = closure_function(5)
    print(result)  # Output: 10 (capturing multiplier = 2)

if __name__ == "__main__":
    main()
