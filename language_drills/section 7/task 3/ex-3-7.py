def recursive_function(n, level=0):
    print(f"{' ' * level}Entering recursion level {level} with n={n}")
    if n == 0:
        return
    recursive_function(n-1, level + 1)
    print(f"{' ' * level}Exiting recursion level {level} with n={n}")

def main():
    recursive_function(3)

if __name__ == "__main__":
    main()
