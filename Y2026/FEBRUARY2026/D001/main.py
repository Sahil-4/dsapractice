from collections import deque
from typing import List


class Solution1:
    def minimumCost(self, nums: List[int]) -> int:
        # nums = [1,2,3,12]
        # [[1],[2],[3,12]]
        # nums = [10,3,1,1]
        # [[10,3],[1],[1]]
        # pick 0th index element and then next two smallest elements
        # this will be minimum total cost

        N = len(nums)

        tcost = nums[0]

        first_min = int(1e9)
        secon_min = int(1e9)

        for i in range(1, N):
            if nums[i] < first_min:
                secon_min = first_min
                first_min = nums[i]
            elif nums[i] < secon_min:
                secon_min = nums[i]

        tcost += first_min
        tcost += secon_min

        return tcost

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3010. Divide an Array Into Subarrays With Minimum Cost I - https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description/?envType=daily-question&envId=2026-02-01

    testcase = [
        [[1, 2, 3, 12], 6],
        [[5, 4, 3], 12],
        [[10, 3, 1, 1], 12],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.minimumCost(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxOfSubarrays(self, arr, k):
        # code here
        # use subarray, sliding window, and monotonic deque
        # add index of largest element in current window in beginning in monotonic deque
        # remove indices from deque if they are out of window
        # last element in monotonic deque will be current window min element index
        # run i = 0 to i < N
        # remove index of out of window elements
        # and elements which are smaller then current index element
        # add current element index
        # then use first element of monotonic stack as index of largest element in current window

        N = len(arr)

        subarray_max = []
        monotonic_dq = deque()

        for i in range(N):
            # remove out of window
            while len(monotonic_dq) and i - monotonic_dq[0] >= k:
                monotonic_dq.popleft()

            # make sure to keep it monotanic when ith index is added
            while len(monotonic_dq) and arr[monotonic_dq[-1]] <= arr[i]:
                monotonic_dq.pop()
            monotonic_dq.append(i)

            if i >= k - 1:
                # add subarray max element for current window
                subarray_max.append(arr[monotonic_dq[0]])

        return subarray_max

        # Complexity analysis
        # Time : O(2N)
        # Space : O(K)


def p2():
    # Problem 2 : POTD Geeksforgeeks K Sized Subarray Maximum - https://www.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1

    testcase = [
        [[1, 2, 3, 1, 4, 5, 2, 3, 6], 3, [3, 3, 4, 5, 5, 5, 6]],
        [[5, 1, 3, 4, 2], 1, [5, 1, 3, 4, 2]],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.maxOfSubarrays(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 1 of February 2026

    p1()

    p2()
