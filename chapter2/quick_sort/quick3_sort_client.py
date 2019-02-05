"""
Quick Sort 클라이언트
"""
import sys
import time
from quick3_sort import Quick3Sort


class Client:
    def test(self, args):
        Quick3Sort.sort(args)
        assert Quick3Sort.is_sorted(args)
        Quick3Sort.show(args)


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
