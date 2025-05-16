import timeit

def main():
    list_time = timeit.timeit('[x*x for x in range(1000000)]', number=1)
    gen_time = timeit.timeit('(x*x for x in range(1000000))', number=1)
    print(f"List comprehension time: {list_time:.6f} sec")
    print(f"Generator expression time: {gen_time:.6f} sec")

if __name__ == "__main__":
    main()
