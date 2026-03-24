from collections import deque
from typing import List


class Solution1:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345

        N = len(grid)
        M = len(grid[0])

        p = [[0 for _ in range(M)] for _ in range(N)]

        suffix = 1
        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                p[i][j] = suffix
                suffix = (suffix * grid[i][j]) % MOD

        prefix = 1
        for i in range(0, N):
            for j in range(0, M):
                p[i][j] = (prefix * p[i][j]) % MOD
                prefix = (prefix * grid[i][j]) % MOD

        return p

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2906. Construct Product Matrix - https://leetcode.com/problems/construct-product-matrix/description/?envType=daily-question&envId=2026-03-24

    testcase = [
        [
            [[1, 2], [3, 4]],
            [[24, 12], [8, 6]],
        ],
        [
            [[12345], [2], [1]],
            [[2], [0], [0]],
        ],
    ]

    for line in testcase:
        [grid, expected] = line
        s1 = Solution1()
        result = s1.constructProductMatrix(grid)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def canFinish(self, n, prerequisites):
        # using kahn's topological sort algo

        adj = [[] for _ in range(n)]  # adjacency list
        indegree = [0] * n  # indegree of nodes

        for prerequisite in prerequisites:
            v, u = prerequisite[0], prerequisite[1]
            adj[u].append(v)
            indegree[v] += 1

        order = []  # store sorted vertices
        q = deque()  # queue for storing nodes while traversal

        for u in range(n):
            if indegree[u] == 0:
                q.append(u)
                order.append(u)

        while q:
            u = q.popleft()

            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
                    order.append(v)

        return len(order) == n

        # Complexity analysis
        # Time : O(E) + O(V) + O(V + E)
        # Space : O(V + E) + O(V) + O(V) + O(E)


def p2():
    # Problem 2 : POTD Geeksforgeeks Course Schedule I - https://www.geeksforgeeks.org/problems/course-schedule-i/1

    testcase = [
        [
            4,
            [[2, 0], [2, 1], [3, 2]],
            True,
        ],
        [
            3,
            [[0, 1], [1, 2], [2, 0]],
            False,
        ],
    ]

    for line in testcase:
        [n, prerequisites, expected] = line
        s2 = Solution2()
        result = s2.canFinish(n, prerequisites)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 24 of March 2026

    p1()

    p2()
