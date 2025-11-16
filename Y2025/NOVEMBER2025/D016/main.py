class Solution1:
    def numSub(self, s: str) -> int:
        modulo = 1000000007

        count = 0

        n = len(s)
        l = 0
        r = 0

        while r < n:
            if s[r] == "1":
                more = r - l + 1
                count = count + more
                count = count % modulo
            else:
                l = r + 1

            r += 1

        return int(count)

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1513. Number of Substrings With Only 1s - https://leetcode.com/problems/number-of-substrings-with-only-1s/description/?envType=daily-question&envId=2025-11-16

    testcases = [
        "0110111",
        "101",
        "111111",
        "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
    ]

    for testcase in testcases:
        s1 = Solution1()
        print(s1.numSub(testcase))


class Solution2:
    def LCIS(self, a, b):
        # code here
        n, m = len(a), len(b)

        # dp[j] = length of LCIS ending at b[j]
        dp = [0] * m

        for i in range(n):
            current_best = 0
            for j in range(m):
                if a[i] > b[j]:
                    current_best = max(current_best, dp[j])
                elif a[i] == b[j]:
                    dp[j] = current_best + 1

        return max(dp) if dp else 0


def p2():
    # Problem 2 : POTD Geeksforgeeks Longest Common Increasing Subsequence - https://www.geeksforgeeks.org/problems/longest-common-increasing-subsequence1437/1

    testcases = [
        [[3, 4, 9, 1], [5, 3, 8, 9, 10, 2, 1]],
        [[1, 1, 4, 3], [1, 1, 3, 4]],
    ]
    for [a, b] in testcases:
        s2 = Solution2()
        print(s2.LCIS(a, b))


if __name__ == "__main__":
    # Day 16 of November 2025

    p1()

    p2()
