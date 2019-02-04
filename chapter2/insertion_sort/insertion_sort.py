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
    def __init__(self, args):
        self.ary = args

    def less(self, v, w):
        return v < w

    def exch(self, i, j):
        temp = self.ary[i]
        self.ary[i] = self.ary[j]
        self.ary[j] = temp

    def is_sorted(self):
        for i in range(1, len(self.ary)):
            if self.less(self.ary[i], self.ary[i-1]):
                return False
            return True

    def show(self):
        for i in range(len(self.ary)):
            print(self.ary[i], end=' ')

    def sort(self):
        for i in range(1, len(self.ary)):
            for j in range(i, 0, -1):
                if self.less(self.ary[j], self.ary[j-1]):
                    self.exch(j, j-1)