# 1. Use timeit to measure execution time of sum(range(10000))
import timeit
def main_timeit():
    print("Time taken by sum(range(10000)):", timeit.timeit("sum(range(10000))", number=100))
if __name__ == "__main__":
    main_timeit()