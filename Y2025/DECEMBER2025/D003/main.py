from collections import defaultdict
from typing import List
from functools import lru_cache


class Solution1:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        INF = 10**9 + 7
        MID_KEY_MULTIPLIER = 10000

        n = len(points)
        ans = 0

        slope_to_intercept = defaultdict(list)
        mid_to_slope = defaultdict(list)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x1 - x2
                dy = y1 - y2

                if x2 == x1:
                    k = INF
                    b = x1
                else:
                    k = (y2 - y1) / (x2 - x1)
                    b = (y1 * dx - x1 * dy) / dx

                mid = (x1 + x2) * MID_KEY_MULTIPLIER + (y1 + y2)
                slope_to_intercept[k].append(b)
                mid_to_slope[mid].append(k)

        for sti in slope_to_intercept.values():
            if len(sti) == 1:
                continue

            cnt = defaultdict(int)
            for b_val in sti:
                cnt[b_val] += 1

            total_sum = 0
            for count in cnt.values():
                ans += total_sum * count
                total_sum += count

        for mts in mid_to_slope.values():
            if len(mts) == 1:
                continue

            cnt = defaultdict(int)
            for k_val in mts:
                cnt[k_val] += 1

            total_sum = 0
            for count in cnt.values():
                ans -= total_sum * count
                total_sum += count

        return ans

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(N*N)


def p1():
    # Problem 1 : POTD Leetcode 3625. Count Number of Trapezoids II - https://leetcode.com/problems/count-number-of-trapezoids-ii/description/?envType=daily-question&envId=2025-12-03

    testcase = [
        [[[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]], 2],
        [[[0, 0], [1, 0], [0, 1], [2, 1]], 1],
    ]

    for line in testcase:
        [points, expected] = line
        s1 = Solution1()
        result = s1.countTrapezoids(points)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    T = 10**9

    def recursion(self, curr, mask):
        if ((1 << self.n) - 1) == mask:
            # all visited 11..1
            return self.cost[curr][0]

        min_cost = self.T

        for neighbor in range(self.n):
            if (neighbor == curr) or (mask & (1 << neighbor)):
                continue

            cost = self.recursion(neighbor, (mask | (1 << neighbor)))
            min_cost = min(min_cost, self.cost[curr][neighbor] + cost)

        return min_cost

        # Complexity analysis
        # O(n!)
        # O(n)

    def memoization(self, curr, mask, memo):
        if ((1 << self.n) - 1) == mask:
            # all visited 11..1
            return self.cost[curr][0]

        min_cost = self.T

        for neighbor in range(self.n):
            if (neighbor == curr) or (mask & (1 << neighbor)):
                continue

            cost = self.memoization(neighbor, (mask | (1 << neighbor)), memo)
            min_cost = min(min_cost, self.cost[curr][neighbor] + cost)

        return min_cost

        # Complexity analysis
        # O(n * 2^n)
        # O(n * 2^n)

    def tabulation(self):
        FULL = (1 << self.n) - 1
        dp = [[self.T] * (1 << self.n) for _ in range(self.n)]

        # base
        for curr in range(self.n):
            dp[curr][FULL] = self.cost[curr][0]

        # fill dp
        for mask in range(FULL - 1, -1, -1):
            for curr in range(self.n):

                # next cities
                for nxt in range(self.n):
                    if (mask & (1 << nxt)) != 0:
                        continue  # already visited

                    new_mask = mask | (1 << nxt)
                    dp[curr][mask] = min(
                        dp[curr][mask],
                        self.cost[curr][nxt] + dp[nxt][new_mask],
                    )

        start_mask = 1 << 0
        return dp[0][start_mask]

        # Complexity analysis
        # O(n^2 * 2^n)
        # O(n * 2^n)

    def optimized(self, cost):
        FULL = (1 << self.n) - 1
        n = self.n

        @lru_cache(None)
        def dp(curr, mask):
            if mask == FULL:
                return cost[curr][0]

            best = self.T

            row = cost[curr]

            remaining = (~mask) & FULL

            while remaining:
                nxt = (remaining & -remaining).bit_length() - 1
                new_mask = mask | (1 << nxt)
                best = min(best, row[nxt] + dp(nxt, new_mask))
                remaining &= remaining - 1

            return best

        return dp(0, 1)

    def tsp(self, cost):
        # code here
        start = 0  # also end
        mask = 1 << 0

        self.cost = cost
        self.n = len(cost)

        # return self.recursion(start, mask)

        # memo = [[-1 for _ in range(self.n)] for _ in range(self.n)]
        # return self.memoization(start, mask, memo)

        # return self.tabulation()
        return self.optimized(cost)


def p2():
    # Problem 2 : POTD Geeksforgeeks Travelling Salesman Problem - https://www.geeksforgeeks.org/problems/travelling-salesman-problem2732/1

    testcase = [
        [[[0, 111], [112, 0]], 223],
        [[[0, 1000, 5000], [5000, 0, 1000], [1000, 5000, 0]], 3000],
    ]

    for line in testcase:
        [cost, expected] = line
        s2 = Solution2()
        result = s2.tsp(cost)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 3 of December 2025

    p1()

    p2()
