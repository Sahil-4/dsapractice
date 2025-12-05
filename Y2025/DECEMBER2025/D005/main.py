from typing import List


class Solution1:
    def countPartitions(self, nums: List[int]) -> int:
        partition_count = 0

        n = len(nums)

        lsum = 0
        rsum = sum(nums)

        for i in range(n - 1):
            lsum += nums[i]
            rsum -= nums[i]

            sum_difference = abs(lsum - rsum)
            if not (sum_difference & 1):
                partition_count += 1

        return partition_count

        # Complexity analysis
        # Time : N(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3432. Count Partitions with Even Sum Difference - https://leetcode.com/problems/count-partitions-with-even-sum-difference/description/?envType=daily-question&envId=2025-12-05

    testcase = [
        [[10, 10, 3, 7, 6], 4],
        [[1, 2, 2], 0],
        [[2, 4, 6, 8], 3],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.countPartitions(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    INF = float("inf")

    def recursion(self, wall, pcolor):
        if wall == 0:
            return 0

        mcost = self.INF

        for color in range(self.k):
            if color == pcolor:
                continue

            cost = self.costs[wall - 1][color] + self.recursion(wall - 1, color)
            mcost = min(mcost, cost)

        return mcost

        # Complexity analysis
        # Time : O(K^N)
        # Space : O(N)

    def memoization(self, wall, pcolor, memo):
        if wall == 0:
            return 0

        if memo[wall][pcolor] != -1:
            return memo[wall][pcolor]

        mcost = self.INF

        for color in range(self.k):
            if color == pcolor:
                continue

            cost = self.costs[wall - 1][color] + self.memoization(wall - 1, color, memo)
            mcost = min(mcost, cost)

        memo[wall][pcolor] = mcost
        return memo[wall][pcolor]

        # Complexity analysis
        # Time : O(K*K*N)
        # Space : O(N) + O(N * K)

    def tabulation(self):
        memo = [[0.0 for _ in range(self.k + 1)] for _ in range(self.n + 1)]

        for wall in range(1, self.n + 1):
            for pcolor in range(0, self.k + 1):
                mcost = self.INF

                for color in range(self.k):
                    if color == pcolor:
                        continue

                    cost = self.costs[wall - 1][color] + memo[wall - 1][color]
                    mcost = min(mcost, cost)

                memo[wall][pcolor] = mcost

        return memo[self.n][self.k]

        # Complexity analysis
        # Time : O(K*K*N)
        # Space : O(N) + O(N * K)

    def optimized(self):
        # min1 and min2 approach

        # dp_prev[c] will hold dp for the previous wall
        dp_prev = [0.0] * self.k

        for i in range(self.n):
            dp_curr = [0.0] * self.k

            # Step 1: find min1, min2 and index of min1
            min1 = min2 = float("inf")
            min1_color = -1

            for c in range(self.k):
                val = dp_prev[c]
                if val < min1:
                    min2 = min1
                    min1 = val
                    min1_color = c
                elif val < min2:
                    min2 = val

            # Step 2: compute dp for current wall using min1/min2 trick
            for c in range(self.k):
                if c == min1_color:
                    dp_curr[c] = self.costs[i][c] + min2
                else:
                    dp_curr[c] = self.costs[i][c] + min1

            dp_prev = dp_curr  # move to next wall

        return min(dp_prev)

        # Complexity analysis
        # Time : O(N*K)
        # Space : O(2 * K)

    def minCost(self, costs: List[List[int]]) -> int:
        # code here
        self.costs = costs
        self.n = len(costs)
        self.k = len(costs[0])

        if self.n == 1:
            return min(costs[0])

        # out = self.recursion(self.n, self.k)
        # memo = [[-1 for _ in range(self.k + 1)] for _ in range(self.n + 1)]
        # out = self.memoization(self.n, self.k, memo)

        # out = self.tabulation()
        out = self.optimized()

        return int(out if out != self.INF else -1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Walls Coloring II - https://www.geeksforgeeks.org/problems/walls-coloring-ii--170647/1

    testcase = [
        [4, 3, [[1, 5, 7], [5, 8, 4], [3, 2, 9], [1, 2, 4]], 8],
        [5, 1, [[5], [4], [9], [2], [1]], -1],
    ]

    for line in testcase:
        [n, k, costs, expected] = line
        s2 = Solution2()
        result = s2.minCost(costs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 5 of December 2025

    p1()

    p2()
