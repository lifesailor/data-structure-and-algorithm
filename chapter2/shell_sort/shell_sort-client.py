"""
Sort 클라이언트
"""
import sys
import time
from shell_sort import ShellSort


class Client:
    def test(self, args):
        ShellSort.sort(args)
        print(args)
        assert ShellSort.is_sorted(args)
        ShellSort.show(args)


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
