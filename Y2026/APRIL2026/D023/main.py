from typing import List


class Solution1:
    def distance(self, nums: List[int]) -> List[int]:
        N = len(nums)

        arr = [0] * N

        index_sum = dict()
        index_count = dict()

        for i in range(N):
            _freq = index_count[nums[i]] if nums[i] in index_count else 0
            _sum = index_sum[nums[i]] if nums[i] in index_sum else 0

            arr[i] = _freq * i - _sum

            index_count[nums[i]] = index_count.get(nums[i], 0) + 1
            index_sum[nums[i]] = index_sum.get(nums[i], 0) + i

        index_count.clear()
        index_sum.clear()

        for i in range(N - 1, -1, -1):
            _freq = index_count[nums[i]] if nums[i] in index_count else 0
            _sum = index_sum[nums[i]] if nums[i] in index_sum else 0

            arr[i] += _sum - _freq * i

            index_count[nums[i]] = index_count.get(nums[i], 0) + 1
            index_sum[nums[i]] = index_sum.get(nums[i], 0) + i

        return arr

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2615. Sum of Distances - https://leetcode.com/problems/sum-of-distances/description/?envType=daily-question&envId=2026-04-23

    testcase = [
        [[1, 3, 1, 1, 2], [5, 0, 3, 4, 0]],
        [[0, 5, 3], [0, 0, 0]],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.distance(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def canSplit(self, arr: List[int]) -> bool:
        # code here

        tsum = sum(arr)

        if tsum & 1:
            return False

        target = tsum // 2

        curr_sum = 0
        for num in arr:
            curr_sum += num
            if curr_sum == target:
                return True

        return False

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Two Equal Sum Subarrays - https://www.geeksforgeeks.org/problems/split-an-array-into-two-equal-sum-subarrays/1

    testcase = [
        [[1, 2, 3, 4, 5, 5], True],
        [[4, 3, 2, 1], False],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.canSplit(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 23 of April 2026

    p1()

    p2()
