"""
Selection Sort(선택 정렬)은 가장 작은 항목을 찾고 이와 뒤바꿈하는 정렬 알고리즘이다.

Selection Sort API

1) void less(Comparable v, Comparable w)
2) void exch(Comparable[] a, int i, int j)
3) boolean is_sorted(Comparable[] a) - 배열 항목이 정렬되어 있는지 검사
4) void show(Comparable[] a) - 배열 내용을 한 줄로 출력
"""


class SelectionSort:
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

        # repeat from 0 to len(ary) - 1
        for j in range(len(self.ary)):
            min_index = j

            # find min index
            for i in range(j, len(self.ary)):
                if self.ary[i] < self.ary[min_index]:
                    min_index = i

            self.exch(j, min_index)