import threading
import time

def my_function():
    print("Thread started.")
    time.sleep(2)
    print("Thread finished.")

def main():
    # Start a thread to run a function concurrently
    thread = threading.Thread(target=my_function)
    thread.start()
    thread.join()
    print("Main program finished.")

if __name__ == "__main__":
    main()
