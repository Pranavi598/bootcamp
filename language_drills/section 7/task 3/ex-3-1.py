import pdb

def example_function(x, y):
    result = x + y
    pdb.set_trace()  # This will pause execution and allow debugging
    return result

def main():
    x = 5
    y = 10
    print(example_function(x, y))

if __name__ == "__main__":
    main()
