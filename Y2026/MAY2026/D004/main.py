from typing import List


class Solution1:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        # swap matrix[i][j], matrix[j][i]
        for i in range(N):
            for j in range(i, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse each row
        for i in range(N):
            matrix[i].reverse()

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 48. Rotate Image - https://leetcode.com/problems/rotate-image/description/?envType=daily-question&envId=2026-05-04

    testcase = [
        [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
        ],
        [
            [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
            [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
        ],
    ]

    for line in testcase:
        [matrix, expected] = line
        s1 = Solution1()
        s1.rotate(matrix)
        result = matrix
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def isBinaryPalindrome(self, n: int) -> bool:
        # code here
        binary_n = bin(n)[2:]
        binary_n_rev = binary_n[::-1]

        return binary_n == binary_n_rev

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Palindrome Binary - https://www.geeksforgeeks.org/problems/palindrome-numbers0942/1

    testcase = [
        [17, True],
        [16, False],
    ]

    for line in testcase:
        [n, expected] = line
        s2 = Solution2()
        result = s2.isBinaryPalindrome(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 4 of May 2026

    p1()

    p2()
