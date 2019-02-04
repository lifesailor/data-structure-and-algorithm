"""
Insertion Sort(삽입 정렬)은 항목을 삽입할 공간을 만들기 위해 삽입할 항목보다 큰 항목을 오른쪽으로 밀어서 이동한다.
그리고 확보된 빈 공간에 항목을 삽입한다.

1) void less(Comparable v, Comparable w)
2) void exch(Comparable[] a, int i, int j)
3) boolean is_sorted(Comparable[] a) - 배열 항목이 정렬되어 있는지 검사
4) void show(Comparable[] a) - 배열 내용을 한 줄로 출력
5) void sort() - 정렬
"""


class InsertionSort:
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
        for i in range(1, len(ary)):
            for j in range(i, 0, -1):
                if cls.less(ary[j], ary[j-1]):
                    cls.exch(ary, j, j-1)
                else:
                    break
