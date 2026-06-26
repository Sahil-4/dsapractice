from functools import cache
from typing import List


class Solution1:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:

        N = len(nums)

        prefix_frequency = [0] * (2 * N + 1)

        current_prefix = N
        prefix_frequency[current_prefix] = 1

        valid_prefixes = 0
        subarray_count = 0

        for number in nums:

            if number == target:
                # Prefix sum increases by 1.
                valid_prefixes += prefix_frequency[current_prefix]
                current_prefix += 1
            else:
                # Prefix sum decreases by 1.
                current_prefix -= 1
                valid_prefixes -= prefix_frequency[current_prefix]

            prefix_frequency[current_prefix] += 1
            subarray_count += valid_prefixes

        return subarray_count

        # Complexity analysis
        # Time : O(N)
        # Space: O(N)


def p1():
    # Problem 1 : POTD Leetcode 3739. Count Subarrays With Majority Element II - https://leetcode.com/problems/count-subarrays-with-majority-element-ii/?envType=daily-question&envId=2026-06-26

    testcase = [
        [[1, 2, 2, 3], 2, 5],
        [[1, 1, 1, 1], 1, 10],
        [[1, 2, 3], 4, 0],
    ]

    for line in testcase:
        [nums, target, expected] = line
        s1 = Solution1()
        result = s1.countMajoritySubarrays(nums, target)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    s1 = ""
    N = 0
    s2 = ""
    M = 0

    @cache
    def solve_recursion(self, s1i: int = 0, s2i: int = 0) -> int:

        # found a valid way
        if s2i == self.M:
            return 1

        # went out of scope
        if s1i == self.N:
            return 0

        count = 0

        # not pick
        count += self.solve_recursion(s1i + 1, s2i)

        # pick
        if self.s1[s1i] == self.s2[s2i]:
            count += self.solve_recursion(s1i + 1, s2i + 1)

        return count

    def solve_tabulation(self) -> int:
        MOD = 1000000007
        dp = [[0] * (self.M + 1) for _ in range(self.N + 1)]

        for s1i in range(self.N, -1, -1):

            for s2i in range(self.M, -1, -1):

                # found a valid way
                if s2i == self.M:
                    dp[s1i][s2i] = 1
                    continue

                # went out of scope
                if s1i == self.N:
                    dp[s1i][s2i] = 0
                    continue

                dp[s1i][s2i] = 0

                # not pick
                dp[s1i][s2i] = (dp[s1i][s2i] + dp[s1i + 1][s2i]) % MOD

                # pick
                if self.s1[s1i] == self.s2[s2i]:
                    dp[s1i][s2i] = (dp[s1i][s2i] + dp[s1i + 1][s2i + 1]) % MOD

        return dp[0][0] % MOD

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(N * M)

    def countWays(self, s1: str, s2: str) -> int:
        # code here

        self.s1 = s1
        self.s2 = s2

        self.N = len(self.s1)
        self.M = len(self.s2)

        # return self.solve_recursion()
        return self.solve_tabulation()


def p2():
    # Problem 2 : POTD Geeksforgeeks Count Matching Subsequences - https://www.geeksforgeeks.org/problems/find-number-of-times-a-string-occurs-as-a-subsequence3020/1

    testcase = [
        ["geeksforgeeks", "gks", 4],
        ["problemoftheday", "geek", 0],
    ]

    for line in testcase:
        [str1, str2, expected] = line
        s2 = Solution2()
        result = s2.countWays(str1, str2)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 26 of June 2026

    p1()

    p2()
