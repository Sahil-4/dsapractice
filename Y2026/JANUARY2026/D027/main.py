import heapq
from typing import List


class Solution1:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # use dijkstra

        INF = 10**9
        dist = [INF] * n
        dist[0] = 0

        # adjacency list: adj[u] = [(v, weight), ...]
        adj = [[] for _ in range(n)]
        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, 2 * wt))

        pq = [(0, 0)]  # (distance, node)

        while pq:
            d, node = heapq.heappop(pq)

            if d > dist[node]:
                continue

            for ne, wt in adj[node]:
                if dist[ne] > dist[node] + wt:
                    dist[ne] = dist[node] + wt
                    heapq.heappush(pq, (dist[ne], ne))

        return -1 if dist[n - 1] == INF else dist[n - 1]

        # Complexity analysis
        # Time : O((N+M) * Log(N))
        # Space : O(N+M)


def p1():
    # Problem 1 : POTD Leetcode 3650. Minimum Cost Path with Edge Reversals - https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/description/?envType=daily-question&envId=2026-01-27

    testcase = [
        [4, [[0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]], 5],
        [4, [[0, 2, 1], [2, 1, 1], [1, 3, 1], [2, 3, 3]], 3],
    ]

    for line in testcase:
        [n, edges, expected] = line
        s1 = Solution1()
        result = s1.minCost(n, edges)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def isWordExist(self, mat, word):
        # Code here
        # use dfs traversal
        # we will use index wi to track point where we are in word
        # and indices ri, ci to track where we are in mat
        # at any point if wi >= len(word)-1 we return mat[ri][ci] == word[wi]
        # we check all four direction and
        # we proceed in direction where word character and cell character matches

        dirs = [
            [-1, 0],  # top
            [0, +1],  # right
            [+1, 0],  # bottom
            [0, -1],  # left
        ]

        N = len(mat)
        M = len(mat[0])
        word_len = len(word)

        def is_valid_cell(nri, nci):
            return (nri >= 0 and nri < N) and (nci >= 0 and nci < M)

        def dfs(wi, ri, ci, visited):
            if wi == word_len - 1:
                return True

            visited.add((ri, ci))

            _check = False

            for _dir in dirs:
                nri = ri + _dir[0]
                nci = ci + _dir[1]
                nwi = wi + 1

                if (
                    is_valid_cell(nri, nci)
                    and mat[nri][nci] == word[nwi]
                    and (nri, nci) not in visited
                ):
                    _check = _check or dfs(nwi, nri, nci, visited)

            visited.remove((ri, ci))

            return _check

        check = False

        for ri in range(N):
            for ci in range(M):
                if mat[ri][ci] == word[0]:
                    visited = set()
                    check = check or dfs(0, ri, ci, visited)

        return check

        # Complexity analysis
        # Time : O((N * M) * (word_len))
        # Space : O(2 * word_len)


def p2():
    # Problem 2 : POTD Geeksforgeeks Word Search - https://www.geeksforgeeks.org/problems/word-search/1

    testcase = [
        [[["T", "E", "E"], ["S", "G", "K"], ["T", "E", "L"]], "GEEK", True],
        [[["T", "E", "U"], ["S", "G", "K"], ["T", "E", "L"]], "GEEK", False],
        [[["A", "B", "A"], ["B", "A", "B"]], "AB", True],
    ]

    for line in testcase:
        [mat, word, expected] = line
        s2 = Solution2()
        result = s2.isWordExist(mat, word)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 27 of January 2026

    p1()

    p2()
