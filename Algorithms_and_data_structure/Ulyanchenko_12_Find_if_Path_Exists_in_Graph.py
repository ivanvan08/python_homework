"""
06/04/2026
@author: Ulyanchenko Ivan
"""


class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        queue = [source]
        visited = {source}
        while queue:
            current = queue.pop(0)
            if current == destination:
                return True
            for i in adj[current]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        return False
