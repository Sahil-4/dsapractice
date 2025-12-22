from bisect import bisect_left
from typing import List


class Solution1:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])

        # dp[i] = length of LIS ending at column i
        dp = [1] * cols
        LIS = 1

        # Khandani LIS Pattern
        for i in range(cols):
            for j in range(i):
                valid = True
                for k in range(rows):
                    if strs[k][j] > strs[k][i]:
                        valid = False
                        break

                if valid:
                    dp[i] = max(dp[i], dp[j] + 1)

            LIS = max(LIS, dp[i])

        return cols - LIS

        # Complexity analysis
        # Time : O(N*M*M)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 960. Delete Columns to Make Sorted III - https://leetcode.com/problems/delete-columns-to-make-sorted-iii/description/?envType=daily-question&envId=2025-12-22

    testcase = []

    for line in testcase:
        [strs, expected] = line
        s1 = Solution1()
        result = s1.minDeletionSize(strs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def rowWithMax1s(self, arr):
        # code here
        # row is sorted
        # hence whichever row has 1 on lowest index
        # that will be answer
        # use binary search to find first occurrence of 1 in each row
        # and finally return the min index
        # more better use left-down walk
        # start from top right
        # if found 1 move left
        # if found 0 move right

        # [
        # [0,1,1,1],
        # [0,0,1,1],
        # [1,1,1,1],
        # [0,0,0,0],
        # ]

        n = len(arr)
        m = len(arr[0])

        row = 0
        col = m - 1
        ans = -1

        while row < n and col >= 0:
            if arr[row][col] == 1:
                ans = row  # better row found
                col -= 1  # move left
            else:
                row += 1  # move down

        return ans

        # Complexity analysis
        # Time : O(N + M)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Row with max 1s - https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1

    testcase = [
        [[[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]], 2],
        [[[0, 0], [1, 1]], 1],
        [[[0, 0], [0, 0]], -1],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.rowWithMax1s(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 22 of December 2025

    p1()

    p2()
