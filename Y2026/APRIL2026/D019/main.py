import math
from typing import List


class Solution1:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # for each nums1[i]
        # look for last nums_j >= nums1[i], in range nums2[i:M] - say index j
        # update max_dist = max(max_dist, j - i)

        def binary_search(left, right, target) -> int:
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums2[mid] >= target:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        N = len(nums1)
        M = len(nums2)

        max_dist = 0

        for i in range(N):
            nums_i = nums1[i]
            j = binary_search(i, M - 1, nums_i)

            if j != -1:
                max_dist = max(max_dist, j - i)

        return max_dist

        # Complexity analysis
        # Time : O(N * Log(M))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1855. Maximum Distance Between a Pair of Values - https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/description/?envType=daily-question&envId=2026-04-19

    testcase = [
        [[55, 30, 5, 4, 2], [100, 20, 10, 10, 5], 2],
        [[2, 2, 2], [10, 10, 1], 1],
        [[30, 29, 19, 5], [25, 25, 25, 25, 25], 2],
    ]

    for line in testcase:
        [nums1, nums2, expected] = line
        s1 = Solution1()
        result = s1.maxDistance(nums1, nums2)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def isPower(self, x, y):
        # code here

        if x == 1:
            return y == 1

        if y == 1:
            return True

        res = math.log(y) / math.log(x)

        return abs(res - round(res)) < 1e-10

        # Complexity analysis
        # Time : O(1)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Check for Power - https://www.geeksforgeeks.org/problems/check-if-a-number-is-power-of-another-number5442/1

    testcase = [
        [2, 8, True],
        [1, 8, False],
        [46, 205962976, True],
        [50, 312500000, True],
    ]

    for line in testcase:
        [x, y, expected] = line
        s2 = Solution2()
        result = s2.isPower(x, y)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 19 of April 2026

    p1()

    p2()
