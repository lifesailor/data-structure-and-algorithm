"""
Union Find는 p, q간이 연결되어 있는지 확인하고 연결되지 않았으면 이를 연결하는 작업을 수행하는 알고리즘이다.

Union Find API
- UF() N개 사이트의 식별자를 정수(0 - N ~ 1) 값으로 초기화
- void union(int p, int q): p, q간의 연결 추가
- int find(int p): p(0 ~ N-1)가 속한 컴포넌트 식별자
- boolean connected(int p, int q): p와 q가 같은 컴포넌트에 속하면 true를 리턴
- int count(): 전체 컴포넌트 개수
"""


class QuickFindUF:
    def __init__(self, N):
        self.components = list(range(N))
        self.count = len(self.components)

    def union(self, p, q):
        if not self.connected(p, q):
            for i in range(len(self.components)):
                if self.components[i] == q:
                    self.components[i] = p
            self.count -= 1

    # quick find
    def find(self, p):
        return self.components[p]

    def connected(self, p, q):
        if self.find(p) == self.find(q):
            return True
        else:
            return False

    def get_count(self):
        return self.count


class QuickUnionUF:
    def __init__(self, N):
        self.components = list(range(N))
        self.count = len(self.components)

    # quick union
    def union(self, p, q):
        parent_p = self.find(p)
        parent_q = self.find(q)

        # connected
        if parent_p == parent_q:
            return
        else:
            self.components[parent_q] = self.components[parent_p]
            self.count -= 1

    def find(self, p):
        while p != self.components[p]:
            p = self.components[p]
        return p

    def connected(self, p, q):
        if self.find(p) == self.find(q):
            return True
        else:
            return False

    def get_count(self):
        return self.count


class WeightedQuickUnionUF:
    def __init__(self, N):
        self.components = list(range(N))
        self.sizes = [1] * N
        self.count = len(self.components)

    # quick union
    def union(self, p, q):
        parent_p = self.find(p)
        parent_q = self.find(q)

        if parent_p == parent_q:
            return
        else:
            # 작은 트리가 큰 트리에 연결하도록 함
            if self.sizes[parent_p] < self.sizes[parent_q]:
                self.components[parent_p] = self.components[parent_q]
                self.sizes[parent_q] += self.sizes[parent_p]
            else:
                self.components[parent_q] = self.components[parent_p]
                self.sizes[parent_p] += self.sizes[parent_q]
            self.count -= 1

    def find(self, p):
        while p != self.components[p]:
            p = self.components[p]
        return p

    def connected(self, p, q):
        if self.find(p) == self.find(q):
            return True
        else:
            return False

    def get_count(self):
        return self.count
