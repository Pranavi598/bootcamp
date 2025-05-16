class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

def use_custom_iterator():
    for number in Counter(3):
        print("Counter value:", number)

if __name__ == "__main__":
    use_custom_iterator()
