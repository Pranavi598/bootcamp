from collections import deque


def main():
    # Create a deque and simulate a stack (LIFO)
    stack = deque()
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print(f"Stack: {stack}")
    print(f"Popped from stack: {stack.pop()}")
    print(f"Stack after pop: {stack}")

    # Create a deque and simulate a queue (FIFO)
    queue = deque()
    queue.append(1)
    queue.append(2)
    queue.append(3)
    print(f"Queue: {queue}")
    print(f"Dequeued from queue: {queue.popleft()}")
    print(f"Queue after dequeue: {queue}")


if __name__ == "__main__":
    main()
