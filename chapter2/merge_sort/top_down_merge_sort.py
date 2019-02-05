"""
Merge Sort는 분할 정복 기법을 이용한 정렬 방법이다. 이 코드는 top down 병합 정렬을 의미한다.

Merge Sort API
1) void less(Comparable v, Comparable w)
2) void exch(Comparable[] a, int i, int j)
3) boolean is_sorted(Comparable[] a) - 배열 항목이 정렬되어 있는지 검사
4) void show(Comparable[] a) - 배열 내용을 한 줄로 출력
5) void sort() - 정렬
6) void merge() - 병합
"""


class MergeSort:
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
            if cls.less(ary[i], ary[i-1]):
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
    def merge(cls, ary, lo, mid, hi):
        """
        ary[0..mid]와 ary[mid+1..hi]를 병합

        :param ary:
        :param lo:
        :param mid:
        :param hi:
        :return:
        """
        i = lo
        j = mid + 1

        # ary를 cls.aux에 복제
        for k in range(lo, hi+1):
            cls.aux[k] = ary[k]

        # inplace merge
        for k in range(lo, hi+1):
            if i > mid:
                ary[k] = cls.aux[j]
                j += 1
            elif j > hi:
                ary[k] = cls.aux[i]
                i += 1
            elif cls.less(cls.aux[j], cls.aux[i]):
                ary[k] = cls.aux[j]
                j += 1
            else:
                ary[k] = cls.aux[i]
                i += 1

    @classmethod
    def sort(cls, ary):
        cls.aux = [None] * len(ary)
        cls.merge_sort(ary, 0, len(ary)-1)

    @classmethod
    def merge_sort(cls, ary, lo=None, hi=None):
        if hi <= lo:
            return
        mid = lo + (hi - lo) // 2
        cls.merge_sort(ary, lo, mid)
        cls.merge_sort(ary, mid+1, hi)
        cls.merge(ary, lo, mid, hi)