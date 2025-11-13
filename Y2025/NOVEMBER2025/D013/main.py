class Solution1:
    def maxOperations(self, s: str) -> int:
        N = len(s)

        operationsCount = 0
        prefix = 0

        for i in range(N):
            if s[i] == "1":
                prefix += 1
            elif i == N - 1 or s[i + 1] == "1":
                operationsCount += prefix

        return operationsCount

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3228. Maximum Number of Operations to Move Ones to the End - https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/description/?envType=daily-question&envId=2025-11-13

    testcases = ["1001101", "00111"]

    for testcase in testcases:
        sol1 = Solution1()
        count = sol1.maxOperations(testcase)
        print(count)


class Solution2:
    def recursion(self, s1, i, s2, j, s3, k):
        if k >= len(s3):
            return i >= len(s1) and j >= len(s2)

        path1 = False
        path2 = False

        if i < len(s1) and s1[i] == s3[k]:
            path1 = self.recursion(s1, i + 1, s2, j, s3, k + 1)

        if j < len(s2) and s2[j] == s3[k]:
            path2 = self.recursion(s1, i, s2, j + 1, s3, k + 1)

        return path1 or path2

        # Complexity analysis
        # Time : O(2^N*M)
        # Space : O(N+M)

    def memoization(self, s1, i, s2, j, s3, k, memo):
        if k >= len(s3):
            return i >= len(s1) and j >= len(s2)

        if memo[i][j] != -1:
            return memo[i][j]

        memo[i][j] = False

        if i < len(s1) and s1[i] == s3[k]:
            memo[i][j] = memo[i][j] or self.memoization(
                s1, i + 1, s2, j, s3, k + 1, memo
            )

        if not memo[i][j] and j < len(s2) and s2[j] == s3[k]:
            memo[i][j] = memo[i][j] or self.memoization(
                s1, i, s2, j + 1, s3, k + 1, memo
            )

        return memo[i][j]

        # Complexity analysis
        # Time : O(2*N*M)
        # Space : O(N*M) + O(N+M)

    def tabulation(self, s1, s2, s3):
        N, M = len(s1), len(s2)
        if len(s3) != N + M:
            return False

        dp = [[False] * (M + 1) for _ in range(N + 1)]
        dp[0][0] = True

        for i in range(1, N + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for j in range(1, M + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                    dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                )

        return dp[N][M]

        # Complexity analysis
        # Time : O(N*M)
        # Space : O(N*M)

    def isInterleave(self, s1, s2, s3):
        # code here
        # return self.recursion(s1, 0, s2, 0, s3, 0)

        # N = len(s1) + 1
        # M = len(s2) + 1
        # memo = [[-1 for _ in range(M)] for _ in range(N)]
        # return self.memoization(s1, 0, s2, 0, s3, 0, memo)

        return self.tabulation(s1, s2, s3)


def p2():
    # Problem 2 : POTD Geeksforgeeks Interleaved Strings - https://www.geeksforgeeks.org/problems/interleaved-strings/1

    testcases = [
        ["AAB", "AAC", "AAAABC"],
        ["AB", "C", "ACB"],
        ["YX", "X", "XXY"],
    ]

    for testcase in testcases:
        [s1, s2, s3] = testcase
        sol2 = Solution2()
        out = sol2.isInterleave(s1, s2, s3)
        print(out)


if __name__ == "__main__":
    # Day 13 of November 2025

    p1()

    p2()
