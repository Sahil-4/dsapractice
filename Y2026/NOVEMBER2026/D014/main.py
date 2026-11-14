import heapq


class Solution1:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        N = len(nums)

        min_sum = 100000000

        prefix_sum = [0] * (N + 1)
        for i in range(N):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        for s in range(l, r + 1):
            for i in range(N - s + 1):
                _sum = prefix_sum[i + s] - prefix_sum[i]

                if _sum > 0:
                    min_sum = min(min_sum, _sum)

        return min_sum if min_sum != 100000000 else -1

        # Complexity analysis
        # Time : O((R - L) * N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3364. Minimum Positive Sum Subarray - https://leetcode.com/problems/minimum-positive-sum-subarray/description/?envType=daily-question&envId=2026-11-14

    testcase = [
        [[3, -2, 1, 4], 2, 3, 1],
        [[-2, 2, -3, 1], 2, 3, -1],
        [[1, 2, 3, 4], 2, 4, 3],
        [[7, 3], 2, 2, 10],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minimumSumSubarray(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxEqualSum(self, s1: list[int], s2: list[int], s3: list[int]) -> int:
        # code here

        N1 = len(s1)
        N2 = len(s2)
        N3 = len(s3)

        sum1 = sum(s1)
        sum2 = sum(s2)
        sum3 = sum(s3)

        i1 = i2 = i3 = 0

        while i1 < N1 and i2 < N2 and i3 < N3:
            if sum1 == sum2 and sum2 == sum3:
                return sum1

            if sum1 >= sum2 and sum1 >= sum3:
                sum1 -= s1[i1]
                i1 += 1
            elif sum2 >= sum1 and sum2 >= sum3:
                sum2 -= s2[i2]
                i2 += 1
            elif sum3 >= sum1 and sum3 >= sum2:
                sum3 -= s3[i3]
                i3 += 1

        return 0

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Equal Sum in 3 Stacks - https://www.geeksforgeeks.org/problems/find-maximum-equal-sum-of-three-stacks/1

    testcase = [
        [[3, 2, 1, 1, 1], [4, 3, 2], [2, 5, 4, 1], 5],
        [[4, 7], [10], [1, 2, 3], 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxEqualSum(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        N = len(nums)

        min_heap: list[int] = []

        for i in range(N):
            heapq.heappush(min_heap, nums[i])

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return heapq.heappop(min_heap)

        # Complexity analysis
        # Time : O(N * Log(K))
        # Space : O(K)


def p3():
    # Problem 3 : NC150 Leetcode 215. Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[3, 2, 1, 5, 6, 4], 2, 5],
        [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.findKthLargest(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 14 of November 2026

    p1()

    p2()

    p3()
