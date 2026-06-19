from typing import List


class Solution1:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        starting from 0
        going forward altitude changes with +alt
        -100 <= alt <= 100

        start with 0
        going forward keep updating the altitude
        at every point calculate highest altitude point

        finally return the highest altitude point
        """

        h_alt = 0
        curr_alt = 0

        for alt_gain in gain:
            curr_alt += alt_gain
            h_alt = max(h_alt, curr_alt)

        return h_alt

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1732. Find the Highest Altitude - https://leetcode.com/problems/find-the-highest-altitude/description/?envType=daily-question&envId=2026-06-19

    testcase = [
        [[-5, 1, 5, 0, -7], 1],
        [[-4, -3, -2, -1, 4, 3, 2], 0],
    ]

    for line in testcase:
        [gain, expected] = line
        s1 = Solution1()
        result = s1.largestAltitude(gain)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def optimalArray(self, arr: List[int]) -> List[int]:
        # code here
        N = len(arr)
        min_operations = []

        # for i in range(N):
        #     mid = i // 2

        #     operations = 0
        #     for j in range(i + 1):
        #         operations += abs(arr[j] - arr[mid])

        #     min_operations.append(operations)

        # return min_operations

        # for i = 0
        min_operations.append(0)

        for i in range(1, N):
            mid = i // 2
            min_operations.append(min_operations[-1] + arr[i] - arr[mid])

        return min_operations

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Equalize All Prefix Sums - https://www.geeksforgeeks.org/problems/optimal-array--170647/1

    testcase = [
        [[1, 6, 9, 12], [0, 5, 8, 14]],
        [[1, 1, 1, 7, 7, 10, 19], [0, 0, 0, 6, 12, 21, 33]],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.optimalArray(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 19 of June 2026

    p1()

    p2()
