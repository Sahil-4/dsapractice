from typing import List

from sortedcontainers import SortedList
from collections import defaultdict, deque
import math


class Solution1:
    def minOperations(self, s: str, k: int) -> int:
        # BFS

        n, m = len(s), s.count("0")  # n = length, m = initial number of zeros

        dist = [math.inf] * (n + 1)

        # separate unvisited states by parity (even/odd zero counts)
        nodeSets = [
            SortedList(range(0, n + 1, 2)),
            SortedList(range(1, n + 1, 2)),
        ]

        q = deque([m])
        dist[m] = 0
        nodeSets[m % 2].remove(m)

        while q:
            m = q.popleft()

            # compute valid range of zeros after one operation
            c1, c2 = max(k - n + m, 0), min(m, k)
            lnode, rnode = m + k - 2 * c2, m + k - 2 * c1

            nodeSet = nodeSets[lnode % 2]
            idx = nodeSet.bisect_left(lnode)

            # visit all reachable zero-count states in [lnode, rnode]
            while idx < len(nodeSet) and nodeSet[idx] <= rnode:
                m2 = nodeSet[idx]
                dist[m2] = dist[m] + 1
                q.append(m2)
                nodeSet.pop(idx)

        return int(-1 if dist[0] == math.inf else dist[0])

        # Complexity analysis
        # Time: O(N log N)
        # Space: O(N)


def p1():
    # Problem 1 : POTD Leetcode 3666. Minimum Operations to Equalize Binary String - https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/description/?envType=daily-question&envId=2026-02-27

    testcase = [
        ["110", 1, 1],
        ["0101", 3, 2],
        ["101", 2, -1],
    ]

    for line in testcase:
        [s, k, expected] = line
        s1 = Solution1()
        result = s1.minOperations(s, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countSquare(self, mat: List[List[int]], x: int):
        res = 0

        n = len(mat)
        m = len(mat[0])

        # row-wise prefix sum
        rowPrefix = [row[:] for row in mat]
        for i in range(n):
            for j in range(1, m):
                rowPrefix[i][j] += rowPrefix[i][j - 1]

        maxSize = min(n, m)

        # all square sizes
        for size in range(1, maxSize + 1):

            # possible column ranges [i, j] of width 'size'
            for i in range(m - size + 1):
                j = i + size - 1
                total = 0

                # sum for top (size - 1) rows of the square window
                for row in range(size - 1):
                    total += rowPrefix[row][j] - (rowPrefix[row][i - 1] if i > 0 else 0)

                # window down row by row
                for row in range(size - 1, n):
                    total += rowPrefix[row][j] - (rowPrefix[row][i - 1] if i > 0 else 0)

                    # current square has sum x
                    if total == x:
                        res += 1

                    # remove top row of the previous window
                    total -= rowPrefix[row - size + 1][j] - (
                        rowPrefix[row - size + 1][i - 1] if i > 0 else 0
                    )

        return res

        # Complexity analysis
        # Time: O(M * N * min(N, M))
        # Space: O(M)


def p2():
    # Problem 2 : POTD Geeksforgeeks Number of submatrix have sum X - https://www.geeksforgeeks.org/problems/number-of-submatrix-have-sum-k/1

    testcase = [
        [
            [[2, 4, 7, 8, 10], [3, 1, 1, 1, 1], [9, 11, 1, 2, 1], [12, -17, 1, 1, 1]],
            10,
            3,
        ],
        [
            [[3, 3, 5, 3], [2, 2, 2, 6], [11, 2, 2, 4]],
            1,
            0,
        ],
    ]

    for line in testcase:
        [mat, x, expected] = line
        s2 = Solution2()
        result = s2.countSquare(mat, x)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 27 of February 2026

    p1()

    p2()
