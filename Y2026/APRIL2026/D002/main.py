from typing import List


class Solution1:
    INT_MIN = -1000000000

    def recursion(self, coins, neu, i, j, memo) -> int:
        if i == self.N - 1 and j == self.M - 1:
            if coins[i][j] < 0 and neu > 0:
                return 0
            return coins[i][j]

        if i >= self.N or j >= self.M:
            return self.INT_MIN

        if memo[neu][i][j] != self.INT_MIN:
            return memo[neu][i][j]

        take = coins[i][j] + max(
            self.recursion(coins, neu, i + 1, j, memo),
            self.recursion(coins, neu, i, j + 1, memo),
        )

        skip = self.INT_MIN
        if coins[i][j] < 0 and neu > 0:
            down = self.recursion(coins, neu - 1, i + 1, j, memo)
            right = self.recursion(coins, neu - 1, i, j + 1, memo)
            skip = max(down, right)

        memo[neu][i][j] = max(take, skip)
        return memo[neu][i][j]

        # Complexity analysis
        # Time : O(2 * 2 * N * M)
        # Space : O(2 * N * M)

    def maximumAmount(self, coins: List[List[int]]) -> int:
        self.N = len(coins)
        self.M = len(coins[0])

        neu = 2

        memo = [
            [[self.INT_MIN for _ in range(self.M + 1)] for _ in range(self.N + 1)]
            for _ in range(neu + 1)
        ]

        return self.recursion(coins, neu, 0, 0, memo)


def p1():
    # Problem 1 : POTD Leetcode 3418. Maximum Amount of Money Robot Can Earn - https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/description/?envType=daily-question&envId=2026-04-02

    testcase = [
        [[[0, 1, -1], [1, -2, 3], [2, -3, 4]], 8],
        [[[10, 10, 10], [10, 10, 10]], 40],
    ]

    for line in testcase:
        [coins, expected] = line
        s1 = Solution1()
        result = s1.maximumAmount(coins)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def memoization(
        self,
        K: int,
        N: int,
        last_used: int,
        consecutive_count: int,
        memo: List[List[List[int]]],
    ) -> int:
        if N == 0:
            return 1

        if memo[N][last_used][consecutive_count] != -1:
            return memo[N][last_used][consecutive_count]

        memo[N][last_used][consecutive_count] = 0

        for k in range(K):
            # cant use k
            if k == last_used and consecutive_count >= 2:
                continue

            next_consecutive_count = 1
            if k == last_used:
                next_consecutive_count = consecutive_count + 1

            memo[N][last_used][consecutive_count] += self.memoization(
                K, N - 1, k, next_consecutive_count, memo
            )

        return memo[N][last_used][consecutive_count]

        # Complexity analysis
        # Time : O(N * K * 3 * 2)
        # Space : O(N * K * 3) + O(N) stack space

    def tabulation(self, n, k) -> int:
        if n == 1:
            return k

        same = k
        diff = k * (k - 1)
        total = same + diff  # k * k

        for _ in range(3, n + 1):
            same = diff
            diff = total * (k - 1)
            total = same + diff

        return total

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)

    def countWays(self, n: int, k: int):
        # code here.

        # memo = [[[-1 for _ in range(3)] for _ in range(k + 1)] for _ in range(n + 1)]
        # return self.memoization(k, n, k, 0, memo)

        return self.tabulation(n, k)


def p2():
    # Problem 2 : POTD Geeksforgeeks Painting the Fence - https://www.geeksforgeeks.org/problems/painting-the-fence3727/1

    testcase = [
        [3, 2, 6],
        [2, 4, 16],
        [7, 2, 42],
    ]

    for line in testcase:
        [n, k, expected] = line
        s2 = Solution2()
        result = s2.countWays(n, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 2 of April 2026

    p1()

    p2()
