import heapq
from typing import List


class Solution1:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # sort input
        N = len(nums)
        nums_copy = list(nums)
        nums_copy.sort()

        for i in range(N):
            if nums_copy[i] == original:
                original *= 2

        return original

        # Complexity analysis
        # Time : O(N * Log(N)) + O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2154. Keep Multiplying Found Values by Two - https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/?envType=daily-question&envId=2025-11-19

    testcases = [
        ([5, 3, 6, 1, 12], 3, 24),
        ([2, 7, 9], 4, 4),
    ]

    for testcase in testcases:
        nums, original, expected = testcase
        sol = Solution1()
        result = sol.findFinalValue(nums, original)
        assert result == expected, f"Testcase failed: expected {expected}, got {result}"
        print(
            f"Testcase passed: nums={nums}, original_input={testcase[1]}, result={result}"
        )


class Trio:
    def __init__(self, cost, row, col):
        self.cost = cost
        self.row = row
        self.col = col

    def __lt__(self, other):
        if self.cost != other.cost:
            return self.cost < other.cost
        if self.row != other.row:
            return self.row < other.row
        return self.col < other.col


class Solution:
    MAXIMUM = int(1e9)

    DROWS = [-1, 0, 0, 1]
    DCOLS = [0, -1, 1, 0]

    @staticmethod
    def isValidIndex(r, c, n, m):
        return 0 <= r < n and 0 <= c < m

    def minCostPath(self, matrix):
        # Dijkstra

        ROWS = len(matrix)
        COLS = len(matrix[0])

        result = [[Solution.MAXIMUM] * COLS for _ in range(ROWS)]

        pq = []
        result[0][0] = 0

        heapq.heappush(pq, Trio(0, 0, 0))

        while pq:
            top = heapq.heappop(pq)

            cost = top.cost
            row = top.row
            col = top.col

            for i in range(4):
                nrow = row + Solution.DROWS[i]
                ncol = col + Solution.DCOLS[i]

                if Solution.isValidIndex(nrow, ncol, ROWS, COLS):
                    absCost = abs(matrix[row][col] - matrix[nrow][ncol])
                    maxCost = max(cost, absCost)

                    if result[nrow][ncol] > maxCost:
                        result[nrow][ncol] = maxCost
                        heapq.heappush(pq, Trio(maxCost, nrow, ncol))

        return result[ROWS - 1][COLS - 1]


def p2():
    # Problem 2 : POTD Geeksforgeeks Path With Minimum Effort - https://www.geeksforgeeks.org/problems/path-with-minimum-effort/1

    testcases = [
        (
            [
                [1, 2, 2],
                [3, 8, 2],
                [5, 3, 5],
            ],
            2,
        ),
        (
            [
                [1, 2, 3],
                [3, 8, 4],
                [5, 3, 5],
            ],
            1,
        ),
        (
            [
                [1, 2, 1, 1, 1],
                [1, 2, 1, 2, 1],
                [1, 2, 1, 2, 1],
                [1, 2, 1, 2, 1],
                [1, 1, 1, 2, 1],
            ],
            0,
        ),
    ]

    for testcase in testcases:
        matrix, expected = testcase
        sol = Solution()
        result = sol.minCostPath(matrix)
        assert result == expected, f"Testcase failed: expected {expected}, got {result}"
        print(f"Testcase passed: result={result}")


if __name__ == "__main__":
    # Day 19 of November 2025

    p1()

    p2()
