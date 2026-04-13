"""
13/04/2026
@author: Ulyanchenko Ivan
"""
from lection13 import digraph, graph, dfs


def reverse(g):
    new_graph = digraph.DiGraph()
    for v in range(g.vertex_count()):
        for w in g.adj(v):
            new_graph.add_edge(w, v)
    return new_graph


def _dfs_recursive(g, v, marked, postorder):
    marked[v] = True
    for w in g.adj(v):
        if marked[w] is False:
            _dfs_recursive(g, w, marked, postorder)
    postorder.append(v)


def dfs_postorder(g):
    marked = [False for i in range(g.vertex_count())]
    postorder = []
    for i in range(len(marked)):
        if marked[i] is False:
            _dfs_recursive(g, i, marked, postorder)
    return postorder


def kosaradge(g):
    # fase 1
    reversed_graph = reverse(g)
    postorder = dfs_postorder(reversed_graph)
    # fase 2
    result = []
    marked = [False for i in range(g.vertex_count())]
    for v in reversed(postorder):
        if marked[v] is False:
            normal_dfs = dfs.DFS(g, v)
            scc = []
            for w in range(g.vertex_count()):
                if normal_dfs.has_path_to(w):
                    scc.append(w)
                    marked[w] = True
            result.append(scc)
    return result
