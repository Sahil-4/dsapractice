from typing import List


class Solution1:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # precompute row sum
        # and col sum
        # if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1
        # increment count of special cells

        special_cells = 0

        R = len(mat)
        C = len(mat[0])

        row_sum = [0] * R
        col_sum = [0] * C

        for i in range(R):
            for j in range(C):
                row_sum[i] += mat[i][j]

        for j in range(C):
            for i in range(R):
                col_sum[j] += mat[i][j]

        for i in range(R):
            for j in range(C):
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    special_cells += 1

        return special_cells

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(N + M)


def p1():
    # Problem 1 : POTD Leetcode 1582. Special Positions in a Binary Matrix - https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/?envType=daily-question&envId=2026-03-04

    testcase = [
        [[[1, 0, 0], [0, 0, 1], [1, 0, 0]], 1],
        [[[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3],
    ]

    for line in testcase:
        [mat, expected] = line
        s1 = Solution1()
        result = s1.numSpecial(mat)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxSubarrayXOR(self, arr, k):
        # code here
        # if we have computed xor = a XOR b XOR c
        # and we want to remove `a` we can do xor = xor XOR a
        # we can use sliding window technique
        # maintain a window of size k,
        # xor is precomputed - while creating or updating window
        # for all subarray of size k
        # find the max xor and return it

        N = len(arr)
        max_xor = 0

        xor = 0
        for i in range(N):
            xor = xor ^ arr[i]
            if i >= k:
                xor = xor ^ arr[i - k]

            if i >= k - 1:
                max_xor = max(max_xor, xor)

        return max_xor

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Xor Subarray of size K - https://www.geeksforgeeks.org/problems/max-xor-subarray-of-size-k/1

    testcase = [
        [[2, 5, 8, 1, 1, 3], 3, 15],
        [[1, 2, 4, 5, 6], 2, 6],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.maxSubarrayXOR(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 4 of March 2026

    p1()

    p2()
