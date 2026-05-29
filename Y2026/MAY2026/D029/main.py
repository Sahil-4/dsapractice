from typing import List
from functools import lru_cache


class Solution1:
    def minElement(self, nums: List[int]) -> int:
        def digit_sum(num: int) -> int:
            dsum = 0

            while num > 0:
                d = num % 10
                dsum += d
                num //= 10

            return dsum

        L = 4
        min_digit_sum = 9 * L

        for num in nums:
            num_digit_sum = digit_sum(num)
            min_digit_sum = min(min_digit_sum, num_digit_sum)

        return min_digit_sum

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3300. Minimum Element After Replacement With Digit Sum - https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/?envType=daily-question&envId=2026-05-29

    testcase = [
        [[10, 12, 13, 14], 1],
        [[1, 2, 3, 4], 1],
        [[999, 19, 199], 10],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.minElement(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def validGroups(self, s: str) -> int:
        # code here

        N = len(s)

        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i + 1] = prefix[i] + int(s[i])

        def digit_sum(l: int, r: int) -> int:
            return prefix[r + 1] - prefix[l]

        @lru_cache(maxsize=None)
        def dp(l: int, prev_sum: int) -> int:
            if l == N:
                return 1

            count = 0

            for r in range(l, N):
                curr = digit_sum(l, r)
                if curr >= prev_sum:
                    count += dp(r + 1, curr)

            return count

        return dp(0, 0)

        # Complexity analysis
        # Time : O(N^3)
        # Space : O(N^2)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count Sorted Digit Groupings - https://www.geeksforgeeks.org/problems/count-digit-groupings-of-a-number1520/1

    testcase = [
        ["1119", 7],
        ["12", 2],
    ]

    for line in testcase:
        [s, expected] = line
        s2 = Solution2()
        result = s2.validGroups(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 29 of May 2026

    p1()

    p2()
