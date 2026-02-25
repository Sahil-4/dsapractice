from typing import List
from functools import cmp_to_key


class Solution1:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def comparator(num1, num2) -> int:
            count1 = num1.bit_count()
            count2 = num2.bit_count()
            if count1 != count2:
                return count1 - count2
            return num1 - num2

        sorted_arr = sorted(arr, key=cmp_to_key(comparator))
        return sorted_arr

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1356. Sort Integers by The Number of 1 Bits - https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/?envType=daily-question&envId=2026-02-25

    testcase = [
        [
            [0, 1, 2, 3, 4, 5, 6, 7, 8],
            [0, 1, 2, 4, 8, 3, 5, 6, 7],
        ],
        [
            [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],
            [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
        ],
    ]

    for line in testcase:
        [arr, expected] = line
        s1 = Solution1()
        result = s1.sortByBits(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def longestSubarray(self, arr, k):
        # Code Here

        N = len(arr)

        psumMap = dict()
        psum = 0

        llen = 0

        psumMap[0] = -1

        for i in range(N):
            psum += 1 if arr[i] > k else -1

            if psum > 0:
                llen = max(llen, i - 0 + 1)

            if (psum - 1) in psumMap:
                llen = max(llen, i - psumMap[psum - 1])

            if psum not in psumMap:
                psumMap[psum] = i

        return llen

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Longest Subarray with Majority Greater than K - https://www.geeksforgeeks.org/problems/longest-subarray-with-majority-greater-than-k/1

    testcase = [
        [[1, 2, 3, 4, 1], 2, 3],
        [[6, 5, 3, 4], 2, 4],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.longestSubarray(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 25 of February 2026

    p1()

    p2()
