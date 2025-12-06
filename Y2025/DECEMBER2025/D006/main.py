from sortedcontainers import SortedList


class Solution1:
    def countPartitions(self, nums, k):
        mod = 10**9 + 7
        n = len(nums)

        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)

        dp[0] = 1
        prefix[0] = 1

        s = SortedList()
        j = 0

        for i in range(n):
            s.add(nums[i])

            while j <= i and (s[-1] - s[0]) > k:
                s.remove(nums[j])
                j += 1

            if j > 0:
                dp[i + 1] = (prefix[i] - prefix[j - 1]) % mod
            else:
                dp[i + 1] = prefix[i] % mod

            prefix[i + 1] = (prefix[i] + dp[i + 1]) % mod

        return dp[n]

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3578. Count Partitions With Max-Min Difference at Most K - https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/description/?envType=daily-question&envId=2025-12-06

    testcase = [
        [[3, 3, 4], 0, 2],
        [[9, 4, 1, 3, 7], 4, 6],
    ]

    for line in testcase:
        [nums, k, expected] = line
        s1 = Solution1()
        result = s1.countPartitions(nums, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def recursion(self, i, j):
        if i > j:
            return 0
        if i == j:
            return self.arr[i]

        take_i = self.arr[i] + min(
            self.recursion(i + 2, j), self.recursion(i + 1, j - 1)
        )
        take_j = self.arr[j] + min(
            self.recursion(i + 1, j - 1), self.recursion(i, j - 2)
        )

        return max(take_i, take_j)

        # Complexity analysis
        # Time : O(2^N)
        # Space : O(N)

    def memoization(self, i, j, memo):
        if i > j:
            return 0
        if i == j:
            return self.arr[i]

        if memo[i][j] != -1:
            return memo[i][j]

        take_i = self.arr[i] + min(
            self.memoization(i + 2, j, memo), self.memoization(i + 1, j - 1, memo)
        )
        take_j = self.arr[j] + min(
            self.memoization(i + 1, j - 1, memo), self.memoization(i, j - 2, memo)
        )

        memo[i][j] = max(take_i, take_j)

        return memo[i][j]

        # Complexity analysis
        # Time : O(2*N*N)
        # Space : O(N) + O(N*N)

    def tabulation(self):
        memo = [[0 for _ in range(self.n + 2)] for _ in range(self.n + 2)]

        for ij in range(self.n):
            memo[ij][ij] = self.arr[ij]

        for i in range(self.n - 1, -1, -1):
            for j in range(0, self.n, 1):
                if i > j:
                    continue

                take_i = self.arr[i] + min(memo[i + 2][j], memo[i + 1][j - 1])
                take_j = self.arr[j] + min(memo[i + 1][j - 1], memo[i][j - 2])

                memo[i][j] = max(take_i, take_j)

        return memo[0][self.n - 1]

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(N*N)

    def maximumAmount(self, arr):
        # code here

        self.arr = arr
        self.n = len(arr)

        # return self.recursion(0, self.n - 1)
        # memo = [[-1 for _ in range(self.n)] for _ in range(self.n)]
        # return self.memoization(0, self.n - 1, memo)
        return self.tabulation()


def p2():
    # Problem 2 : POTD Geeksforgeeks Optimal Strategy For A Game - https://www.geeksforgeeks.org/problems/optimal-strategy-for-a-game-1587115620/1

    testcase = [
        [[5, 3, 7, 10], 15],
        [[8, 15, 3, 7], 22],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.maximumAmount(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 6 of December 2025

    p1()

    p2()
