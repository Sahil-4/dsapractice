from typing import List
from collections import deque


class Solution1:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # points = [[1,1],[3,4],[-1,0]]
        # d([1,1],[3,4]) = 3
        # d([3,4],[-1,0]) = 4
        # take adjacent points
        # calculate absolute distance between x axis
        # and distance between y axis
        # whichever is maximum add that into time_sum
        # at last return time_sum

        time_sum = 0

        N = len(points)

        for i in range(1, N):
            point1 = points[i - 1]
            point2 = points[i]

            dx = abs(point2[0] - point1[0])
            dy = abs(point2[1] - point1[1])

            time_sum += max(dx, dy)

        return time_sum

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1266. Minimum Time Visiting All Points - https://leetcode.com/problems/minimum-time-visiting-all-points/?envType=daily-question&envId=2026-01-12

    testcase = [
        [[[1, 1], [3, 4], [-1, 0]], 7],
        [[[3, 2], [-2, 2]], 5],
    ]

    for line in testcase:
        [points, expected] = line
        s1 = Solution1()
        result = s1.minTimeToVisitAllPoints(points)
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
    # Day 12 of January 2026

    p1()

    p2()
