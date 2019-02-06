"""
Merge Sort 클라이언트
"""
import sys
import time
# from top_down_merge_sort import HeapSort
from heap_sort import HeapSort


class Client:
    def test(self, args):
        HeapSort.sort(args)
        assert HeapSort.is_sorted(args)
        HeapSort.show(args)


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
