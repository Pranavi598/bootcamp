def compare_generator_vs_list():
    gen = (x * 2 for x in range(5))
    lst = [x * 2 for x in range(5)]
    print("Generator output:", list(gen))
    print("List comprehension output:", lst)

if __name__ == "__main__":
    compare_generator_vs_list()
