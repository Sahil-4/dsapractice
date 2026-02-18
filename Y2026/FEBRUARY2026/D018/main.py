from typing import List


class Solution1:
    def hasAlternatingBits(self, n: int) -> bool:
        prev_bit = -1

        while n > 0:
            bit = n & 1
            if bit == prev_bit:
                return False
            prev_bit = bit
            n = n >> 1

        return True

        # Complexity analysis
        # Time : O(32)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 693. Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/description/?envType=daily-question&envId=2026-02-18

    testcase = [
        [5, True],
        [7, False],
        [11, False],
    ]

    for line in testcase:
        [n, expected] = line
        s1 = Solution1()
        result = s1.hasAlternatingBits(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def merge_and_count(self, arr: List[int], left: int, mid: int, right: int):
        left_half = arr[left : mid + 1]
        right_half = arr[mid + 1 : right + 1]

        i = 0  # left half iterator
        j = 0  # right half iterator
        k = left  # merged array iterator
        inversions = 0  # inversions count

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                # inversion found: all remaining elements in the left half
                # are greater than the current element in the right half
                arr[k] = right_half[j]
                j += 1
                inversions += len(left_half) - i
            k += 1

        # copy remaining elements of left_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # copy remaining elements of right_half, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        return inversions

    def count_inversions_merge_sort(self, arr: List[int], left: int, right: int):
        inversions = 0

        if left < right:
            mid = (left + right) // 2
            # inversions in left, right subarrays, and during merge
            inversions += self.count_inversions_merge_sort(arr, left, mid)
            inversions += self.count_inversions_merge_sort(arr, mid + 1, right)
            inversions += self.merge_and_count(arr, left, mid, right)

        return inversions

    def inversionCount(self, arr: List[int]) -> int:
        # Code Here
        # merge sort algorithm

        N = len(arr)
        return self.count_inversions_merge_sort(arr, 0, N - 1)
        
        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count Inversions - https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1

    testcase = [
        [[2, 4, 1, 3, 5], 3],
        [[2, 3, 4, 5, 6], 0],
        [[10, 10, 10], 0],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.inversionCount(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 18 of February 2026

    p1()

    p2()
