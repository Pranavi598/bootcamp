def generator_expression():
    """
    Use a generator expression to square numbers from 0 to 4 and print them.
    """
    gen = (n * n for n in range(5))
    return list(gen)

if __name__ == "__main__":
    # 5. Generator Expression
    result = generator_expression()
    print("Generator Expression Result:", result)

