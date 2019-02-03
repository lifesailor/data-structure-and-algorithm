"""
선입선출 Queue는 먼저 들어간 것이 먼저 나오는 것을 정책으로 하는 컬렉션이다.

Queue API

- Queue(): 비어 있는 큐 생성
- void enqueue(Item item): 항목 추가
- void dequeue(): 최근에 추가된 항목 제거
- boolean is_empty(): 큐가 비었는가?
- int size(): 큐에 든 항목 개수
"""


class Node:
    def __init__(self):
        self.node = None
        self.item = None


class Queue:
    def __init__(self):
        self.first = None
        self.n = 0

    def enqueue(self, item):
        next = self.first

        if next is None:
            next = Node()
            next.item = item
            self.first = next
            self.n += 1
            return

        while next.node is not None:
            next = next.node
        next.node = Node()
        next.node.item = item
        self.n += 1

    def dequeue(self):
        assert self.n > 0

        first = self.first
        self.first = first.node
        self.n -= 1
        return first.item

    def is_empty(self):
        if self.n == 0:
            return True
        else:
            return False

    def size(self):
        return self.n
