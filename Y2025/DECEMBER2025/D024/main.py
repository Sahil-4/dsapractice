from typing import List


class Solution1:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort()
        capacity.reverse()
        M = len(capacity)

        total_apples_count = sum(apple)
        total_boxes_count = 0

        while total_apples_count > 0 and total_boxes_count < M:
            total_apples_count -= capacity[total_boxes_count]
            total_boxes_count += 1

        return total_boxes_count

        # Complexity analysis
        # Time : O(M * Log(M))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3074. Apple Redistribution into Boxes - https://leetcode.com/problems/apple-redistribution-into-boxes/description/?envType=daily-question&envId=2025-12-24

    testcase = [
        [[1, 3, 2], [4, 3, 1, 5, 2], 2],
        [[5, 5, 5], [2, 4, 2, 7], 4],
    ]

    for line in testcase:
        [apple, capacity, expected] = line
        s1 = Solution1()
        result = s1.minimumBoxes(apple, capacity)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


from bisect import bisect_right


class Solution2:

    def find_pivot(self, arr):
        """
        Finds index of the smallest element (rotation point)
        Using binary search
        """
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid element is greater than last element,
            # pivot must be in right half
            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                # Pivot is at mid or in left half
                right = mid

        return left  # index of smallest element

    def countLessEqual(self, arr, x):
        # code here

        """
        Counts number of elements <= x in sorted rotated array
        """
        n = len(arr)
        if n == 0:
            return 0

        pivot = self.find_pivot(arr)
        count = 0

        # Left sorted part: arr[0 ... pivot-1]
        # Use bisect_right to count elements <= x
        if pivot > 0 and x >= arr[0]:
            count += bisect_right(arr, x, 0, pivot)

        # Right sorted part: arr[pivot ... n-1]
        if x >= arr[pivot]:
            count += bisect_right(arr, x, pivot, n) - pivot

        return count

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count elements less than or equal to k in a sorted rotated array - https://www.geeksforgeeks.org/problems/count-elements-less-than-or-equal-to-k-in-a-sorted-rotated-array/1

    testcase = [
        [[4, 5, 8, 1, 3], 6, 4],
        [[6, 10, 12, 15, 2, 4, 5], 14, 6],
    ]

    for line in testcase:
        [arr, x, expected] = line
        s2 = Solution2()
        result = s2.countLessEqual(arr, x)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 24 of December 2025

    p1()

    p2()
