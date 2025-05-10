import functools
import time

# Uncached version of Fibonacci
def fib_uncached(n):
    if n <= 1:
        return n
    return fib_uncached(n - 1) + fib_uncached(n - 2)

@functools.lru_cache(maxsize=None)  # Memoized version of Fibonacci
def fib_cached(n):
    if n <= 1:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)

def main():
    # Test performance of uncached version
    start = time.time()
    print(fib_uncached(30))
    print(f"Uncached duration: {time.time() - start:.4f} seconds")

    # Test performance of cached version
    start = time.time()
    print(fib_cached(30))
    print(f"Cached duration: {time.time() - start:.4f} seconds")

if __name__ == "__main__":
    main()
