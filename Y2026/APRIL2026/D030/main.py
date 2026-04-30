import heapq
from typing import List


class Solution1:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        N = len(grid)
        M = len(grid[0])

        # dp[row][col][cost] = max score
        dp = [[[-1] * (k + 1) for _ in range(M)] for _ in range(N)]

        # start
        dp[0][0][0] = 0

        for row in range(N):
            for col in range(M):
                for cost in range(k + 1):
                    if dp[row][col][cost] == -1:
                        continue

                    # move right
                    if col + 1 < M:
                        val = grid[row][col + 1]
                        cost_inc = 1 if val > 0 else 0
                        new_cost = cost + cost_inc

                        if new_cost <= k:
                            dp[row][col + 1][new_cost] = max(
                                dp[row][col + 1][new_cost],
                                dp[row][col][cost] + val,
                            )

                    # move down
                    if row + 1 < N:
                        val = grid[row + 1][col]
                        cost_inc = 1 if val > 0 else 0
                        new_cost = cost + cost_inc

                        if new_cost <= k:
                            dp[row + 1][col][new_cost] = max(
                                dp[row + 1][col][new_cost],
                                dp[row][col][cost] + val,
                            )

        # answer
        score = max(dp[N - 1][M - 1])

        return score if score != -1 else -1

        # Complexity analysis
        # Time : O(N * M * K)
        # Space : O(N * M * K)


def p1():
    # Problem 1 : POTD Leetcode 3742. Maximum Path Score in a Grid - https://leetcode.com/problems/maximum-path-score-in-a-grid/description/?envType=daily-question&envId=2026-04-30

    testcase = [
        [[[0, 1], [2, 0]], 1, 2],
        [[[0, 1], [1, 2]], 1, -1],
        [[[0, 1, 1, 2, 0], [2, 2, 0, 1, 1]], 2, -1],
    ]

    for line in testcase:
        [grid, k, expected] = line
        s1 = Solution1()
        result = s1.maxPathScore(grid, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def isMaxHeap(self, arr: List[int]) -> bool:
        # code here
        # u -> parent
        # [2 * u + 1] -> left child
        # [2 * u + 2] -> right child
        # ensure left child < parent and right child < parent

        N = len(arr)

        for i in range(N):
            left = 2 * i + 1
            right = 2 * i + 2

            # exhausted
            if left >= N and right >= N:
                break

            # left child does not satisfy
            if left < N and arr[left] > arr[i]:
                return False

            # right child does not satisfy
            if right < N and arr[right] > arr[i]:
                return False

        return True

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Check if an Array is Max Heap - https://www.geeksforgeeks.org/problems/does-array-represent-heap4345/1

    testcase = [
        [[90, 15, 10, 7, 12, 2], True],
        [[9, 15, 10, 7, 12, 11], False],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.isMaxHeap(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 30 of April 2026

    p1()

    p2()
