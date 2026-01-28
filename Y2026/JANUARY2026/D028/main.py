from collections import Counter
from typing import List


class Solution1:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        inf = int(1e5) * 8

        cost = [[inf] * m for _ in range(n)]
        cost[-1][-1] = 0
        tcost = [inf] * (max(max(row) for row in grid) + 1)

        for _ in range(k + 1):
            for i in range(n - 1, -1, -1):
                for j in range(m - 1, -1, -1):
                    if i < n - 1:
                        cost[i][j] = min(cost[i][j], cost[i + 1][j] + grid[i + 1][j])
                    if j < m - 1:
                        cost[i][j] = min(cost[i][j], cost[i][j + 1] + grid[i][j + 1])
                    cost[i][j] = min(cost[i][j], tcost[grid[i][j]])

            for i in range(n):
                for j in range(m):
                    tcost[grid[i][j]] = min(tcost[grid[i][j]], cost[i][j])

            for i in range(1, len(tcost)):
                tcost[i] = min(tcost[i], tcost[i - 1])

        return cost[0][0]

        # Complexity analysis
        # Time : O(K * N * M)
        # Space : O(N * M)


def p1():
    # Problem 1 : POTD Leetcode 3651. Minimum Cost Path with Teleportations - https://leetcode.com/problems/minimum-cost-path-with-teleportations/description/?envType=daily-question&envId=2026-01-28

    testcase = [
        [[[1, 3, 3], [2, 5, 4], [4, 3, 5]], 2, 7],
        [[[1, 2], [2, 3], [3, 4]], 1, 9],
    ]

    for line in testcase:
        [grid, k, expected] = line
        s1 = Solution1()
        result = s1.minCost(grid, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countSubset(self, arr, k):
        # code here
        # use meet in the middle
        # generate subset sum of left and right half separately
        # then use frequency map for each sum in right part subsets
        # convert this problem into two sum
        # left subset sum + right subset sum == k
        # this gives us 1 valid answer
        # use frequency map to count (k - left subset sum)

        n = len(arr)
        mid = n // 2

        left = arr[:mid]
        right = arr[mid:]

        def gen_sums(nums, idx, curr, res):
            if idx == len(nums):
                res.append(curr)
                return
            gen_sums(nums, idx + 1, curr, res)
            gen_sums(nums, idx + 1, curr + nums[idx], res)

        left_sums = []
        right_sums = []

        gen_sums(left, 0, 0, left_sums)
        gen_sums(right, 0, 0, right_sums)

        freq = Counter(right_sums)

        ans = 0
        for s in left_sums:
            ans += freq[k - s]

        return ans

        # Complexity analysis
        # Time : O(2^(n/2))
        # Space : O(2^(n/2))


def p2():
    # Problem 2 : POTD Geeksforgeeks Count Subset With Target Sum II - https://www.geeksforgeeks.org/problems/count-the-subset-with-sum-equal-to-k/1

    testcase = [
        [[1, 3, 2], 3, 2],
        [[4, 2, 3, 1, 2], 4, 3],
        [[10, 20, 30], 25, 0],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.countSubset(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 28 of January 2026

    p1()

    p2()
