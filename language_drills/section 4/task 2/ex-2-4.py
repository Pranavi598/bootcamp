def memoize(func):
    """Memoization decorator to cache function results"""
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def expensive_computation(x):
    print("Calculating...")
    return x * x

def main():
    print(expensive_computation(5))
    print(expensive_computation(5))  # Should return cached result

if __name__ == "__main__":
    main()
