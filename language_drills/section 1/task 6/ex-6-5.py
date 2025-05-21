def running_totals(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total

def use_running_totals():
    for value in running_totals([1, 2, 3, 4]):
        print("Running total:", value)

if __name__ == "__main__":
    use_running_totals()
