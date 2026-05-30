import queue

import edge
import edge_weighted_graph
import mst


class LazyPrimMST(mst.MST):
    def __init__(self, graph: edge_weighted_graph.EdgeWeightedGraph):
        super().__init__(graph)

        self._pq = queue.PriorityQueue()
        self._mst = queue.Queue()
        self._marked: list[bool] = [False for _ in range(self._graph.v())]

        self._weight = 0

        self._visit(0)

        while not self._pq.empty() and self._mst.qsize() < self._graph.v() - 1:
            e = self._pq.get()
            v = e.either()
            w = e.other(v)

            if self._marked[v] and self._marked[w]:
                continue

            self._weight += e.weight()
            self._mst.put(e)

            if not self._marked[v]:
                self._visit(v)

            if not self._marked[w]:
                self._visit(w)

        self._edges = list(self._mst.queue)

    def _visit(self, v: int):
        self._marked[v] = True

        for e in self._graph.adj(v):
            if not self._marked[e.other(v)]:
                self._pq.put(e)

    def weight(self) -> int:
        return self._weight

    def edges(self) -> list[edge.Edge]:
        return self._edges


if __name__ == "__main__":
    g = edge_weighted_graph.EdgeWeightedGraph(8)

    g.add_edge(edge.Edge(0, 7, 0.16))
    g.add_edge(edge.Edge(3, 7, 0.19))
    g.add_edge(edge.Edge(2, 3, 0.17))
    # g.add_edge(edge.Edge(1, 7, 0.19))
    g.add_edge(edge.Edge(0, 2, 0.26))
    g.add_edge(edge.Edge(5, 7, 0.28))
    g.add_edge(edge.Edge(1, 3, 0.29))
    g.add_edge(edge.Edge(1, 5, 0.32))
    g.add_edge(edge.Edge(2, 7, 0.34))
    g.add_edge(edge.Edge(4, 5, 0.35))
    g.add_edge(edge.Edge(1, 2, 0.36))
    g.add_edge(edge.Edge(4, 7, 0.37))
    g.add_edge(edge.Edge(0, 4, 0.38))
    g.add_edge(edge.Edge(6, 2, 0.40))
    g.add_edge(edge.Edge(3, 6, 0.52))
    g.add_edge(edge.Edge(6, 0, 0.58))
    g.add_edge(edge.Edge(6, 4, 0.93))

    prim_mst = LazyPrimMST(g)

    print("\n".join(map(repr, prim_mst.edges())))
    print(f"{prim_mst.weight()}")
