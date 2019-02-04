"""
Sort 클라이언트
"""
import sys
import time
from insertion_sort import InsertionSort


class Client:
    def test(self, args):
        InsertionSort.sort(args)
        assert InsertionSort.is_sorted(args)
        InsertionSort.show(args)


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
