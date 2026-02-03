from typing import List


class Solution1:
    def isTrionic(self, nums: List[int]) -> bool:
        # [0, ..., p, ..., q, ...]

        N = len(nums)

        i = 1

        # phase 1: increasing
        while i < N and nums[i] > nums[i - 1]:
            i += 1
        if i == 1 or i == N:
            return False

        # phase 2: decreasing
        while i < N and nums[i] < nums[i - 1]:
            i += 1
        if i == N:
            return False

        # phase 3: increasing
        while i < N and nums[i] > nums[i - 1]:
            i += 1

        return i == N

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3637. Trionic Array I - https://leetcode.com/problems/trionic-array-i/description/?envType=daily-question&envId=2026-02-03

    testcase = [
        [[1, 3, 5, 4, 2, 6], True],
        [[2, 1, 3], False],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.isTrionic(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxProfit(self, prices):
        # code here
        # key point : buy on low and sell on high

        N = len(prices)

        profit = 0

        buy_index = 0
        for sell_index in range(1, N):
            # buy on low
            if prices[buy_index] > prices[sell_index]:
                buy_index = sell_index

            # calculate profit - if sold on sell_index price
            profit = max(profit, prices[sell_index] - prices[buy_index])

        return profit

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Stock Buy and Sell – Max one Transaction Allowed - https://www.geeksforgeeks.org/problems/buy-stock-2/1

    testcase = [
        [[7, 10, 1, 3, 6, 9, 2], 8],
        [[7, 6, 4, 3, 1], 0],
        [[1, 3, 6, 9, 11], 10],
    ]

    for line in testcase:
        [prices, expected] = line
        s2 = Solution2()
        result = s2.maxProfit(prices)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 3 of February 2026

    p1()

    p2()
