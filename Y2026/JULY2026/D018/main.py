from math import gcd


class Solution1:
    def findGCD(self, nums: list[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        return gcd(min_num, max_num)

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1979. Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/?envType=daily-question&envId=2026-07-18

    testcase = [
        [[2, 5, 6, 9, 10], 2],
        [[7, 5, 6, 8, 3], 1],
        [[3, 3], 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.findGCD(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findWays(self, matrix: list[list[int]], k: int) -> int:
        MOD = 10**9 + 7

        N = len(matrix)
        M = len(matrix[0])

        # suffix sum of 1's
        suffix = [[0] * (M + 1) for _ in range(N + 1)]
        for r in range(N - 1, -1, -1):
            for c in range(M - 1, -1, -1):
                suffix[r][c] = (
                    suffix[r + 1][c]
                    + suffix[r][c + 1]
                    - suffix[r + 1][c + 1]
                    + matrix[r][c]
                )

        # dp[r][c][pieces]
        dp = [[[0] * (k + 1) for _ in range(M)] for _ in range(N)]

        # base case
        for r in range(N):
            for c in range(M):
                if suffix[r][c] > 0:
                    dp[r][c][1] = 1

        for pieces in range(2, k + 1):

            # row suffix sums
            suffix_row = [[0] * M for _ in range(N + 1)]
            for c in range(M):
                for r in range(N - 1, -1, -1):
                    suffix_row[r][c] = (
                        suffix_row[r + 1][c] + dp[r][c][pieces - 1]
                    ) % MOD

            # column suffix sums
            suffix_col = [[0] * (M + 1) for _ in range(N)]
            for r in range(N):
                for c in range(M - 1, -1, -1):
                    suffix_col[r][c] = (
                        suffix_col[r][c + 1] + dp[r][c][pieces - 1]
                    ) % MOD

            for r in range(N - 1, -1, -1):
                for c in range(M - 1, -1, -1):

                    if suffix[r][c] == 0:
                        continue

                    ways = 0

                    # first valid horizontal cut
                    lo, hi = r + 1, N
                    while lo < hi:
                        mid = (lo + hi) // 2
                        if suffix[mid][c] < suffix[r][c]:
                            hi = mid
                        else:
                            lo = mid + 1

                    if lo < N:
                        ways = (ways + suffix_row[lo][c]) % MOD

                    # first valid vertical cut
                    lo, hi = c + 1, M
                    while lo < hi:
                        mid = (lo + hi) // 2
                        if suffix[r][mid] < suffix[r][c]:
                            hi = mid
                        else:
                            lo = mid + 1

                    if lo < M:
                        ways = (ways + suffix_col[r][lo]) % MOD

                    dp[r][c][pieces] = ways

        return dp[0][0][k]

        # Complexity analysis
        # Time : O(N * M * k * log(N + M))
        # Space : O(N * M * k)


def p2():
    # Problem 2 : POTD Geeksforgeeks Cut Matrix - https://www.geeksforgeeks.org/problems/cut-matrix/1

    testcase = [
        [[[1, 0, 0], [1, 1, 1], [0, 0, 0]], 3, 3],
        [[[0, 0], [1, 1]], 2, 1],
        [[[1, 0], [0, 0]], 1, 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.findWays(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 18 of July 2026

    p1()

    p2()
