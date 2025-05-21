def countdown(n):
    while n > 0:
        yield n
        n -= 1

def run_countdown():
    for number in countdown(3):
        print("Countdown:", number)

if __name__ == "__main__":
    run_countdown()
