import concurrent.futures

def compute_square(x):
    return x * x

def main():
    # Use ThreadPoolExecutor to parallelize calls to a function
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(compute_square, [1, 2, 3, 4, 5])
        for result in results:
            print("Square:", result)

if __name__ == "__main__":
    main()
