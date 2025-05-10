import time

def compute():
    return sum(i * i for i in range(100000))

def main():
    start = time.time()
    result = compute()
    end = time.time()
    print(f"Result: {result}")
    print(f"Execution time: {end - start:.6f} seconds")

if __name__ == "__main__":
    main()
