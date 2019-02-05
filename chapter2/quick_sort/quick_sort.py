"""
Quick Sort는 분할 정복 기법을 이용한 정렬 방법이다.

Merge Sort API
1) void less(Comparable v, Comparable w)
2) void exch(Comparable[] a, int i, int j)
3) boolean is_sorted(Comparable[] a) - 배열 항목이 정렬되어 있는지 검사
4) void show(Comparable[] a) - 배열 내용을 한 줄로 출력
5) void sort() - 정렬 함수 호출
6) void quick_sort() - 분할 및 정복
7) void partition() - 분할 지점
"""
import random


class QuickSort:
    aux = None

    @classmethod
    def less(cls, v, w):
        return v < w

    @classmethod
    def exch(cls, ary, i, j):
        temp = ary[i]
        ary[i] = ary[j]
        ary[j] = temp

    @classmethod
    def is_sorted(cls, ary):
        for i in range(1, len(ary)):
            if cls.less(ary[i], ary[i - 1]):
                return False
            return True

    @classmethod
    def show(cls, ary):
        for i in range(len(ary)):
            print(ary[i], end=' ')

    @classmethod
    def sort(cls, ary):
        pass

    @classmethod
    def sort(cls, ary):
        random.shuffle(ary)
        cls.quick_sort(ary, 0, len(ary) - 1)

    @classmethod
    def quick_sort(cls, ary, lo=None, hi=None):
        if hi <= lo:
            return

        j = cls.partition(ary, lo, hi)
        cls.quick_sort(ary, lo, j - 1)
        cls.quick_sort(ary, j + 1, hi)

    @classmethod
    def partition(cls, ary, lo, hi):
        i = lo
        j = hi + 1
        v = ary[lo]

        i += 1
        j -= 1

        while True:

            # from left
            while cls.less(ary[i], v):
                if i == hi:
                    break
                i += 1

            # from right
            while cls.less(v, ary[j]):
                if j == lo:
                    break
                j -= 1

            # index intersect
            if i >= j:
                break

            # exchange
            cls.exch(ary, i, j)

        # exchange v into j
        cls.exch(ary, lo, j)
        return j
