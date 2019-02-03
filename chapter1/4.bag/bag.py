"""
백은 항목을 삭제할 수 없는 컬렉션이다. 백의 목적은 항목을 수집하고 수집된 항목들을 순회할 수 있는 도구를 제공하는 것이다.

Bag API
- Bag(): 공백 백 생성
- add(Item item): 항목 추가
- is_empty(): 백이 비어 있는가.
- int size(): 백에 든 항목 개수

"""


class Node:
    def __init__(self):
        self.node = None
        self.item = None


class Bag:
    def __init__(self):
        self.first = None
        self.n = 0

    def add(self, item):
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

    def is_empty(self):
        if self.n == 0:
            return True
        else:
            return False

    def size(self):
        return self.n

    def __iter__(self):
        self.index = 0
        self.current = self.first
        return self

    def __next__(self):
        if self.index >= self.n:
            raise StopIteration

        item = self.current.item
        self.current = self.current.node
        self.index += 1
        return item


