from typing import List


class Solution1:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_non_decreasing():
            N = len(nums)
            for i in range(1, N):
                if nums[i - 1] > nums[i]:
                    return False

            return True

        def min_pair():
            N = len(nums)
            index = 0
            for i in range(0, N - 1):
                if (nums[index] + nums[index + 1]) > (nums[i] + nums[i + 1]):
                    index = i

            return index

        operations_count = 0
        while not is_non_decreasing():
            index = min_pair()

            nums[index] += nums[index + 1]
            nums.pop(index + 1)

            operations_count += 1

        return operations_count

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3507. Minimum Pair Removal to Sort Array I - https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/description/?envType=daily-question&envId=2026-01-22

    testcase = [
        [[5, 2, 3, 1], 2],
        [[1, 2, 2], 0],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.minimumPairRemoval(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def next_small_left(self, arr, n):
        out = [-1] * n
        stk = []

        for i in range(n):
            while stk and arr[stk[-1]] >= arr[i]:
                stk.pop()

            if stk:
                out[i] = stk[-1]
            stk.append(i)

        return out

    def next_small_right(self, arr, n):
        out = [n] * n
        stk = []

        for i in range(n - 1, -1, -1):
            while stk and arr[stk[-1]] > arr[i]:
                stk.pop()

            if stk:
                out[i] = stk[-1]
            stk.append(i)

        return out

    def subarray_min_sum(self, arr):
        mins_sum = 0
        n = len(arr)

        nsl = self.next_small_left(arr, n)
        nsr = self.next_small_right(arr, n)

        for i in range(n):
            el = arr[i]
            l = nsl[i]
            r = nsr[i]

            subarrs = (i - l) * (r - i)
            prod = subarrs * el
            mins_sum += prod

        return mins_sum

    def next_greater_left(self, arr, n):
        out = [-1] * n
        stk = []

        for i in range(n):
            while stk and arr[stk[-1]] <= arr[i]:
                stk.pop()

            if stk:
                out[i] = stk[-1]
            stk.append(i)

        return out

    def next_greater_right(self, arr, n):
        out = [n] * n
        stk = []

        for i in range(n - 1, -1, -1):
            while stk and arr[stk[-1]] < arr[i]:
                stk.pop()

            if stk:
                out[i] = stk[-1]
            stk.append(i)

        return out

    def subarray_max_sum(self, arr):
        maxes_sum = 0
        n = len(arr)

        ngl = self.next_greater_left(arr, n)
        ngr = self.next_greater_right(arr, n)

        for i in range(n):
            el = arr[i]
            l = ngl[i]
            r = ngr[i]

            subarrs = (i - l) * (r - i)
            prod = el * subarrs
            maxes_sum += prod

        return maxes_sum

    def subarrayRanges(self, arr):
        # Code here
        # subarray_range = max(subarr) - min(subarr)
        # we have to return sum(subarray_range) for all subarrays
        # arr[] = [1, 2, 3]
        # count(e) ->
        # for how many subarrays element e is smallest
        # for how many subarrays element e is largest
        # arr[] = [1, 2, 3]
        # subarrays ->
        # [1]
        # [1,2]
        # [1,2,3]
        # [2]
        # [2,3]
        # [3]
        # count(1) = [3,1]
        # count(2) = [2,2]
        # count(3) = [1,3]
        # final answer would be
        # sum = [(1*1) + (2*2) + (3*3)] - [(1*3) + (2*2) + (3*1)]
        # = 14 - 10
        # = 4
        # find sum of elements that are greatest in subarray
        # find sum of elements that are smallest in subarray
        # return sum_greatest - sum_smallest

        sum_greatest = self.subarray_max_sum(arr)
        sum_smallest = self.subarray_min_sum(arr)

        subarray_range_sum = sum_greatest - sum_smallest

        return subarray_range_sum

        # Complexity Analysis
        # Time: O(N)
        # Space: O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Sum of subarray ranges - https://www.geeksforgeeks.org/problems/sum-of-subarray-ranges/1

    testcase = [
        [[1, 2, 3], 4],
        [[-32, 0, -2, 72], 318],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.subarrayRanges(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 22 of January 2026

    p1()

    p2()
