from typing import List


class Solution1:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 153. Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=daily-question&envId=2026-05-15

    testcase = [
        [[3, 4, 5, 1, 2], 1],
        [[4, 5, 6, 7, 0, 1, 2], 0],
        [[11, 13, 15, 17], 11],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.findMin(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def optimalKeys(self, n: int) -> int:
        if n <= 6:
            return n

        screen = [0] * n

        for i in range(1, 7):
            screen[i - 1] = i

        for i in range(7, n + 1):
            screen[i - 1] = max(2 * screen[i - 4], 3 * screen[i - 5], 4 * screen[i - 6])

        return screen[n - 1]

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Special Keyboard - https://www.geeksforgeeks.org/problems/special-keyboard3018/1

    testcase = [
        [3, 3],
        [7, 9],
    ]

    for line in testcase:
        [n, expected] = line
        s2 = Solution2()
        result = s2.optimalKeys(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 15 of May 2026

    p1()

    p2()
