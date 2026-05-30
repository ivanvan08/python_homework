class WeightedQuickUnionUF:
    def __init__(self, n: int):
        self._count: int = n
        self._id: list[int] = [i for i in range(n)]
        self._sz: list[int] = [1 for _ in range(n)]

    def count(self) -> int:
        return self._count

    def find(self, p: int) -> int:
        while p != self._id[p]:
            p = self._id[p]
        return p

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def union(self, p: int, q: int):
        i = self.find(p)
        j = self.find(q)

        if i == j:
            return

        if self._sz[i] < self._sz[j]:
            self._id[i] = j
            self._sz[j] += self._sz[i]
        else:
            self._id[j] = i
            self._sz[i] += self._sz[j]

        self._count -= 1
