"""
Quick3 Sort는 분할 정복 기법을 이용한 정렬 방법이다.

Merge Sort API
1) void compare(Comparable v, Comparable w)
2) void exch(Comparable[] a, int i, int j)
3) boolean is_sorted(Comparable[] a) - 배열 항목이 정렬되어 있는지 검사
4) void show(Comparable[] a) - 배열 내용을 한 줄로 출력
5) void sort() - 정렬 함수 호출
6) void quick_sort() - 분할 및 정복
7) void partition() - 분할 지점
"""
import random


class Quick3Sort:
    aux = None

    @classmethod
    def compare(cls, v, w):
        if v < w:
            return -1
        elif v == w:
            return 0
        else:
            return 1

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
        cls.quick3_sort(ary, 0, len(ary) - 1)

    @classmethod
    def quick3_sort(cls, ary, lo=None, hi=None):
        if hi <= lo:
            return

        lt = lo
        i = lo + 1
        gt = hi

        v = ary[lo]

        while i <= gt:
            cmap = cls.compare(ary[i], v)

            if cmap < 0:
                cls.exch(ary, lt, i)
                lt = lt + 1
                i = i + 1
            elif cmap > 0:
                cls.exch(ary, i, gt)
                gt = gt - 1
            else:
                i += 1

        cls.quick3_sort(ary, lo, lt - 1)
        cls.quick3_sort(ary, gt + 1, hi)




