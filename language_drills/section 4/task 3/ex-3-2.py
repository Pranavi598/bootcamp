import functools

@functools.lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def main():
    # Calculate Fibonacci numbers using memoization
    print(fib(10))  # Should print 55
    print(fib(30))  # Should print 832040

if __name__ == "__main__":
    main()
