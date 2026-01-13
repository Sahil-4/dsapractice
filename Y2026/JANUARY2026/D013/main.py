import math
from typing import List


class Solution1:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # divide total area of squares on graph into two parts upper and lower
        # on this use binary search to find out the point y on which
        # the difference between upper and lower area is minimum

        BOUND = 0.00001  # 1e-5
        low = 0.0
        high = 1000000000.0

        def is_upper_area_greater(mid: float) -> bool:
            upper_area = 0.0
            lower_area = 0.0

            for square in squares:
                yi = square[1]
                li = square[2]

                if yi >= mid:
                    upper_area += (float)(li * li)
                elif yi + li <= mid:
                    lower_area += (float)(li * li)
                else:
                    lower_area += (float)(li * (mid - yi))
                    upper_area += (float)(li * (li + yi - mid))

            return upper_area > lower_area

        while high - low >= BOUND:
            mid = (low + high) / 2

            if is_upper_area_greater(mid):
                low = mid
            else:
                high = mid

        return low

        # Complexity analysis
        # Time : O(Log(E) * N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3453. Separate Squares I - https://leetcode.com/problems/separate-squares-i/description/?envType=daily-question&envId=2026-01-13

    BOUND = 0.00001  # 1e-5
    testcase = [
        [[[0, 0, 1], [2, 2, 1]], 1.00000],
        [[[0, 0, 2], [1, 1, 1]], 1.16667],
    ]

    for line in testcase:
        [squares, expected] = line
        s1 = Solution1()
        result = s1.separateSquares(squares)
        assert math.isclose(
            result, expected, rel_tol=BOUND, abs_tol=BOUND
        ), f"Test failed: expected {expected}, got {result}"

        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def canServe(self, arr):
        # code here
        # notes = [5, 10, 20]
        # initially all are 0
        # notes = {5: 0, 10: 0, 20: 0}
        # ticket_cost = 5
        # there are 3 possible cases
        # a passenger comes with
        # 1. note of 5
        # 2. note of 10
        # 3. note of 20
        # in case 1 we just increase count of note of 5
        # in case 2 we have to return note of 5
        # then decrement count of note of 5 and increment count of note of 10
        # in case 3 we have to return note of 10 and 5 or 5 and 5 and 5
        # and then decrement returned notes count and increment count of note of 20
        # use coin exchange algorithm (provide largest coins first) instead of multiple if else conditions

        N = len(arr)
        ticket_cost = 5
        notes = {5: 0, 10: 0, 20: 0}

        for i in range(N):
            note = arr[i] - 5
            while note >= 10 and notes[10] >= 1:
                notes[10] -= 1
                note -= 10
            while note >= 5 and notes[5] >= 1:
                notes[5] -= 1
                note -= 5
            if note != 0:
                return False
            notes[arr[i]] += 1

        return True

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Bus Ticket Change - https://www.geeksforgeeks.org/problems/lemonade-change/1

    testcase = [
        [[5, 5, 5, 10, 20], True],
        [[5, 5, 10, 10, 20], False],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.canServe(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 13 of January 2026

    p1()

    p2()
