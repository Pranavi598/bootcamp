def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

if __name__ == "__main__":
    triple = make_multiplier(3)
    result = triple(10)
    print("Triple of 10 is:", result)
