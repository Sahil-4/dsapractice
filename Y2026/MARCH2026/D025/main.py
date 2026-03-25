from collections import deque
from typing import List


class Solution1:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # create a grid for sum
        # sum_grid[i][j] will contain some of elements from grid[0][0] to grid[i][j]
        # sum up from left to right
        # now we make partition on index i (for row)
        # and check if sum_grid[N-1][M-1] == sum_grid[i-1][M-1] * 2
        # for column wise partition
        # we have to sum up from top to bottom
        # and have to check if sum_grid[N-1][M-1] == sum_grid[N-1][j-1] * 2
        # we are making partition on j
        # now creating sum grid is unnecessary
        # and we can use row-wise and column-wise cumulative sums instead

        m, n = len(grid), len(grid[0])

        total = sum(sum(row) for row in grid)
        if total & 1:
            return False

        target = total // 2

        # check horizontal cuts
        curr_sum = 0
        for i in range(m - 1):
            curr_sum += sum(grid[i])
            if curr_sum == target:
                return True

        # compute column sums
        col_sums = [0] * n
        for row in grid:
            for j in range(n):
                col_sums[j] += row[j]

        # check vertical cuts
        curr_sum = 0
        for j in range(n - 1):
            curr_sum += col_sums[j]
            if curr_sum == target:
                return True

        return False

        # Complexity analysis
        # Time : O(M * N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3546. Equal Sum Grid Partition I - https://leetcode.com/problems/equal-sum-grid-partition-i/description/?envType=daily-question&envId=2026-03-25

    testcase = [
        [[[1, 4], [2, 3]], True],
        [[[1, 3], [2, 4]], False],
    ]

    for line in testcase:
        [grid, expected] = line
        s1 = Solution1()
        result = s1.canPartitionGrid(grid)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minHeightRoot(self, V, edges):
        # Code here

        # base case
        if V < 2:
            centroids = []
            for i in range(V):
                centroids.append(i)
            return centroids

        # build adjacency list
        adj = [[] for _ in range(V)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        # degree of each node
        deg = [len(adj[i]) for i in range(V)]

        # initialize the first layer of leaves
        leaves = deque()
        for i in range(V):
            if deg[i] == 1:
                leaves.append(i)

        remNodes = V

        # trim the leaves level by level until reaching the centroids
        while remNodes > 2:
            leafCount = len(leaves)
            remNodes -= leafCount

            for _ in range(leafCount):
                leaf = leaves.popleft()

                for neighbor in adj[leaf]:
                    deg[neighbor] -= 1
                    if deg[neighbor] == 1:
                        leaves.append(neighbor)

                deg[leaf] = 0  # mark as removed

        # remaining nodes are the centroids
        result = []
        while leaves:
            result.append(leaves.popleft())

        return result

        # Complexity analysis
        # Time : O(V)
        # Space : O(V)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum height roots - https://www.geeksforgeeks.org/problems/minimum-height-roots/1

    testcase = [
        [
            5,
            4,
            [[0, 2], [1, 2], [2, 3], [3, 4]],
            [2, 3],
        ],
        [
            4,
            3,
            [[0, 1], [0, 2], [0, 3]],
            [0],
        ],
    ]

    for line in testcase:
        [V, E, edges, expected] = line
        s2 = Solution2()
        result = s2.minHeightRoot(V, edges)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 25 of March 2026

    p1()

    p2()
