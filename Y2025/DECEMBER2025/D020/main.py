from typing import List
import math


class Solution1:
    def minDeletionSize(self, strs: List[str]) -> int:
        deletions = 0

        str_len = len(strs[0])
        N = len(strs)

        for j in range(str_len):
            prev = chr(97)
            for i in range(N):
                if strs[i][j] < prev:
                    deletions += 1
                    break
                prev = strs[i][j]

        return deletions

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 944. Delete Columns to Make Sorted - https://leetcode.com/problems/delete-columns-to-make-sorted/description/?envType=daily-question&envId=2025-12-20

    testcase = [
        [["cba", "daf", "ghi"], 1],
        [["zyx", "wvu", "tsr"], 3],
        [["a", "b"], 0],
        [["a", "b", "b"], 0],
        [["b", "b", "a"], 1],
    ]

    for line in testcase:
        [strs, expected] = line
        s1 = Solution1()
        result = s1.minDeletionSize(strs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def searchInsertK(self, arr, k):
        # code here
        N = len(arr)
        low = 0
        high = N - 1
        ans = N

        while low <= high:
            mid = math.floor(low + (high - low) / 2)

            if arr[mid] >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks  Search insert position of K in a sorted array - https://www.geeksforgeeks.org/problems/search-insert-position-of-k-in-a-sorted-array/1

    testcase = [
        [[1, 3, 5, 6], 5, 2],
        [[1, 3, 5, 6], 2, 1],
        [[2, 6, 7, 10, 14], 15, 5],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.searchInsertK(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 20 of December 2025

    p1()

    p2()
