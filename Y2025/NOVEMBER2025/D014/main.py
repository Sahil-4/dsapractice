from typing import List
from functools import lru_cache


class Solution1:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for query in queries:
            [row1i, col1i, row2i, col2i] = query

            diff[row1i][col1i] += 1
            diff[row1i][col2i + 1] -= 1
            diff[row2i + 1][col1i] -= 1
            diff[row2i + 1][col2i + 1] += 1

        output = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                output[i][j] = diff[i][j]

                if j > 0:
                    output[i][j] += output[i][j - 1]
                if i > 0:
                    output[i][j] += output[i - 1][j]
                if i > 0 and j > 0:
                    output[i][j] -= output[i - 1][j - 1]

        return output

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(N * N)


def p1():
    # Problem 1 : POTD Leetcode 2536. Increment Submatrices by One - https://leetcode.com/problems/increment-submatrices-by-one/description/?envType=daily-question&envId=2025-11-14

    class Testcase:
        n: int
        queries: List[List[int]]

        def __init__(self, n: int, queries: List[List[int]]) -> None:
            self.n = n
            self.queries = queries

    testcases: List[Testcase] = [
        Testcase(3, [[1, 1, 2, 2], [0, 0, 1, 1]]),
        Testcase(2, [[0, 0, 1, 1]]),
    ]

    s1 = Solution1()
    for testcase in testcases:
        matrix = s1.rangeAddQueries(n=testcase.n, queries=testcase.queries)
        print(matrix)


class Solution2:
    def mergeStones(self, stones, k):
        # code here
        n = len(stones)

        # Check if merging to one stone is possible
        if (n - 1) % (k - 1) != 0:
            return -1

        # Prefix sum for fast range sum calculation
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        def range_sum(i, j):
            return prefix[j + 1] - prefix[i]

        @lru_cache(None)
        def dp(i, j, t):
            """
            Minimum cost to merge stones[i..j] into t piles.
            """
            # Length of segment
            # length = j - i + 1

            # Base: single pile
            if i == j:
                return 0 if t == 1 else float("inf")

            # If we want 1 pile, first merge to k piles, then final merge
            if t == 1:
                cost = dp(i, j, k)
                if cost == float("inf"):
                    return cost
                return cost + range_sum(i, j)

            # Otherwise, merge subintervals to reach t piles.
            res = float("inf")

            # Only split at steps of (k-1): optimization
            for mid in range(i, j, k - 1):
                left = dp(i, mid, 1)
                right = dp(mid + 1, j, t - 1)
                res = min(res, left + right)

            return res

        return dp(0, n - 1, 1)

        # Complexity analysis
        # Time : O(N * N * N)
        # Space : O(N * N * K)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Cost to Merge Stones - https://www.geeksforgeeks.org/problems/minimum-cost-to-merge-stones/1

    class T:
        stones: List[int]
        k: int

        def __init__(self, stones: List[int], k: int) -> None:
            self.stones = stones
            self.k = k

    testcases: List[T] = [
        T(stones=[1, 2, 3], k=2),
        T(stones=[1, 5, 3, 2, 4], k=2),
        T(stones=[1, 5, 3, 2, 4], k=4),
    ]

    s2 = Solution2()
    for testcase in testcases:
        tcost = s2.mergeStones(stones=testcase.stones, k=testcase.k)
        print(tcost)


if __name__ == "__main__":
    # Day 14 of November 2025

    p1()

    p2()
