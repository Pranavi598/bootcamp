# Save this as memory_profile_example.py
# Run using: mprof run memory_profile_example.py && mprof plot

from memory_profiler import profile

@profile
def allocate_memory():
    a = [i for i in range(1000000)]
    return sum(a)

def main():
    print("Result:", allocate_memory())

if __name__ == "__main__":
    main()
