class Solution1:
    def countTriples(self, n: int) -> int:
        # find tuple (a,b,c) such that
        # a^2 + b^2 = c^2
        # if we have (a,b)
        # we can find c = root of (a^2 + b^2)
        # and if c <= n increment count

        count = 0

        for a in range(1, n + 1, 1):
            for b in range(1, n + 1, 1):
                c = ((a * a) + (b * b)) ** 0.5
                if c == int(c) and c <= n:
                    count += 1

        return count

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1925. Count Square Sum Triples - https://leetcode.com/problems/count-square-sum-triples/description/?envType=daily-question&envId=2025-12-08

    testcase = [
        [5, 2],
        [1, 0],
        [3, 0],
        [13, 6],
    ]

    for line in testcase:
        [n, expected] = line
        s1 = Solution1()
        result = s1.countTriples(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def matrixChainOrder(self, arr):
        n = len(arr)

        dp = [[0.0] * n for _ in range(n)]
        split = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for i in range(1, n - length + 1):
                j = i + length - 1
                dp[i][j] = float("inf")
                for k in range(i, j):
                    cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                    if cost < dp[i][j]:
                        dp[i][j] = cost
                        split[i][j] = k

        def build(i, j):
            if i == j:
                return chr(ord("A") + i - 1)
            k = split[i][j]
            return f"({build(i, k)}{build(k + 1, j)})"

        return build(1, n - 1)

        # Complexity analysis
        # Time : O(N*N*N)
        # Space : O(2*N*N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Brackets in Matrix Chain Multiplication - https://www.geeksforgeeks.org/problems/brackets-in-matrix-chain-multiplication1024/1

    testcase = [
        [],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.matrixChainOrder(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 8 of December 2025

    p1()

    p2()
