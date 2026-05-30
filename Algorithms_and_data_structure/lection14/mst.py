import abc

import edge
import edge_weighted_graph


class MST(abc.ABC):
    def __init__(self, graph: edge_weighted_graph.EdgeWeightedGraph):
        self._graph = graph

    @abc.abstractmethod
    def weight(self) -> int:
        ...

    @abc.abstractmethod
    def edges(self) -> list[edge.Edge]:
        ...
