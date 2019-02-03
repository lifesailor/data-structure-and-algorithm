"""
Stack API

- void push(Item): 항목 추가
- Item pop(): 가장 최근에 추가된 항목 제거
- boolean is_empty(): 스택이 비었는가?
- int size(): 스택에 든 항목 개수
"""


class Node:
    def __init__(self):
        self.node = None
        self.item = None


class Stack:
    def __init__(self):
        self.first = None  # 첫 노드
        self.n = 0  # 항목 개수

    def push(self, item):
        first_node = self.first
        self.first = Node()
        self.first.item = item
        self.first.node = first_node
        self.n += 1

    def pop(self):
        assert self.n > 0

        first = self.first
        item = first.item
        self.first = first.node
        self.n -= 1
        return item

    def is_empty(self):
        if self.first is None:
            return True
        else:
            return False

    def size(self):
        return self.n