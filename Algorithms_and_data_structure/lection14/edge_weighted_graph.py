import edge


class EdgeWeightedGraph:
    def __init__(self, vertices: int):
        self._vertices: int = vertices
        self._edges: int = 0
        self._adj: dict[int, list[edge.Edge]] = {
            v: [] for v in range(self._vertices)
        }

    def v(self) -> int:
        return self._vertices

    def e(self) -> int:
        return self._edges

    def add_edge(self, e: edge.Edge):
        v = e.either()
        w = e.other(v)
        self._adj[v].append(e)
        self._adj[w].append(e)
        self._edges += 1

    def adj(self, v: int) -> list[edge.Edge]:
        return self._adj[v]

    def edges(self) -> list[edge.Edge]:
        res = []

        for v in range(self._vertices):
            loops = 0

            for e in self.adj(v):
                if e.other(v) > v:
                    res.append(e)

                elif e.other(v) == v:
                    if loops % 2 == 0:
                        res.append(e)

                    loops += 1

        return res

    def __repr__(self) -> str:
        return "\n".join(map(repr, self.edges()))
