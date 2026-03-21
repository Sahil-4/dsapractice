from bisect import bisect_left
from typing import List


class Solution1:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        # iterate over half the rows of the submatrix
        for i in range(k // 2):
            for j in range(k):
                # Swap elements vertically
                grid[x + i][y + j], grid[x + k - 1 - i][y + j] = (
                    grid[x + k - 1 - i][y + j],
                    grid[x + i][y + j],
                )

        return grid

        # Complexity analysis
        # Time : O(k^2)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3643. Flip Square Submatrix Vertically - https://leetcode.com/problems/flip-square-submatrix-vertically/description/?envType=daily-question&envId=2026-03-21

    testcase = [
        [
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            1,
            0,
            3,
            [[1, 2, 3, 4], [13, 14, 15, 8], [9, 10, 11, 12], [5, 6, 7, 16]],
        ],
        [
            [[3, 4, 2, 3], [2, 3, 4, 2]],
            0,
            2,
            2,
            [[3, 4, 4, 2], [2, 3, 2, 3]],
        ],
    ]

    for line in testcase:
        [grid, x, y, k, expected] = line
        s1 = Solution1()
        result = s1.reverseSubmatrix(grid, x, y, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:

    def generate_catalan(self, N):
        catalan = [0] * (N + 1)
        catalan[0] = 1

        for i in range(1, N + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - 1 - j]

        return catalan

    def countBSTs(self, arr):
        N = len(arr)

        copy = sorted(arr)
        catalan = self.generate_catalan(N)

        output = [0] * N

        for i in range(N):
            index = bisect_left(copy, arr[i])

            left = index
            right = N - index - 1

            output[i] = catalan[left] * catalan[right]

        return output

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Number of BST From Array - https://www.geeksforgeeks.org/problems/number-of-bst-from-array/1

    testcase = [
        [[2, 1, 3], [1, 2, 2]],
        [[2, 1], [1, 1]],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.countBSTs(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 21 of March 2026

    p1()

    p2()
