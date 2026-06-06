from typing import List


class Solution1:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        N = len(nums)

        difference = [-1] * N

        leftSum = 0
        rightSum = sum(nums)

        for i in range(N):
            rightSum -= nums[i]

            difference[i] = abs(leftSum - rightSum)

            leftSum += nums[i]

        return difference

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2574. Left and Right Sum Differences - https://leetcode.com/problems/left-and-right-sum-differences/description/?envType=daily-question&envId=2026-06-06

    testcase = [
        [[10, 4, 8, 3], [15, 1, 11, 22]],
        [[1], [0]],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.leftRightDifference(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def numOfWays(self, n: int, m: int) -> int:
        # code here

        delta = [
            (-2, 1),
            (-1, 2),
            (1, 2),
            (2, 1),
        ]

        total_ways = (m * n) * ((m * n) - 1)
        invalid_ways = 0

        for i in range(n):
            for j in range(m):
                for dx, dy in delta:
                    x = i + dx
                    y = j + dy

                    if 0 <= x < n and 0 <= y < m:
                        invalid_ways += 2

        return total_ways - invalid_ways

        # Complexity analysis
        # Time : O(N*M)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Non-Attacking Black and White Knights - https://www.geeksforgeeks.org/problems/black-and-white-1587115620/1

    testcase = [
        [2, 2, 12],
        [2, 3, 26],
    ]

    for line in testcase:
        [n, m, expected] = line
        s2 = Solution2()
        result = s2.numOfWays(n, m)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 6 of June 2026

    p1()

    p2()
