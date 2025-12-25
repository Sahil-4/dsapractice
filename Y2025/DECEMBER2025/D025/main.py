from typing import List


class Solution1:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        max_happiness = 0

        # sort in DESC
        happiness.sort()
        happiness.reverse()

        for i in range(k):
            max_happiness += max(0, happiness[i] - i)

        return max_happiness

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3075. Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/description/?envType=daily-question&envId=2025-12-25

    testcase = [
        [[1, 2, 3], 2, 4],
        [[1, 1, 1, 1], 2, 1],
        [[2, 3, 4, 5], 1, 5],
    ]

    for line in testcase:
        [happiness, k, expected] = line
        s1 = Solution1()
        result = s1.maximumHappinessSum(happiness, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])

        left, right = 0, m - 1

        while left <= right:
            mid = (left + right) // 2

            # Find row index of maximum element in mid column
            max_row = 0
            for i in range(n):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i

            # Get left and right neighbors
            left_val = mat[max_row][mid - 1] if mid - 1 >= 0 else float("-inf")
            right_val = mat[max_row][mid + 1] if mid + 1 < m else float("-inf")

            # Check peak condition
            if mat[max_row][mid] >= left_val and mat[max_row][mid] >= right_val:
                return [max_row, mid]

            # Move towards bigger neighbor
            elif right_val > mat[max_row][mid]:
                left = mid + 1
            else:
                right = mid - 1

        return [-1, -1]

        # Complexity analysis
        # Time : O(N * Log(M))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Find the Peak Element in a 2D Matrix - https://www.geeksforgeeks.org/problems/find-the-peak-element-in-a-2d-matrix/1

    testcase = [
        [[[10, 20, 15], [21, 30, 14], [7, 16, 32]], [1, 1]],
        [[[17, 7], [11, 10]], [0, 0]],
    ]

    for line in testcase:
        [mat, expected] = line
        s2 = Solution2()
        result = s2.findPeakGrid(mat)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 25 of December 2025

    p1()

    p2()
