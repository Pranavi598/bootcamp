import threading

counter = 0
lock = threading.Lock()


def increment():
    global counter
    with lock:
        counter += 1
        print(f"Counter value: {counter}")


def main():
    threads = []

    for _ in range(5):
        thread = threading.Thread(target=increment)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("Final counter value:", counter)


if __name__ == "__main__":
    main()
