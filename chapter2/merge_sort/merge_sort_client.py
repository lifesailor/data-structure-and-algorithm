"""
Merge Sort 클라이언트
"""
import sys
import time
# from top_down_merge_sort import MergeSort
from bottom_up_merge_sort import MergeSort


class Client:
    def test(self, args):
        MergeSort.sort(args)
        assert MergeSort.is_sorted(args)
        MergeSort.show(args)


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
