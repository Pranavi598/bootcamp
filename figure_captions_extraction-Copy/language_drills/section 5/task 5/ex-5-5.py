import multiprocessing
import time

def compute():
    print("Process started.")
    time.sleep(2)
    print("Process finished.")

def main():
    # Start a process to compute something in parallel
    process = multiprocessing.Process(target=compute)
    process.start()
    process.join()
    print("Main program finished.")

if __name__ == "__main__":
    main()
