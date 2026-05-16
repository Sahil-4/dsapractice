from typing import List


class Solution1:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        l = 0
        r = N - 1

        ans = 0

        while l <= r:
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1

            mid = (l + r) // 2

            if nums[mid] < nums[ans]:
                ans = mid

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return nums[ans]

        # Complexity analysis
        # Time : O(Log(N)) or O(N) in worst case
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 154. Find Minimum in Rotated Sorted Array II - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/?envType=daily-question&envId=2026-05-16

    testcase = [
        [[1, 3, 5], 1],
        [[2, 2, 2, 0, 1], 0],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.findMin(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findSmallest(self, arr: list[int]) -> int:
        # code here

        # process smaller numbers first
        arr.sort()

        # can form sums [1, reach]
        reach = 0

        for x in arr:

            # gap -> reach + 1 cannot be formed
            if x > reach + 1:
                return reach + 1

            # extend reachable range
            reach += x

        # all sums till reach are possible
        return reach + 1

        # Complexity analysis
        # Time : O(N * logN)
        # Space : O(N) modify input


def p2():
    # Problem 2 : POTD Geeksforgeeks Not a subset sum - https://www.geeksforgeeks.org/problems/smallest-number-subset1220/1

    testcase = [
        [[3, 1, 2], 7],
        [[3, 10, 9, 6, 20, 28], 1],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.findSmallest(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 16 of May 2026

    p1()

    p2()
