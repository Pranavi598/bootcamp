def example_function(x, y):
    result = x + y
    breakpoint()  # This will pause execution and open the debugger in Python 3.7+
    return result

def main():
    x = 5
    y = 10
    print(example_function(x, y))

if __name__ == "__main__":
    main()
