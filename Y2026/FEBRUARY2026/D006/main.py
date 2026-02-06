from typing import List


class Solution1:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # nums = [1,6,2,9], k = 3
        # sorted = [1 2 6 9]
        # condition to satisfy ->
        # nums[l] * k >= nums[r]
        # we have to find maximum subarray that satisfy the condition
        # for each pointer l have to find largest pointer r that satisfy
        # nums[r] <= nums[l] * k

        nums.sort()
        n = len(nums)

        l = 0
        max_len = 0

        for r in range(n):
            while nums[r] > nums[l] * k:
                l += 1

            max_len = max(max_len, r - l + 1)

        return n - max_len

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3634. Minimum Removals to Balance Array - https://leetcode.com/problems/minimum-removals-to-balance-array/description/?envType=daily-question&envId=2026-02-06

    testcase = [
        [[2, 1, 5], 2, 1],
        [[1, 6, 2, 9], 3, 2],
        [[4, 6], 2, 0],
    ]

    for line in testcase:
        [nums, k, expected] = line
        s1 = Solution1()
        result = s1.minRemoval(nums, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def smallestDiff(self, a, b, c):
        # code here.
        # minimize (max − min)
        # find closest values

        a.sort()
        b.sort()
        c.sort()

        i = j = k = 0
        best_diff = float("inf")
        best_sum = float("inf")
        ans = []

        while i < len(a) and j < len(b) and k < len(c):
            x, y, z = a[i], b[j], c[k]

            mx = max(x, y, z)
            mn = min(x, y, z)

            diff = mx - mn
            s = x + y + z

            if diff < best_diff or (diff == best_diff and s < best_sum):
                best_diff = diff
                best_sum = s
                ans = [x, y, z]

            if mn == x:
                i += 1
            elif mn == y:
                j += 1
            else:
                k += 1

        return sorted(ans, reverse=True)

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Happiest Triplet - https://www.geeksforgeeks.org/problems/happiest-triplet2921/1

    testcase = [
        [[5, 2, 8], [10, 7, 12], [9, 14, 6], [7, 6, 5]],
        [[15, 12, 18, 9], [10, 17, 13, 8], [14, 16, 11, 5], [11, 10, 9]],
    ]

    for line in testcase:
        [a, b, c, expected] = line
        s2 = Solution2()
        result = s2.smallestDiff(a, b, c)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 6 of February 2026

    p1()

    p2()
