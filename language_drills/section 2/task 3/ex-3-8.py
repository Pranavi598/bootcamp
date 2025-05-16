# conditional_expressions_in_comprehensions_example.py

def main():
    numbers = range(5)
    result = ['even' if x % 2 == 0 else 'odd' for x in numbers]
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
