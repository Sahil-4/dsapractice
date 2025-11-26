from typing import List


class Solution1:
    n = 0
    m = 0
    k = 1
    grid = None
    MOD = 10**9 + 7

    def recursion(self, i, j, csum):
        if i >= self.n or j >= self.m:
            return 0
        if i == self.n - 1 and j == self.m - 1:
            return ((csum + self.grid[i][j]) % self.k) == 0

        right = self.recursion(i, j + 1, csum + self.grid[i][j])
        down = self.recursion(i + 1, j, csum + self.grid[i][j])

        return right + down

        # Complexity analysis
        # Time : O(2^(N+M))
        # Space : O(N+M)

    def memoization(self, i, j, csum, memo):
        if i >= self.n or j >= self.m:
            return 0
        if i == self.n - 1 and j == self.m - 1:
            return ((csum + self.grid[i][j]) % self.k) == 0

        if memo[i][j][csum] != -1:
            return memo[i][j][csum]

        ncsum = (csum + self.grid[i][j]) % self.k

        right = self.memoization(i, j + 1, ncsum, memo)
        down = self.memoization(i + 1, j, ncsum, memo)

        memo[i][j][csum] = (right + down) % self.MOD

        return memo[i][j][csum]

        # Complexity analysis
        # Time : O(2*(N*M*K))
        # Space : O(N*M*K) + O(N+M)

    def tabulation(self):
        dp = [[[0] * self.k for _ in range(self.m)] for _ in range(self.n)]
        dp[0][0][self.grid[0][0] % self.k] = 1

        for i in range(self.n):
            for j in range(self.m):
                for r in range(self.k):
                    if dp[i][j][r] == 0:
                        continue

                    if i + 1 < self.n:
                        nr = (r + self.grid[i + 1][j]) % self.k
                        dp[i + 1][j][nr] = (
                            dp[i + 1][j][nr] + dp[i][j][r]
                        ) % self.MOD  # added modulo

                    if j + 1 < self.m:
                        nr = (r + self.grid[i][j + 1]) % self.k
                        dp[i][j + 1][nr] = (
                            dp[i][j + 1][nr] + dp[i][j][r]
                        ) % self.MOD  # added modulo

        return dp[self.n - 1][self.m - 1][0] % self.MOD  # added modulo

        # Complexity analysis
        # Time : O(N*M*K)
        # Space : O(N*M*K)

    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        self.n = len(grid)
        self.m = len(grid[0])
        self.grid = grid
        self.k = k

        # return self.recursion(0, 0, 0)
        # memo = [[[-1 for _ in range(self.k)] for _ in range(self.m)] for _ in range(self.n)]
        # return self.memoization(0, 0, 0, memo)
        return self.tabulation()


def p1():
    # Problem 1 : POTD Leetcode 2435. Paths in Matrix Whose Sum Is Divisible by K - https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/description/?envType=daily-question&envId=2025-11-26

    testcase = [
        [[[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3, 2],
        [[[0, 0]], 5, 1],
        [[[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1, 10],
    ]

    for line in testcase:
        [grid, k, expected] = line
        s1 = Solution1()
        result = s1.numberOfPaths(grid, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def solve1(self, l, r):
        binaryl = l
        binaryr = r

        count = 0

        while binaryl != binaryr:
            binaryl = binaryl >> 1
            binaryr = binaryr >> 1

            count += 1

        return binaryl << count

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)

    def solve2(self, l, r):
        while r > l:
            r = r & (r - 1)

        return r

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)

    def andInRange(self, l, r):
        # return self.solve1(l, r)
        return self.solve2(l, r)


def p2():
    # Problem 2 : POTD Geeksforgeeks AND In Range - https://www.geeksforgeeks.org/problems/and-operation5726/1

    testcase = [
        [8, 13, 8],
        [2, 3, 2],
    ]

    for line in testcase:
        [l, r, expected] = line
        s2 = Solution2()
        result = s2.andInRange(l, r)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 26 of November 2025

    p1()

    p2()
