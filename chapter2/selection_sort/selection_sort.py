"""
Selection Sort(선택 정렬)은 가장 작은 항목을 찾고 이와 뒤바꿈하는 정렬 알고리즘이다.

Selection Sort API

1) void less(Comparable v, Comparable w)
2) void exch(Comparable[] a, int i, int j)
3) boolean is_sorted(Comparable[] a) - 배열 항목이 정렬되어 있는지 검사
4) void show(Comparable[] a) - 배열 내용을 한 줄로 출력
5) void sort() - 정렬
"""


class SelectionSort:
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
        # repeat from 0 to len(ary) - 1
        for i in range(len(ary)):
            min_index = i

            # find min index
            for j in range(i+1, len(ary)):
                if cls.less(ary[j], ary[min_index]):
                    min_index = j

            cls.exch(ary, i, min_index)