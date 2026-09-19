from math import sqrt


class Solution1:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:

        # find nearest point from x, or y
        def clamp(a1: int, a2: int, ac: int) -> int:
            if a1 > ac:
                return a1
            elif a2 < ac:
                return a2
            return ac

        xi = clamp(x1, x2, xCenter)
        yi = clamp(y1, y2, yCenter)

        # distance from center
        distance = sqrt(
            (xi - xCenter) * (xi - xCenter) + (yi - yCenter) * (yi - yCenter)
        )

        return distance <= radius

        # Complexity analysis
        # Time : O(1)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1401. Circle and Rectangle Overlapping - https://leetcode.com/problems/circle-and-rectangle-overlapping/description/?envType=daily-question&envId=2026-09-19

    testcase = [
        [1, 0, 0, 1, -1, 3, 1, True],
        [1, 1, 1, 1, -3, 2, -1, False],
        [1, 0, 0, -1, 0, 0, 1, True],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.checkOverlap(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findMinCost(self, s1: str, s2: str, costS1: int, costS2: int) -> int:
        # code here

        N1 = len(s1)
        N2 = len(s2)

        dp = [[0 for _ in range(N2 + 1)] for _ in range(N1 + 1)]

        for i1 in range(N1, -1, -1):
            for i2 in range(N2, -1, -1):

                cost = 0

                if i1 == N1:
                    cost = (N2 - i2) * costS2

                elif i2 == N2:
                    cost = (N1 - i1) * costS1

                elif s1[i1] == s2[i2]:
                    # match
                    cost = dp[i1 + 1][i2 + 1]

                else:
                    # no match - delete s1[i1]
                    option1 = costS1 + dp[i1 + 1][i2]

                    # no match - delete s2[i2]
                    option2 = costS2 + dp[i1][i2 + 1]

                    cost = min(option1, option2)

                dp[i1][i2] = cost

        return dp[0][0]

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(N * N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Min Cost To Make Two Strings Identical - https://www.geeksforgeeks.org/problems/minimum-cost-to-make-two-strings-identical1107/1

    testcase = [
        ["abcd", "acdb", 10, 20, 30],
        ["ef", "gh", 10, 20, 60],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.findMinCost(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def solveNQueens(self, N: int) -> list[list[str]]:
        solutions: list[list[str]] = []
        board = [["." for _ in range(N)] for _ in range(N)]

        def can_place(board: list[list[str]], row: int, col: int) -> bool:
            if row < 0 or row >= N:
                return False

            if col < 0 or col >= N:
                return False

            for i in range(N):
                # check horizontally and vertically
                if board[row][i] == "Q" or board[i][col] == "Q":
                    return False

                # check diagonally
                if row + i < N and col + i < N and board[row + i][col + i] == "Q":
                    return False
                if row - i >= 0 and col - i >= 0 and board[row - i][col - i] == "Q":
                    return False
                if row + i < N and col - i >= 0 and board[row + i][col - i] == "Q":
                    return False
                if row - i >= 0 and col + i < N and board[row - i][col + i] == "Q":
                    return False

            return True

        def helper(index: int, solution: list[list[str]]):
            if index == N:
                solutions.append(["".join(row) for row in solution])
                return

            # put a queen in row index
            # at all possible columns

            for c in range(N):
                if not can_place(solution, index, c):
                    continue

                solution[index][c] = "Q"
                helper(index + 1, solution)
                solution[index][c] = "."

        helper(0, board)

        return solutions

        # Complexity analysis
        # Time : O(N * N! + S(N) * N^2)
        # Space : O(N * N)


def p3():
    # Problem 3 : NC150 Leetcode 51. N-Queens - https://leetcode.com/problems/n-queens/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [4, [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]],
        [1, [["Q"]]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.solveNQueens(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 19 of September 2026

    p1()

    p2()

    p3()
