class Solution1:
    def maxProduct(self, n: int) -> int:
        first = 0
        second = 0

        while n > 0:
            d = n % 10
            n = n // 10

            if d >= first:
                second = first
                first = d
            elif d > second:
                second = d

        return first * second

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3536. Maximum Product of Two Digits - https://leetcode.com/problems/maximum-product-of-two-digits/description/?envType=daily-question&envId=2026-07-25

    testcase = [
        [31, 3],
        [22, 4],
        [124, 8],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maxProduct(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maximumSum(self, mat: list[list[int]], k: int) -> int:
        # code here

        N = len(mat)

        col_sum = [0] * N
        res = -(1000 * 1000 * 1000)

        for i in range(N):

            for j in range(N):
                col_sum[j] += mat[i][j]
                if i >= k:
                    col_sum[j] -= mat[i - k][j]

            if i >= k - 1:
                window_sum = 0
                for j in range(N):
                    window_sum += col_sum[j]
                    if j >= k:
                        window_sum -= col_sum[j - k]
                    if j >= k - 1:
                        res = max(res, window_sum)

        return res

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Sum Square Sub-Matrix of Size k - https://www.geeksforgeeks.org/problems/coins-of-geekland--141631/1

    testcase = [
        [
            [[1, 2, -1, 4], [-8, -3, 4, 2], [3, 8, 10, -8], [-4, -1, 1, 7]],
            3,
            20,
        ],
        [
            [[4]],
            1,
            4,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maximumSum(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 25 of July 2026

    p1()

    p2()
