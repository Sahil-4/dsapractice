from typing import List
import math


class Solution1:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)

        min_sub_len = 0
        count_non_one = 0

        __gcd = nums[0]
        for num in nums:
            __gcd = math.gcd(__gcd, num)
            if num != 1:
                count_non_one += 1

        if __gcd != 1:
            return -1

        min_sub_len = int(1e9)
        for i in range(N):
            ___gcd = nums[i]
            for j in range(i + 1, N):
                ___gcd = math.gcd(___gcd, nums[j])
                if ___gcd == 1:
                    min_sub_len = min(min_sub_len, j - i + 1)

        return (min_sub_len - 1) + (count_non_one - 1)

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2654. Minimum Number of Operations to Make All Array Elements Equal to 1 - https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/description/?envType=daily-question&envId=2025-11-12

    testcases = [
        [2, 6, 3, 4],
        [2, 10, 6, 14],
        [2, 10, 6, 12, 14, 28, 280, 7, 21, 14],
        [2, 10, 6, 12, 14, 28, 280, 7, 21, 14, 5, 35],
        [2, 10, 6, 12, 14, 28, 280, 7, 21, 14, 35, 5],
        [2, 10, 6, 12, 14, 28, 280, 21, 7, 14],
        [6, 10, 15],
    ]

    s1 = Solution1()
    for testcase in testcases:
        print(s1.minOperations(testcase))


class Solution2:
    TN = 0
    PN = 0

    def recursion(self, txt, pat, ti, pi):
        if ti >= self.TN:
            check = True
            for j in range(pi, self.PN):
                check = check and pat[j] == "*"
            return check
        if ti >= self.TN or pi >= self.PN:
            return False

        if txt[ti] == pat[pi]:
            return self.recursion(txt, pat, ti + 1, pi + 1)
        elif pat[pi] == "?":
            return self.recursion(txt, pat, ti + 1, pi + 1)
        elif pat[pi] == "*":
            op1 = self.recursion(txt, pat, ti + 1, pi)
            op2 = self.recursion(txt, pat, ti, pi + 1)
            op3 = self.recursion(txt, pat, ti + 1, pi + 1)
            return op1 or op2 or op3
        else:
            return False

        # Complexity analysis
        # Time : O(2^N*M)
        # Space : O(N+M)

    def memoization(self, txt, pat, ti, pi, memo):
        if ti >= self.TN:
            check = True
            for j in range(pi, self.PN):
                check = check and pat[j] == "*"
            return check
        if ti >= self.TN or pi >= self.PN:
            return False

        if memo[ti][pi] != -1:
            return memo[ti][pi]

        memo[ti][pi] = False

        if txt[ti] == pat[pi]:
            memo[ti][pi] = self.memoization(txt, pat, ti + 1, pi + 1, memo)
        elif pat[pi] == "?":
            memo[ti][pi] = self.memoization(txt, pat, ti + 1, pi + 1, memo)
        elif pat[pi] == "*":
            memo[ti][pi] = memo[ti][pi] or self.memoization(txt, pat, ti + 1, pi, memo)
            memo[ti][pi] = memo[ti][pi] or self.memoization(txt, pat, ti, pi + 1, memo)
            memo[ti][pi] = memo[ti][pi] or self.memoization(
                txt, pat, ti + 1, pi + 1, memo
            )
        else:
            memo[ti][pi] = False

        return memo[ti][pi]

        # Complexity analysis
        # Time : O(2*N*M)
        # Space : O(N*M) + O(N+M)

    def tabulation(self, txt, pat):
        memo = [[False for _ in range(self.PN + 1)] for _ in range(self.TN + 1)]
        memo[self.TN][self.PN] = True
        j = self.PN - 1
        while j >= 0 and pat[j] == "*":
            memo[self.TN][j] = True
            j -= 1

        for ti in range(self.TN - 1, -1, -1):
            for pi in range(self.PN - 1, -1, -1):
                if txt[ti] == pat[pi]:
                    memo[ti][pi] = memo[ti + 1][pi + 1]
                elif pat[pi] == "?":
                    memo[ti][pi] = memo[ti + 1][pi + 1]
                elif pat[pi] == "*":
                    memo[ti][pi] = memo[ti][pi] or memo[ti + 1][pi]
                    memo[ti][pi] = memo[ti][pi] or memo[ti][pi + 1]
                    memo[ti][pi] = memo[ti][pi] or memo[ti + 1][pi + 1]
                else:
                    memo[ti][pi] = False

        return memo[0][0]

        # Complexity analysis
        # Time : O(N*M)
        # Space : O(N*M)

    def wildCard(self, txt, pat):
        # code here
        # txt = "abcde", pat = "a?c*"
        # abc

        self.TN = len(txt)
        self.PN = len(pat)

        # use dp
        # return self.recursion(txt, pat, 0, 0);

        # memo = [[-1 for _ in range(self.PN)] for _ in range(self.TN)]
        # return self.memoization(txt, pat, 0, 0, memo);

        return self.tabulation(txt, pat)


def p2():
    # Problem 2 : POTD Geeksforgeeks Wildcard Pattern Matching - https://www.geeksforgeeks.org/problems/wildcard-pattern-matching/1

    testcases = [
        ["abcde", "a?c*"],
        ["baaabab", "a*ab"],
        ["abc", "*"],
        ["abbbbb", "a*ab"],
    ]

    s2 = Solution2()
    for testcase in testcases:
        txt = testcase[0]
        pat = testcase[1]
        print(s2.wildCard(txt, pat))


if __name__ == "__main__":
    # Day 12 of November 2025

    p1()

    p2()
