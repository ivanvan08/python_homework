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


if __name__ == "__main__":
    sol = Solution()

    print(sol.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))  # True
    print(sol.validPath(1, [], 0, 0))  # True
    print(sol.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))  # False
    print(sol.validPath(5, [[0, 1], [1, 2]], 3, 3))  # True
    print(sol.validPath(5, [[0, 1], [1, 2], [2, 3], [3, 4]], 0, 4))  # True
    print(sol.validPath(3, [], 0, 2))  # False
