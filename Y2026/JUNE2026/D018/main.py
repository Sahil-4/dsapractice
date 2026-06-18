from typing import List


class Solution1:
    def angleClock(self, hour: int, minutes: int) -> float:
        T_HOURS = 12
        T_MINUTES = 60
        FULL_CIRCLE = 360

        MINUTE_DEGREES_PER_MINUTE = FULL_CIRCLE / T_MINUTES
        HOUR_DEGREES_PER_HOUR = FULL_CIRCLE / T_HOURS
        HOUR_DEGREES_PER_MINUTE = HOUR_DEGREES_PER_HOUR / T_MINUTES

        hour_angle = hour * HOUR_DEGREES_PER_HOUR + minutes * HOUR_DEGREES_PER_MINUTE
        minute_angle = minutes * MINUTE_DEGREES_PER_MINUTE

        angle_difference = abs(hour_angle - minute_angle)

        return min(
            angle_difference,
            FULL_CIRCLE - angle_difference,
        )

        # Complexity analysis
        # Time : O(1)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1344. Angle Between Hands of a Clock - https://leetcode.com/problems/angle-between-hands-of-a-clock/description/?envType=daily-question&envId=2026-06-18

    testcase = [
        [12, 30, 165],
        [3, 30, 75],
        [3, 15, 7.5],
    ]

    for line in testcase:
        [hour, minutes, expected] = line
        s1 = Solution1()
        result = s1.angleClock(hour, minutes)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findCoverage(self, mat: List[List[int]]) -> int:
        """
        DRY RUN

        given mat
        [
            [1, 1, 1, 0],
            [1, 0, 0, 1],
        ]

        initially coverage
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]

        left to right and right to left
        [
            [0, 0, 0, 1],
            [0, 2, 2, 0],
        ]

        top to bottom and bottom to top
        [
            [0, 0, 0, 2],
            [0, 3, 3, 0],
        ]

        total = 8
        """

        # code here
        N = len(mat)
        M = len(mat[0])

        coverage = [[0 for _ in range(M)] for _ in range(N)]

        # left to right and right to left
        for i in range(N):
            seen_1 = False
            for j in range(M):
                if mat[i][j] == 1:
                    seen_1 = True

                if mat[i][j] == 0:
                    coverage[i][j] += 1 if seen_1 else 0

            seen_1 = False
            for j in range(M - 1, -1, -1):
                if mat[i][j] == 1:
                    seen_1 = True

                if mat[i][j] == 0:
                    coverage[i][j] += 1 if seen_1 else 0

        # top to bottom and bottom to top
        for j in range(M):
            seen_1 = False
            for i in range(N):
                if mat[i][j] == 1:
                    seen_1 = True

                if mat[i][j] == 0:
                    coverage[i][j] += 1 if seen_1 else 0

            seen_1 = False
            for i in range(N - 1, -1, -1):
                if mat[i][j] == 1:
                    seen_1 = True

                if mat[i][j] == 0:
                    coverage[i][j] += 1 if seen_1 else 0

        coverage_sum = 0
        for i in range(N):
            for j in range(M):
                coverage_sum += coverage[i][j]

        return coverage_sum

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(N * M)


def p2():
    # Problem 2 : POTD Geeksforgeeks Coverage of all Zeros in a Binary Matrix - https://www.geeksforgeeks.org/problems/coverage-of-all-zeros-in-a-binary-matrix4024/1

    testcase = [
        [[[1, 1, 1, 0], [1, 0, 0, 1]], 8],
        [[[0, 1, 0], [0, 1, 1], [0, 0, 0]], 6],
        [[[0, 1]], 1],
    ]

    for line in testcase:
        [mat, expected] = line
        s2 = Solution2()
        result = s2.findCoverage(mat)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 18 of June 2026

    p1()

    p2()
