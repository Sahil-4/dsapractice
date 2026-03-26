import heapq
from typing import List


class Solution1:
    def __init__(self):
        self.total = 0

    def checkHorCuts(self, grid):
        m = len(grid)
        n = len(grid[0])

        st = set()
        top = 0

        for i in range(m - 1):  # equivalent to i <= m-2

            for j in range(n):
                st.add(grid[i][j])
                top += grid[i][j]

            bottom = self.total - top
            diff = top - bottom

            if diff == 0:
                return True

            if diff == grid[0][0]:
                return True
            if diff == grid[0][n - 1]:
                return True
            if diff == grid[i][0]:
                return True

            if i > 0 and n > 1 and diff in st:
                return True

        return False

    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # compute total sum
        self.total = sum(sum(row) for row in grid)

        # horizontal cuts
        if self.checkHorCuts(grid):
            return True

        grid.reverse()

        # reversed
        if self.checkHorCuts(grid):
            return True

        grid.reverse()  # restore original grid

        # transpose grid (n x m)
        transposeGrid = [[grid[i][j] for i in range(m)] for j in range(n)]

        if self.checkHorCuts(transposeGrid):
            return True

        transposeGrid.reverse()

        if self.checkHorCuts(transposeGrid):
            return True

        return False

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(N * N)


def p1():
    # Problem 1 : POTD Leetcode 3548. Equal Sum Grid Partition II - https://leetcode.com/problems/equal-sum-grid-partition-ii/description/?envType=daily-question&envId=2026-03-26

    testcase = [
        [
            [[1, 4], [2, 3]],
            True,
        ],
        [
            [[1, 2], [3, 4]],
            True,
        ],
        [
            [[1, 2, 4], [2, 3, 5]],
            False,
        ],
        [
            [[4, 1, 8], [3, 2, 6]],
            False,
        ],
    ]

    for line in testcase:
        [grid, expected] = line
        s1 = Solution1()
        result = s1.canPartitionGrid(grid)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:

    def countPaths(self, V, edges):
        MOD = 10**9 + 7

        # adjacency list
        adj = [[] for _ in range(V)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))

        # distance and ways arrays
        dist = [float("inf")] * V
        ways = [0] * V

        dist[0] = 0
        ways[0] = 1

        # min heap (time, node)
        pq = [(0, 0)]

        while pq:
            curr_time, node = heapq.heappop(pq)

            # skip outdated entries
            if curr_time > dist[node]:
                continue

            for nei, t in adj[node]:
                new_time = curr_time + t

                # found shorter path
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    ways[nei] = ways[node]
                    heapq.heappush(pq, (new_time, nei))

                # found another shortest path
                elif new_time == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD

        return ways[V - 1]

        # Complexity analysis
        # Time : O(V + E * log E)
        # Space : O(V + E)


def p2():
    # Problem 2 : POTD Geeksforgeeks Number of Ways to Arrive at Destination - https://www.geeksforgeeks.org/problems/number-of-ways-to-arrive-at-destination/1

    testcase = [
        [
            4,
            [
                [0, 1, 2],
                [1, 2, 3],
                [0, 3, 5],
                [1, 3, 3],
                [2, 3, 4],
            ],
            2,
        ],
        [
            6,
            [
                [0, 2, 3],
                [0, 4, 2],
                [0, 5, 7],
                [2, 3, 1],
                [2, 5, 5],
                [5, 3, 3],
                [5, 1, 4],
                [1, 4, 1],
                [4, 5, 5],
            ],
            4,
        ],
    ]

    for line in testcase:
        [V, edges, expected] = line
        s2 = Solution2()
        result = s2.countPaths(V, edges)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 26 of March 2026

    p1()

    p2()
