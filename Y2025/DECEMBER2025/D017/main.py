class Solution1:
    def maximumProfit(self, prices, k):
        n = len(prices)
        NEG = -(10**18)

        # dp[i][k][state]
        dp = [[[-1] * 3 for _ in range(k + 1)] for _ in range(n)]

        def solve(i, state, k):
            if k < 0:
                return NEG
            if i == n:
                return 0 if state == 0 else NEG

            if dp[i][k][state] != -1:
                return dp[i][k][state]

            normal = NEG
            short_sell = NEG
            skip = solve(i + 1, state, k)

            if state == 0:
                normal = -prices[i] + solve(i + 1, 1, k)
                short_sell = prices[i] + solve(i + 1, 2, k)

            elif state == 1:
                normal = prices[i] + solve(i + 1, 0, k - 1)

            else:  # state == 2
                short_sell = -prices[i] + solve(i + 1, 0, k - 1)

            dp[i][k][state] = max(normal, short_sell, skip)
            return dp[i][k][state]

        return solve(0, 0, k)

        # Complexity analysis
        # Time: O(N * K)
        # Space: O(N * K)


def p1():
    # Problem 1 : POTD Leetcode 3573. Best Time to Buy and Sell Stock V - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/description/?envType=daily-question&envId=2025-12-17

    testcase = [
        [[1, 7, 9, 8, 2], 2, 14],
        [[12, 16, 19, 19, 8, 1, 19, 13, 9], 3, 36],
    ]

    for line in testcase:
        [prices, k, expected] = line
        s1 = Solution1()
        result = s1.maximumProfit(prices, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def mergeOverlap(self, arr):
        # Code here

        N = len(arr)

        # sort arr on (arr[1],arr[0])
        arr.sort(key=lambda interval: interval[0])

        # merge overlapping intervals
        output = []
        starti = arr[0][0]
        endi = arr[0][1]

        for i in range(1, N + 1):
            if i == N or endi < arr[i][0]:
                output.append([starti, endi])
                if i == N:
                    break
                starti = arr[i][0]
                endi = arr[i][1]

            starti = min(starti, arr[i][0])
            endi = max(endi, arr[i][1])

        return output

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Overlapping Intervals - https://www.geeksforgeeks.org/problems/overlapping-intervals--170633/1

    testcase = [
        [[[1, 3], [2, 4], [6, 8], [9, 10]], [[1, 4], [6, 8], [9, 10]]],
        [[[6, 8], [1, 9], [2, 4], [4, 7]], [[1, 9]]],
        [[[1, 2], [2, 3], [3, 4], [5, 6]], [[1, 4], [5, 6]]],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.mergeOverlap(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 17 of December 2025

    p1()

    p2()
