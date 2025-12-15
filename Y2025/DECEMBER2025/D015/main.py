from typing import List


class Solution1:
    def getDescentPeriods(self, prices: List[int]) -> int:
        N = len(prices)

        count = 1

        l = 0
        r = 1

        while r < N:
            if prices[r - 1] - prices[r] != 1:
                l = r

            count += r - l + 1
            r += 1

        return count

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2110. Number of Smooth Descent Periods of a Stock - https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/?envType=daily-question&envId=2025-12-15

    testcase = [
        [[3, 2, 1, 4], 7],
        [[8, 6, 7, 7], 4],
        [[1], 1],
    ]

    for line in testcase:
        [prices, expected] = line
        s1 = Solution1()
        result = s1.getDescentPeriods(prices)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def cntWays(self, arr):
        # code here
        n = len(arr)

        total_even = sum(arr[i] for i in range(0, n, 2))
        total_odd = sum(arr[i] for i in range(1, n, 2))

        left_even = left_odd = 0
        count = 0

        for i in range(n):
            # remove current element from total
            if i % 2 == 0:
                total_even -= arr[i]
            else:
                total_odd -= arr[i]

            # calculate sums after removal
            new_even = left_even + total_odd
            new_odd = left_odd + total_even

            if new_even == new_odd:
                count += 1

            # add current element to left sums
            if i % 2 == 0:
                left_even += arr[i]
            else:
                left_odd += arr[i]

        return count

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count Indices to Balance Even and Odd Sums - https://www.geeksforgeeks.org/problems/count-indices-to-balance-even-and-odd-sums/1

    testcase = [
        [[2, 1, 6, 4], 1],
        [[1, 1, 1], 3],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.cntWays(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 15 of December 2025

    p1()

    p2()
