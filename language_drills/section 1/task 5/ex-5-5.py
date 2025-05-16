def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

if __name__ == "__main__":
    doubler = make_multiplier(2)
    print("Doubler result for 5:", doubler(5))
