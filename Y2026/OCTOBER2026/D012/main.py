class Solution1:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 1000000007
        BITS = 30

        # AND / OR operation never changes the count of set bits at any bit position,
        # it only moves the set bits between elements
        bit_count = [0] * BITS
        for num in nums:
            for b in range(BITS):
                if (num >> b) & 1:
                    bit_count[b] += 1

        # sum of squares is maximised by making few numbers as large as possible,
        # build each of the k numbers greedily by packing all the remaining set bits into it
        total = 0
        for _ in range(k):
            value = 0

            for b in range(BITS):
                if bit_count[b] > 0:
                    value |= 1 << b
                    bit_count[b] -= 1

            total = (total + value * value) % MOD

        return total

        # Complexity analysis
        # Time : O(BITS * (N + K))
        # Space : O(BITS)


def p1():
    # Problem 1 : POTD Leetcode 2897. Apply Operations on Array to Maximize Sum of Squares - https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/description/?envType=daily-question&envId=2026-10-12

    testcase = [
        [[2, 6, 5, 8], 2, 261],
        [[4, 5, 4, 7], 3, 90],
        [[1000000000], 1, 49],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maxSum(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minCuts(self, n: int, m: int) -> int:
        # code here

        # every full cut removes the largest possible square from the remaining paper,
        # the shorter side is the square side, so this is the euclidean algorithm;
        # a / b squares are removed in one go, then the remaining paper is b x (a % b)
        count = 0

        a, b = max(n, m), min(n, m)

        while b > 0:
            count += a // b
            a, b = b, a % b

        return count

        # Complexity analysis
        # Time : O(log(min(N, M)))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Squares with Full Cuts - https://www.geeksforgeeks.org/problems/squares-in-reactangle3340/1

    testcase = [
        [1, 1, 1],
        [2, 3, 3],
        [4, 6, 3],
        [2, 4, 2],
        [5, 8, 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minCuts(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            # best profit if we sell today, having bought at the cheapest earlier day
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 121. Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[7, 1, 5, 3, 6, 4], 5],
        [[7, 6, 4, 3, 1], 0],
        [[5], 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.maxProfit(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 12 of October 2026

    p1()

    p2()

    p3()
