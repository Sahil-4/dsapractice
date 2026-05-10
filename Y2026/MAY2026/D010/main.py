from functools import cache
import heapq
from typing import List


class Solution1:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        N = len(nums)

        @cache
        def recursion(i: int = 0):
            if i == N - 1:
                return 0

            min_jumps = -1

            for j in range(i + 1, N):
                diff = nums[j] - nums[i]
                if diff <= target and diff >= -target:
                    __next = recursion(j)

                    if __next != -1:
                        min_jumps = max(min_jumps, __next + 1)

            return min_jumps

        ans = recursion()
        return ans

        # Complexity analysis
        # Time : O(N^2)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2770. Maximum Number of Jumps to Reach the Last Index - https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/description/?envType=daily-question&envId=2026-05-10

    testcase = [
        [[1, 3, 6, 4, 1, 2], 2, 3],
        [[1, 3, 6, 4, 1, 2], 3, 5],
        [[1, 3, 6, 4, 1, 2], 0, -1],
    ]

    for line in testcase:
        [nums, target, expected] = line
        s1 = Solution1()
        result = s1.maximumJumps(nums, target)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxProfit(self, x: int, y: int, a: list, b: list) -> int:
        # code here
        tasks = []

        for i in range(len(a)):
            diff = abs(a[i] - b[i])
            tasks.append((diff, a[i], b[i]))

        # largest difference first
        tasks.sort(reverse=True)

        profit = 0

        for _, pa, pb in tasks:

            # prefer A
            if pa >= pb:
                if x > 0:
                    profit += pa
                    x -= 1
                else:
                    profit += pb
                    y -= 1

            # prefer B
            else:
                if y > 0:
                    profit += pb
                    y -= 1
                else:
                    profit += pa
                    x -= 1

        return profit

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Profit from Two Machines - https://www.geeksforgeeks.org/problems/max-profit-from-two-machines/1

    testcase = [
        [3, 3, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 21],
        [4, 4, [1, 4, 3, 2, 7, 5, 9, 6], [1, 2, 3, 6, 5, 4, 9, 8], 43],
        [3, 4, [8, 7, 15, 19, 16, 16, 18], [1, 7, 15, 11, 12, 31, 9], 110],
    ]

    for line in testcase:
        [x, y, a, b, expected] = line
        s2 = Solution2()
        result = s2.maxProfit(x, y, a, b)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 10 of May 2026

    p1()

    p2()
