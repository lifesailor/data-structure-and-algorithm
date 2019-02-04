"""
Shell Sort(Shell 정렬)은 가장 작은 항목을 찾고 이와

Selection Sort API

1) void less(Comparable v, Comparable w)
2) void exch(Comparable[] a, int i, int j)
3) boolean is_sorted(Comparable[] a) - 배열 항목이 정렬되어 있는지 검사
4) void show(Comparable[] a) - 배열 내용을 한 줄로 출력
5) void sort() - 정렬
"""


class ShellSort:
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
        N = len(ary) # 11
        h = 1

        while h < N // 3:
            h = 3 * h + 1  # 1 4 13 40
        while h >= 1:
            for i in range(h, N):  # 40 - 121
                for j in range(i, h-1, -h):
                    if cls.less(ary[j], ary[j - h]):
                        cls.exch(ary, j, j-h)
                    else:
                        break
            h = h // 3