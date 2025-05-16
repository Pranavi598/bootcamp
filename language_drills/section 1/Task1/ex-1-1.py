from collections import deque

def list_operations(a):
    """
    Perform append, remove, and sort operations on the list using collections.deque.
    """
    # Convert list to deque to demonstrate usage of collections library
    a = deque(a)
    a.append(2)  # Append 2
    a.remove(3)  # Remove 3
    a = sorted(a)  # Sort the deque
    return a

if __name__ == "__main__":
    # 1. List Operations
    a = [5, 3, 8]
    updated_list = list_operations(a)
    print("Updated List after operations:", updated_list)
