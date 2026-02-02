from typing import List
from sortedcontainers import SortedList


class Solution1:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # first subarray always starts at index 0
        # cost always includes nums[0]
        # we need to choose (k-1) starting points after index 0
        # starting index of 2nd to kth subarray must satisfy:
        # ik-1 - i1 <= dist
        # idea:
        # fix nums[0] as first cost
        # from remaining elements, choose (k-1) minimum values
        # such that their indices lie within a sliding window of size dist
        # maintain two sets:
        # kMinimum -> stores (k-1) smallest elements in current window
        # remaining -> stores other elements
        # keep track of sum of elements in kMinimum
        # slide window and update minimum sum
        # final answer = nums[0] + minimum sum found

        n = len(nums)

        # stores (value, index)
        kMinimum = SortedList()  # size <= k-1, smallest elements
        remaining = SortedList()  # rest of elements

        total = 0
        i = 1

        # initial window
        while i - dist < 1:
            kMinimum.add((nums[i], i))
            total += nums[i]

            if len(kMinimum) > k - 1:
                temp = kMinimum[-1]
                total -= temp[0]
                kMinimum.pop()
                remaining.add(temp)
            i += 1

        result = float("inf")

        # sliding window
        while i < n:
            kMinimum.add((nums[i], i))
            total += nums[i]

            if len(kMinimum) > k - 1:
                temp = kMinimum[-1]
                total -= temp[0]
                kMinimum.pop()
                remaining.add(temp)

            result = min(result, total)

            # remove element at (i - dist)
            rem = (nums[i - dist], i - dist)
            if rem in kMinimum:
                kMinimum.remove(rem)
                total -= rem[0]

                if remaining:
                    temp = remaining[0]
                    remaining.pop(0)
                    kMinimum.add(temp)
                    total += temp[0]
            else:
                if rem in remaining:
                    remaining.remove(rem)

            i += 1

        return int(nums[0] + result)

        # Complexity analysis
        # Time : O(N * Log(K))
        # Space : O(dist)


def p1():
    # Problem 1 : POTD Leetcode 3013. Divide an Array Into Subarrays With Minimum Cost II - https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/description/?envType=daily-question&envId=2026-02-02

    testcase = [
        [[1, 3, 2, 6, 4, 2], 3, 3, 5],
        [[10, 1, 2, 2, 2, 1], 4, 3, 15],
        [[10, 8, 18, 9], 3, 1, 36],
    ]

    for line in testcase:
        [nums, k, dist, expected] = line
        s1 = Solution1()
        result = s1.minimumCost(nums, k, dist)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxCircularSum(self, arr):
        # code here
        # loop through i = 0 to i < N
        # run another loop j = 0 to j < N
        # consider element arr[i + j] to put in current subarray (starting from i)
        # update maximum subarray sum

        N = len(arr)

        max_sub_sum = -(10**18)

        # brute force O(N*N)
        # for i in range(N):
        #     sub_sum = 0
        #     for j in range(N):
        #         index = (i + j) % N
        #         sub_sum += arr[index]
        #         max_sub_sum = max(max_sub_sum, sub_sum)

        # optimal solution using kadane
        # idea:
        # maximum circular subarray sum =
        # max(
        #     normal maximum subarray sum (kadane),
        #     total array sum - minimum subarray sum
        # )

        # step 1: normal kadane to find max subarray sum (non-circular)
        curr_max = arr[0]
        max_kadane = arr[0]

        for i in range(1, N):
            curr_max = max(arr[i], curr_max + arr[i])
            max_kadane = max(max_kadane, curr_max)

        # step 2: kadane to find minimum subarray sum
        curr_min = arr[0]
        min_kadane = arr[0]

        for i in range(1, N):
            curr_min = min(arr[i], curr_min + arr[i])
            min_kadane = min(min_kadane, curr_min)

        # step 3: total sum of array
        total_sum = sum(arr)

        # edge case:
        # if all elements are negative
        # total_sum - min_kadane will become 0 (invalid)
        if max_kadane < 0:
            return max_kadane

        # final answer
        # either non-circular max or circular max
        return max(max_kadane, total_sum - min_kadane)

        # Complexity analysis
        # Time : O(2N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Circular Subarray Sum - https://www.geeksforgeeks.org/problems/max-circular-subarray-sum-1587115620/1

    testcase = [
        [[8, -8, 9, -9, 10, -11, 12], 22],
        [[10, -3, -4, 7, 6, 5, -4, -1], 23],
        [[5, -2, 3, 4], 12],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.maxCircularSum(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 2 of February 2026

    p1()

    p2()
