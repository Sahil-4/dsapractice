from typing import List


class Solution1:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # we can make any number negative or positive (by multiplying it with -1)
        # if there are pairs of negatives
        # we can always make them positive
        # if there are odd number of negative elements
        # we make abs bigger numbers positive
        # take out smallest abs number from remaining (including positives)
        # and except it make all other positive
        # IDEA:
        # if there are even number of negatives
        # we make all of them positive
        # if there are odd number of negatives
        # we make all pairs positive which will give more sum
        # last negative we will compare with smallest positive
        # take abs of both whichever is less make it negative
        # we need only min abs from matrix so we need only one variable instead of two separate for negative and positive

        T = 100000000

        matrix_sum = 0

        N = len(matrix)

        negative_count = 0
        min_abs = T

        for i in range(N):
            for j in range(N):
                if matrix[i][j] < 0:
                    negative_count += 1

                matrix_sum += abs(matrix[i][j])
                min_abs = min(min_abs, abs(matrix[i][j]))

        # subtract leftover negative
        if negative_count & 1:
            # 2* because we already have included it above in NN loop
            matrix_sum -= 2 * min_abs

        return matrix_sum

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1975. Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=daily-question&envId=2026-01-05

    testcase = [
        [[[1, -1], [-1, 1]], 4],
        [[[1, 2, 3], [-1, -2, -3], [1, 2, 3]], 16],
    ]

    for line in testcase:
        [matrix, expected] = line
        s1 = Solution1()
        result = s1.maxMatrixSum(matrix)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxSubarraySum(self, arr: List[int], k: int) -> int:
        # code here
        # keep a window of size k
        # while moving forward remove leftest (out of window) element
        # and add rightest (new element in window) element
        # arr[] = [100, 200, 300, 400], k = 2
        # first window [100, 200]
        # sum = 300, maximum till now = 300 (updated from 0)
        # move towards right
        # next window [200, 300]
        # sum = 300 - 100 + 300 = 500, maximum till now = 500 (updated)
        # move towards right
        # next window [300, 400]
        # sum = 500 - 200 + 400 = 700, maximum till now = 700 (udpated)
        # final output will be 700
        # use left, and right pointers to track window and operate on window
        # use sum variable to track and update window sum
        # and max_sum to track maximum sum
        # pointers can be reduces to only one
        # we can use right (from i = 0 to i < N) and k
        # at every point we can remove element (right - k) if right >= k

        max_sum = 0

        N = len(arr)

        sum = 0
        for right in range(N):
            sum += arr[right]
            if right >= k:
                sum -= arr[right - k]

            max_sum = max(max_sum, sum)

        return max_sum

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Sum Subarray of size K - https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

    testcase = [
        [[100, 200, 300, 400], 2, 700],
        [[1, 4, 2, 10, 23, 3, 1, 0, 20], 4, 39],
        [[100, 200, 300, 400], 1, 400],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.maxSubarraySum(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 5 of January 2026

    p1()

    p2()
