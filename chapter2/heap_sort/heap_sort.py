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


class HeapSort:
    @classmethod
    def less(cls, ary, i, j):
        return ary[i] < ary[j]

    @classmethod
    def exch(cls, ary, i, j):
        temp = ary[i]
        ary[i] = ary[j]
        ary[j] = temp

    @classmethod
    def is_sorted(cls, ary):
        for i in range(1, len(ary)):
            if cls.less(ary, i+1, i):
                return False
            return True

    @classmethod
    def show(cls, ary):
        for i in range(1, len(ary)):
            print(ary[i], end=' ')

    @classmethod
    def sort(cls, ary):
        N = len(ary)
        ary.insert(0, None)

        for k in range(N//2, 0, -1):
            cls.sink(ary, k, N)

        while N > 1:
            cls.exch(ary, 1, N)
            N = N - 1
            cls.sink(ary, 1, N)

    @classmethod
    def sink(cls, ary, k, N):
        while 2 * k <= N:
            j = 2 * k
            if j < N and cls.less(ary, j, j+1):
                j += 1
            if not cls.less(ary, k, j):
                break
            cls.exch(ary, k, j)
            k = j

