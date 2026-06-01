from typing import List


class Solution1:
    def minimumCost(self, cost: List[int]) -> int:
        N = len(cost)
        cost_arr = cost.copy()
        cost_arr.sort(reverse=True)

        tcost = 0

        for i in range(0, N, 3):
            # pay for  i + 0
            tcost += cost_arr[i + 0]
            # pay for  i + 1
            tcost += cost_arr[i + 1] if i + 1 < N else 0
            # get free i + 2

        return tcost

        # Complexity Analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2144. Minimum Cost of Buying Candies With Discount - https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/?envType=daily-question&envId=2026-06-01

    testcase = [
        [[1, 2, 3], 5],
        [[6, 5, 7, 9, 2, 2], 23],
        [[5, 5], 10],
    ]

    for line in testcase:
        [cost, expected] = line
        s1 = Solution1()
        result = s1.minimumCost(cost)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findMaxProduct(self, arr: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(arr)

        # Single element: return as-is (problem guarantees this is valid)
        if n == 1:
            return arr[0]

        zero_count = 0
        neg_count = 0
        max_neg = None  # least-magnitude negative (closest to 0)
        max_neg_idx = -1

        for i, x in enumerate(arr):
            if x == 0:
                zero_count += 1
            elif x < 0:
                neg_count += 1
                if max_neg is None or x > max_neg:
                    max_neg = x
                    max_neg_idx = i

        # Edge case 1: all zeros
        if zero_count == n:
            return 0

        # Edge case 2: exactly one negative, rest all zeros
        if neg_count == 1 and zero_count == n - 1:
            return 0

        # Multiply all non-zero elements, skipping max_neg if neg_count is odd
        product = 1
        for i, x in enumerate(arr):
            if x == 0:
                continue
            if neg_count % 2 == 1 and i == max_neg_idx:
                continue
            product = ((product * x) % MOD + MOD) % MOD

        return product

        # Complexity Analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Product Subset - https://www.geeksforgeeks.org/problems/maximum-product-subset-of-an-array/1

    testcase = [
        [[-1, 0, -2, 4, 3], 24],
        [[-1, 0], 0],
        [[5], 5],
        [[-1], -1],
        [[-1, -1, -2, 0], 2],
        [[0, 0, 0, 0, 0], 0],
        [[-1, -1, -1, -1, -1], 1],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.findMaxProduct(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 1 of June 2026

    p1()

    p2()
