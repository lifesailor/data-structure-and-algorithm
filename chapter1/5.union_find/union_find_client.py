"""
Bag Client
"""
import sys
import time
from union_find import QuickFindUF, QuickUnionUF, WeightedQuickUnionUF


class Client:
    def __init__(self):
        pass

    def test(self, N, args):

        # uf = QuickFindUF(N)
        # uf = QuickUnionUF(N)
        uf = WeightedQuickUnionUF(N)

        while args:
            item = args.pop(0)
            p = item[0]
            q = item[1]

            if uf.connected(p, q):
                continue
            uf.union(p, q)
            print(str(p) + " " + str(q))
        print(str(uf.get_count()) + " components")


if __name__ == "__main__":
    union_find_client = Client()

    # N = 10
    # tiny_args = [(0, 1), (0, 2), (0, 3), (0, 4)]
    # tiny_args = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (5, 0), (7, 2), (6, 1)]
    medium_args = []

    N = next(sys.stdin)

    for line in sys.stdin:
        args = line.rstrip().split(" ")
        for i, arg in enumerate(args):
            args[i] = int(args[i])
        medium_args.append(args)

    start_time = time.time()
    union_find_client.test(N=int(N), args=medium_args)
    end_time = time.time()
    print(end_time - start_time)