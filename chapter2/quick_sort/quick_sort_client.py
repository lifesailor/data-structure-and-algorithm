"""
Quick Sort 클라이언트
"""
import sys
import time
from quick_sort import QuickSort


class Client:
    def test(self, args):
        QuickSort.sort(args)
        assert QuickSort.is_sorted(args)
        QuickSort.show(args)


if __name__ == "__main__":

    # client
    client = Client()

    # input
    args = []
    for line in sys.stdin:
        arg = line.rstrip().split(" ")
        args.extend(arg)

    # test
    start_time = time.time()
    client.test(args)
    end_time = time.time()
    print("\nTime:", end_time - start_time)
