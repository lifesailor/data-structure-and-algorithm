"""
Sort 클라이언트
"""
import sys
import time
from selection_sort import SelectionSort


class Client:
    def test(self, args):
        SelectionSort.sort(args)
        assert SelectionSort.is_sorted(args)
        SelectionSort.show(args)


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
