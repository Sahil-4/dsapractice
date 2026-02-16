from typing import List
from operator import itemgetter


class Solution1:
    def reverseBits(self, n: int) -> int:
        # take out bit one by one from last (LSB)
        # put it in result
        # take from back, shift to right
        # insert at back, shift to left and update last bit with MASK

        result = 0
        iter = 32

        while n > 0 or iter > 0:
            bit = n & 1
            n = n >> 1

            result = result << 1
            result = result | bit

            iter -= 1

        return result

        # Complexity analysis
        # Time : O(32)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 190. Reverse Bits - https://leetcode.com/problems/reverse-bits/description/?envType=daily-question&envId=2026-02-16

    testcase = [
        [43261596, 964176192],
        [2147483644, 1073741822],
        [12, 805306368],
    ]

    for line in testcase:
        [n, expected] = line
        s1 = Solution1()
        result = s1.reverseBits(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def canAttend(self, arr: List[List[int]]) -> bool:
        # Code Here
        # meetings time should be sorted by end time in ASC order
        # a meeting can be attended only
        # if prev meeting end time is LTE
        # then current meeting start time
        # initially prev meeting end time will be -1

        arr = sorted(arr, key=itemgetter(1, 0))

        prev_end = -1

        for time in arr:
            [start, end] = time

            if start < prev_end:
                return False

            prev_end = end

        return True

        # Complexity analysis
        # Time : O(N * Log(N)) + O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Meeting Rooms - https://www.geeksforgeeks.org/problems/attend-all-meetings/1

    testcase = [
        [[[1, 4], [10, 15], [7, 10]], True],
        [[[2, 4], [9, 12], [6, 10]], False],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.canAttend(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 16 of February 2026

    p1()

    p2()
