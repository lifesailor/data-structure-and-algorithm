"""
후입선출 스택은 마지막으로 들어간 것이 가장 먼저 나오는 정책을 가지는 컬렉션이다.

ResizeStackArray API

- ResizeStackArray(): 빈 스택 생성
- void push(Item): 항목 추가
- Item pop(): 가장 최근에 추가된 항목 제거
- boolean is_empty(): 스택이 비었는가?
- int size(): 스택에 든 항목 개수
- void resize(): 스택 크기 변경
"""


class ResizeStackArray:
    def __init__(self):
        self.item_ary = []
        self.n = 0

    def is_empty(self):
        if self.n == 0:
            return True
        else:
            return False

    def size(self):
        return self.n

    def push(self, item):
        if self.n == len(self.item_ary):
            self.resize(self.n * 2 + 1)
        self.item_ary[self.n] = item
        self.n += 1

    def resize(self, max):
        item_ary = [None] * max
        for i in range(self.n):
            item_ary[i] = self.item_ary[i]
        self.item_ary = item_ary

    def pop(self):
        assert self.n > 0
        self.n -= 1

        ele = self.item_ary[self.n]
        self.item_ary[self.n] = None

        if self.n == len(self.item_ary) // 4:
            self.resize(len(self.item_ary) // 2)
        return ele








