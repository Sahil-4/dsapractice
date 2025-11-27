from typing import List


class Solution1:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        ans = -(10**18)
        prefix = 0

        n = len(nums)

        min_prefix = [10**18 for _ in range(k)]
        min_prefix[k - 1] = 0

        for i in range(n):
            prefix += nums[i]

            rem = i % k

            if i >= k - 1:
                ans = max(ans, prefix - min_prefix[rem])
            if i == k - 1:
                ans = prefix

            min_prefix[rem] = min(min_prefix[rem], prefix)

        return ans

        # Complexity analysis
        # Time : O(N)
        # Space : O(K)


def p1():
    # Problem 1 : POTD Leetcode 3381. Maximum Subarray Sum With Length Divisible by K - https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/description/?envType=daily-question&envId=2025-11-27

    testcase = [
        [[1, 2], 1, 3],
        [[-1, -2, -3, -4, -5], 4, -10],
        [[-5, 1, 2, -3, 4], 2, 4],
    ]

    for line in testcase:
        [nums, k, expected] = line
        s1 = Solution1()
        result = s1.maxSubarraySum(nums, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def subsetXORSum(self, arr):
        # code here
        # bit magic

        or_result = 0
        for num in arr:
            or_result |= num

        xor_result = or_result << len(arr) - 1

        return xor_result

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks All Subsets Xor Sum - https://www.geeksforgeeks.org/problems/sum-of-xor-of-all-possible-subsets/1

    testcase = [
        [[7, 2], 14],
        [[1, 2, 3], 12],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.subsetXORSum(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 27 of November 2025

    p1()

    p2()
