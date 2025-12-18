from functools import cmp_to_key


class Solution1:
    def maxProfit(self, prices, strategy, k):
        n = len(prices)

        # base profit (no modification)
        base_profit = 0
        for i in range(n):
            base_profit += strategy[i] * prices[i]

        # prefix sums
        pref_price = [0] * (n + 1)
        pref_contrib = [0] * (n + 1)

        for i in range(n):
            pref_price[i + 1] = pref_price[i] + prices[i]
            pref_contrib[i + 1] = pref_contrib[i] + strategy[i] * prices[i]

        half = k // 2
        best_gain = 0

        # slide window of size k
        for l in range(0, n - k + 1):
            mid = l + half
            r = l + k

            # original contribution in full window
            original = pref_contrib[r] - pref_contrib[l]

            # forced sell contribution in second half
            forced_sell = pref_price[r] - pref_price[mid]

            gain = forced_sell - original
            best_gain = max(best_gain, gain)

        return base_profit + best_gain

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3652. Best Time to Buy and Sell Stock using Strategy - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/description/?envType=daily-question&envId=2025-12-18

    testcase = [
        [
            [4, 2, 8],
            [-1, 0, 1],
            2,
            10,
        ],
        [
            [5, 4, 3],
            [1, 1, 0],
            2,
            9,
        ],
    ]

    for line in testcase:
        [prices, strategy, k, expected] = line
        s1 = Solution1()
        result = s1.maxProfit(prices, strategy, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:

    def solve1(self, arr):
        n = len(arr)
        i, j = 0, n - 1

        # Partition odds (left) and evens (right)
        while i <= j:
            if arr[i] % 2 == 1:
                i += 1
            elif arr[j] % 2 == 0:
                j -= 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        # Sort odds in descending order
        arr[:i] = sorted(arr[:i], reverse=True)

        # Sort evens in ascending order
        arr[i:] = sorted(arr[i:])

        return arr

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(1)

    def solve2(self, arr):
        def cmp(a, b):
            # odd first
            if (a % 2) != (b % 2):
                return -1 if a % 2 else 1

            # both odd → descending
            if a % 2 == 1:
                return -1 if a > b else 1 if a < b else 0

            # both even → ascending
            return -1 if a < b else 1 if a > b else 0

        arr.sort(key=cmp_to_key(cmp))
        return arr

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(1)

    def sortIt(self, arr):
        # code here

        # return self.solve1(arr)
        return self.solve2(arr)


def p2():
    # Problem 2 : POTD Geeksforgeeks Sort in specific order - https://www.geeksforgeeks.org/problems/sort-in-specific-order2422/1

    testcase = [
        [[1, 2, 3, 5, 4, 7, 10], [7, 5, 3, 1, 2, 4, 10]],
        [[0, 4, 5, 3, 7, 2, 1], [7, 5, 3, 1, 0, 2, 4]],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.sortIt(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 18 of December 2025

    p1()

    p2()
