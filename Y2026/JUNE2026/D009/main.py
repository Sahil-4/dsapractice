from typing import List


class Solution1:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        v1 = min(nums)
        v2 = max(nums)

        return (v2 - v1) * k

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3689. Maximum Total Subarray Value I - https://leetcode.com/problems/maximum-total-subarray-value-i/description/?envType=daily-question&envId=2026-06-09

    testcase = [
        [[1, 3, 2], 2, 4],
        [[4, 2, 5, 1], 3, 12],
    ]

    for line in testcase:
        [nums, k, expected] = line
        s1 = Solution1()
        result = s1.maxTotalValue(nums, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def canSeatAllPeople(self, k: int, seats: List[int]) -> bool:
        N = len(seats)

        # Pass 1: validate no two pre-existing occupied seats are adjacent
        for i in range(N - 1):
            if seats[i] == 1 and seats[i + 1] == 1:
                return False

        # Pass 2: greedy placement of k additional people
        available_seats = 0
        i = 0
        while i < N:
            prev = seats[i - 1] if i > 0 else 0
            nxt = seats[i + 1] if i < N - 1 else 0

            if seats[i] == 0 and prev == 0 and nxt == 0:
                seats[i] = 1
                available_seats += 1
                i += 2
            else:
                i += 1

        return available_seats >= k

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Seating Arrangement - https://www.geeksforgeeks.org/problems/seating-arrangement--170647/1

    testcase = [
        [2, [0, 0, 1, 0, 0, 0, 1], True],
        [1, [0, 1, 0], False],
        [0, [1, 1, 1, 0], False],
        [0, [1, 0, 1], True],
        [3, [0, 0, 0, 0, 0], True],
        [4, [0, 0, 0, 0, 0], False],
    ]

    for line in testcase:
        [k, seats, expected] = line
        s2 = Solution2()
        result = s2.canSeatAllPeople(k, seats)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 9 of June 2026

    p1()

    p2()
