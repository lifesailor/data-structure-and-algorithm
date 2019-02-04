import time
import random
from selection_sort.selection_sort import SelectionSort
from insertion_sort.insertion_sort import InsertionSort


class SortCompare:

    @classmethod
    def time(cls, alg, ary):
        start_time = time.time()

        if alg == "Selection":
            SelectionSort.sort(ary)
        elif alg == "Insertion":
            InsertionSort.sort(ary)
        end_time = time.time()
        return end_time - start_time

    @classmethod
    def time_random_input(cls, alg, N, T):
        total = 0.0
        ary = [None]*N

        for i in range(T):
            for j in range(N):
                ary[j] = random.uniform(0, 1)
            total += cls.time(alg, ary)
        return total


if __name__ == "__main__":
    alg1 = "Insertion"
    alg2 = "Selection"
    N = 1000
    T = 100

    t1 = SortCompare.time_random_input(alg1, N, T)
    t2 = SortCompare.time_random_input(alg2, N, T)

    print("For {} random doubles".format(N))
    print("{0} is {2} times faster than {1}".format(alg1, alg2, t2/t1))

