"""
후입선출 스택은 마지막으로 들어간 것이 가장 먼저 나오는 정책을 가지는 컬렉션이다.

FixedCapacityStack API

- FixedCapacityStackOfStrings(int cap) cap을 용량으로 하는 빈 스택 생성
- void push(Item): 항목 추가
- Item pop(): 가장 최근에 추가된 항목 제거
- boolean is_empty(): 스택이 비었는가?
- int size(): 스택에 든 항목 개수
"""

class FixedCapacityStack:
    def __init__(self, cap):
        """
        item_ary: fixed size array
        n: number of elements in array

        :param cap:
        """
        self.item_ary = [None] * cap
        self.n = 0

    def is_empty(self):
        if self.n == 0:
            return True
        else:
            return False

    def size(self):
        return self.n

    def push(self, item):
        assert self.n <= len(self.item_ary) - 1  # item_ary 가 꽉 차있으면 에러 출력

        self.item_ary[self.n] = item
        self.n += 1

    def pop(self):
        assert self.n > 0  # 비어 있으면 에러 출력

        self.n -= 1
        ele = self.item_ary[self.n]
        self.item_ary[self.n] = None
        return ele

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= self.n:
            raise StopIteration

        n = self.item_ary[self.index]
        self.index += 1
        return n

