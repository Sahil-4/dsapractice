from typing import List


class Solution1:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        N = len(nums)

        l = -1
        r = 0
        while r < N:
            if nums[r] == 1:
                if l != -1 and r - l - 1 < k:
                    return False
                l = r
            r += 1

        return True

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1437. Check If All 1's Are at Least Length K Places Away - https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/?envType=daily-question&envId=2025-11-17

    testcases = [
        [[1, 0, 0, 0, 1, 0, 0, 1], 2],
        [[1, 0, 0, 1, 0, 1], 2],
    ]

    for [nums, k] in testcases:
        s1 = Solution1()
        print("nums=", nums)
        print("k=", k)
        print("OUT=", s1.kLengthApart(nums, k))


class Solution2:
    def memoization(self, arr, curr_index, prev_index, memo):
        if curr_index >= len(arr):
            return 0

        key = (curr_index, prev_index)

        if key in memo:
            return memo[key]

        skip = self.memoization(arr, curr_index + 1, prev_index, memo)
        take = 0
        if prev_index == -1 or arr[curr_index] > arr[prev_index]:
            take = arr[curr_index] + self.memoization(
                arr, curr_index + 1, curr_index, memo
            )

        memo[key] = max(skip, take)

        return memo[key]

        # Complexity analysis
        # Time : O(2*N*N)
        # Space : O(N*N) + O(N)

    def tabulation(self, arr):
        N = len(arr)
        memo = {}

        for prev_index in range(N, -2, -1):
            key = (N, prev_index)
            memo[key] = 0

        for curr_index in range(N - 1, -1, -1):
            for prev_index in range(curr_index, -2, -1):
                key = (curr_index, prev_index)

                skip = memo[(curr_index + 1, prev_index)]
                take = 0

                if prev_index == -1 or arr[curr_index] > arr[prev_index]:
                    take = arr[curr_index] + memo[(curr_index + 1, curr_index)]

                memo[key] = max(skip, take)

        return memo[(0, -1)]

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(N*N)

    def maxSumIS(self, arr):
        # code here

        # memo = {}
        # return self.memoization(arr, 0, -1, memo)

        return self.tabulation(arr)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Sum Increasing Subsequence - https://www.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence4749/1

    testcases = [
        [1, 101, 2, 3, 100],
        [4, 1, 2, 3],
        [4, 1, 2, 4],
    ]

    for nums in testcases:
        s2 = Solution2()
        print("nums=", nums)
        print("OUT=", s2.maxSumIS(nums))


if __name__ == "__main__":
    # Day 17 of November 2025

    p1()

    p2()
