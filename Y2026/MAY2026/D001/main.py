import heapq
from typing import List


class Solution1:
    def maxRotateFunction(self, nums: List[int]) -> int:
        N = len(nums)

        tsum = sum(nums)
        F = sum(i * num for i, num in enumerate(nums))

        max_weighted_sum = F

        for k in range(1, N):
            F = F + tsum - N * nums[N - k]
            max_weighted_sum = max(max_weighted_sum, F)

        return max_weighted_sum

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode  396. Rotate Function - https://leetcode.com/problems/rotate-function/description/?envType=daily-question&envId=2026-05-01

    testcase = [
        [[4, 3, 2, 6], 26],
        [[100], 0],
    ]

    for line in testcase:
        [arr, expected] = line
        s1 = Solution1()
        result = s1.maxRotateFunction(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def kthLargest(self, arr: List[int], k: int) -> List[int]:
        # code here

        kth_largest_stream = []

        heap = []

        for item in arr:
            heapq.heappush(heap, item)

            if len(heap) > k:
                heapq.heappop(heap)

            if len(heap) >= k:
                kth_largest_stream.append(heap[0])
            else:
                kth_largest_stream.append(-1)

        return kth_largest_stream

        # Complexity analysis
        # Time : O(N*Log(K))
        # Space : O(K)


def p2():
    # Problem 2 : POTD Geeksforgeeks Kth Largest in a Stream - https://www.geeksforgeeks.org/problems/kth-largest-element-in-a-stream2220/1

    testcase = [
        [[1, 2, 3, 4, 5, 6], 4, [-1, -1, -1, 1, 2, 3]],
        [[3, 2, 1, 3, 3], 2, [-1, 2, 2, 3, 3]],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.kthLargest(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 1 of May 2026

    p1()

    p2()
