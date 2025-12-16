class Solution1:
    def __init__(self):
        self.B = 0

    def merge(self, dp1, dp2):
        next_dp = [-int(1e9)] * (self.B + 1)
        for i in range(self.B + 1):
            if dp1[i] < 0:
                continue
            for j in range(self.B - i + 1):
                if dp2[j] < 0:
                    continue
                next_dp[i + j] = max(next_dp[i + j], dp1[i] + dp2[j])
        return next_dp

    def dfs(self, u, tree, present, future, dp):
        skipBranch = [-int(1e9)] * (self.B + 1)
        buyBranch = [-int(1e9)] * (self.B + 1)

        skipBranch[0] = 0
        buyBranch[0] = 0

        for v in tree[u]:
            self.dfs(v, tree, present, future, dp)
            skipBranch = self.merge(skipBranch, dp[v][0])
            buyBranch = self.merge(buyBranch, dp[v][1])

        for parentBought in range(2):
            price = present[u] // 2 if parentBought else present[u]
            profit = future[u] - price

            currentDP = skipBranch[:]

            if price <= self.B:
                for b in range(self.B - price + 1):
                    if buyBranch[b] > -int(1e9):
                        currentDP[b + price] = max(
                            currentDP[b + price], buyBranch[b] + profit
                        )

            dp[u][parentBought] = currentDP

    def maxProfit(self, n, present, future, hierarchy, budget):
        self.B = budget
        tree = [[] for _ in range(n)]
        for edge in hierarchy:
            tree[edge[0] - 1].append(edge[1] - 1)

        dp = [[[0] * (self.B + 1) for _ in range(2)] for _ in range(n)]

        self.dfs(0, tree, present, future, dp)

        ans = 0
        for b in range(self.B + 1):
            ans = max(ans, dp[0][0][b])
        return ans


def p1():
    # Problem 1 : POTD Leetcode 3562. Maximum Profit from Trading Stocks with Discounts - https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/description/?envType=daily-question&envId=2025-12-16

    testcase = [
        [2, [1, 2], [4, 3], [[1, 2]], 3, 5],
        [2, [3, 4], [5, 8], [[1, 2]], 4, 4],
        [3, [4, 6, 8], [7, 9, 11], [[1, 2], [1, 3]], 10, 10],
        [3, [5, 2, 3], [8, 5, 6], [[1, 2], [2, 3]], 7, 12],
    ]

    for line in testcase:
        [n, present, future, hierarchy, budget, expected] = line
        s1 = Solution1()
        result = s1.maxProfit(n, present, future, hierarchy, budget)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def areRotations(self, s1, s2):
        # code here
        if len(s1) != len(s2):
            return False

        return s2 in (s1 + s1)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Strings Rotations of Each Other - https://www.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1

    testcase = [
        ["abcd", "cdab", True],
        ["aab", "aba", True],
        ["abcd", "acbd", False],
    ]

    for line in testcase:
        [str1, str2, expected] = line
        s2 = Solution2()
        result = s2.areRotations(str1, str2)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 16 of December 2025

    p1()

    p2()
