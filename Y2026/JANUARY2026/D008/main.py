from functools import lru_cache
from typing import List


class Solution1:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # use dynamic programming (derived from recursion)
        # at each step (i,j) we have four choices
        # take nums1[i], and nums2[j] alone
        # or take nums1[i], and nums2[j] and call recursion/memo for next indices (i+1, j+1)
        # or take only (i+1, j)
        # or take only (i, j+1)
        # at last return whichever is max

        T = -1000000000

        N = len(nums1)
        M = len(nums2)

        @lru_cache(None)
        def solve(i: int, j: int) -> int:
            if i == N or j == M:
                return T

            case1 = nums1[i] * nums2[j]
            case2 = (nums1[i] * nums2[j]) + solve(i + 1, j + 1)
            case3 = solve(i + 1, j)
            case4 = solve(i, j + 1)

            return max(case1, case2, case3, case4)

        return solve(0, 0)

        # Complexity analysis
        # Time : O(2*N*M)
        # Space : O(N*M)


def p1():
    # Problem 1 : POTD Leetcode 1458. Max Dot Product of Two Subsequences - https://leetcode.com/problems/max-dot-product-of-two-subsequences/description/?envType=daily-question&envId=2026-01-08

    testcase = [
        [[2, 1, -2, 5], [3, 0, -6], 18],
        [[3, -2], [2, -6, 7], 21],
        [[-1, -1], [1, 1], -1],
    ]

    for line in testcase:
        [nums1, nums2, expected] = line
        s1 = Solution1()
        result = s1.maxDotProduct(nums1, nums2)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def atMost(self, arr, k):
        left = 0
        count = 0
        odds = 0

        for right in range(len(arr)):
            if arr[right] & 1:
                odds += 1

            while odds > k:
                if arr[left] & 1:
                    odds -= 1
                left += 1

            count += right - left + 1

        return count

    def countSubarrays(self, arr, k):
        # Code here
        # idea:
        # we use a sliding window
        # we continuously expand the right pointer and count odd numbers
        # once the window has exactly k odds, we have a "core" valid window
        # now:
        # any even numbers added to the right will keep the odd count same
        # so each such extension forms a new valid subarray
        # similarly:
        # we can move the left pointer over even numbers
        # and each move still keeps exactly k odds
        # so each shift also forms a new valid subarray
        # but:
        # instead of counting these one by one,
        # we count all such combinations together
        # to simplify counting:
        # number of subarrays with exactly k odds =
        # subarrays with at most k odds - subarrays with at most (k - 1) odds

        return self.atMost(arr, k) - self.atMost(arr, k - 1)

        # Complexity analysis
        # Time : O(2N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count Subarray with k odds - https://www.geeksforgeeks.org/problems/count-subarray-with-k-odds/1

    testcase = [
        [[2, 5, 6, 9], 2, 2],
        [[2, 2, 5, 6, 9, 2, 11], 2, 8],
        [[18, 11, 13, 1, 8, 5, 2, 15, 14, 10, 9, 11, 20, 1], 5, 11],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.countSubarrays(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 8 of January 2026

    p1()

    p2()
