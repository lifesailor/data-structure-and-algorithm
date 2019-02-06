"""
Priority Queue는 가장 높은 우선순위

Priority Queue API
- MaxPQ(): 우선순위 큐 생성
- MaxPQ(int max): 최대 크기를 지정해서 우선순위 큐 생성
- MaxPQ(Key[] a); a[]의 키를 이용해 우선순위 큐 생성
- void insert(Key v): 우선순위 큐에 키 추가
- Key max(): 가장 큰 키 리턴
- Key delMax(): 가장 큰 키를 리턴하고 삭제
- boolean is_empty(): 우선순위 큐가 비어있는가.
- int size(): 우선순위 큐에 저장된 키의 개수
"""


class MaxPQ:
    def __init__(self, max):
        self.pq = [None] * (max + 1)
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def insert(self, v):
        self.n += 1
        self.pq[self.n] = v
        self.swim(self.n)

    def del_max(self):
        max = self.pq[1]
        self.exch(1, self.n)
        self.n -= 1

        self.pq[self.n + 1] = None
        self.sink(1)
        return max

    def less(self, i , j):
        return self.pq[i] < self.qp[j]

    def exch(self, i, j):
        temp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = temp

    def swim(self, k):
        while k > 1 and self.less(k//2, k):
            self.exch(k//2, k)
            k = k // 2

    def sink(self, ary, k):
        while 2 * k <= self.n:
            j = 2 * k
            if j < self.n and self.less(j, j+1):
                j += 1
            if not self.less(k, j):
                break
            self.exch(k, j)
            k = j