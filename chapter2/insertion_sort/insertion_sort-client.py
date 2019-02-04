"""
Sort 클라이언트
"""
import sys
import time
from insertion_sort import InsertionSort


class Client:
    def test(self, args):
        selection = InsertionSort(args)
        selection.sort()
        assert selection.is_sorted()
        selection.show()


if __name__ == "__main__":
    args = []
    for line in sys.stdin:
        arg = line.rstrip().split(" ")
        args.extend(arg)

    client = Client()

    start_time = time.time()
    client.test(args)
    end_time = time.time()
    print("\nTime:", end_time - start_time)
