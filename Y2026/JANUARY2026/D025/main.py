from typing import List
from functools import lru_cache


class Solution1:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # k = 1, only one score return 0
        # k = 2, pick closest two element max - min will give least difference
        # k > 2, pick closest k element (adjacent upon sorting)
        # and calculate difference between min and max of this window
        # do this for all windows and build final answer
        # choose k scores that are as close together as possible,
        # answer is (max − min) of that group

        if k == 1:
            return 0

        nums.sort()
        ans = float("inf")

        for i in range(len(nums) - k + 1):
            ans = min(ans, nums[i + k - 1] - nums[i])

        return int(ans)

        # Complexity analysis
        # Time : O(N * Log(N)) + O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1984. Minimum Difference Between Highest and Lowest of K Scores - https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/?envType=daily-question&envId=2026-01-25

    testcase = [
        [[90], 1, 0],
        [[9, 4, 1, 7], 2, 2],
    ]

    for line in testcase:
        [nums, k, expected] = line
        s1 = Solution1()
        result = s1.minimumDifference(nums, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findWays(self, n):
        # code here
        # Catalan number
        # let "(" = +1
        # and ")" = -1
        # we start with place parentheses we can possibly place ["(", ")"]
        # at any point if we get sum of parentheses in negative we return 0
        # at the end ie. at index = n
        # we return 1 if sum == 0 - denoting we get one possible way
        # instead of maintaining a stack of parens just use a variable parensum

        if n % 2 == 1:
            return 0

        pairs = n // 2

        @lru_cache(None)
        def dfs(index, open_used, paren_sum):
            # invalid state
            if paren_sum < 0:
                return 0

            # finished building string
            if index == n:
                return 1 if paren_sum == 0 else 0

            ways = 0

            # try placing "("
            if open_used < pairs:
                ways += dfs(index + 1, open_used + 1, paren_sum + 1)

            # try placing ")"
            if paren_sum > 0:
                ways += dfs(index + 1, open_used, paren_sum - 1)

            return ways

        return dfs(0, 0, 0)

        # Complexity analysis
        # Time : < O(2^N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Number of Valid Parentheses - https://www.geeksforgeeks.org/problems/valid-number-of-parenthesis/1

    testcase = [
        [2, 1],
        [4, 2],
        [6, 5],
    ]

    for line in testcase:
        [n, expected] = line
        s2 = Solution2()
        result = s2.findWays(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 25 of January 2026

    p1()

    p2()
