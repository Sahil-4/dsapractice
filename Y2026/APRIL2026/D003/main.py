from bisect import bisect_left, bisect_right
from typing import List


class Solution1:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)

        # Sort robots with distances
        robot_dist = sorted(zip(robots, distance))
        walls.sort()

        r = [x[0] for x in robot_dist]
        d = [x[1] for x in robot_dist]

        # Precompute counts
        left = [0] * n
        right = [0] * n
        num = [0] * n  # walls between i-1 and i

        def count(l, r):
            return bisect_right(walls, r) - bisect_left(walls, l)

        for i in range(n):
            # LEFT interval
            L = r[i] - d[i]
            if i > 0:
                L = max(L, r[i - 1] + 1)
            left[i] = count(L, r[i])

            # RIGHT interval
            R = r[i] + d[i]
            if i < n - 1:
                R = min(R, r[i + 1] - 1)
            right[i] = count(r[i], R)

            # walls between robots
            if i > 0:
                num[i] = count(r[i - 1], r[i])

        # DP - state compression
        sub_left = left[0]
        sub_right = right[0]

        for i in range(1, n):
            # shoots LEFT
            current_left = max(
                sub_left + left[i],
                sub_right - right[i - 1] + min(left[i] + right[i - 1], num[i]),
            )

            # shoots RIGHT
            current_right = max(sub_left + right[i], sub_right + right[i])

            sub_left, sub_right = current_left, current_right

        return max(sub_left, sub_right)

        # Complexity analysis
        # Time : O(N * Log(N) + M * Log(M))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3661. Maximum Walls Destroyed by Robots - https://leetcode.com/problems/maximum-walls-destroyed-by-robots/description/?envType=daily-question&envId=2026-04-03

    testcase = [
        [[4], [3], [1, 10], 1],
        [[10, 2], [5, 1], [5, 2, 7], 3],
        [[1, 2], [100, 1], [10], 0],
        [
            [
                63,
                56,
                40,
                45,
                4,
                9,
                44,
                69,
                55,
                26,
                73,
                15,
                12,
                60,
                43,
                39,
                37,
                74,
                36,
                34,
                13,
                23,
                66,
                14,
                11,
                42,
                72,
                3,
                57,
                10,
                53,
                8,
                70,
                17,
                58,
                61,
                30,
                32,
            ],
            [
                8,
                7,
                4,
                8,
                9,
                5,
                2,
                4,
                5,
                2,
                6,
                9,
                5,
                9,
                5,
                3,
                7,
                6,
                9,
                2,
                8,
                7,
                4,
                3,
                5,
                1,
                7,
                5,
                1,
                3,
                5,
                3,
                5,
                4,
                8,
                7,
                6,
                4,
            ],
            [6, 22, 50, 52, 20, 9, 23, 75, 26, 21, 60, 58, 41, 28, 30],
            15,
        ],
    ]

    for line in testcase:
        [robots, distance, walls, expected] = line
        s1 = Solution1()
        result = s1.maxWalls(robots, distance, walls)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:

    def diagView(self, mat):
        N = len(mat)
        result = []

        for d in range(2 * N - 1):
            for i in range(N):
                j = d - i

                if 0 <= j < N:
                    result.append(mat[i][j])

        return result

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Print Diagonally - https://www.geeksforgeeks.org/problems/print-diagonally4331/1

    testcase = [
        [
            2,
            [[1, 2], [3, 4]],
            [1, 2, 3, 4],
        ],
        [
            3,
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [1, 2, 4, 3, 5, 7, 6, 8, 9],
        ],
    ]

    for line in testcase:
        [N, mat, expected] = line
        s = Solution2()
        result = s.diagView(mat)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 3 of April 2026

    p1()

    p2()
