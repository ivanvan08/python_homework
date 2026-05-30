class Edge:
    def __init__(self, v: int, w: int, weight: float):
        self._v: int = v
        self._w: int = w
        self._weight: float = weight

    def either(self) -> int:
        return self._v

    def weight(self) -> float:
        return self._weight

    def other(self, vertex: int) -> int:
        if vertex == self._v:
            return self._w
        return self._v

    def __repr__(self):
        return f"{self._v}-{self._w} {self._weight:.2f}"

    def __lt__(self, other: "Edge") -> bool:
        return self._weight < other.weight()
