from collections import deque
from functools import lru_cache


class Solution1:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        M = len(grid)
        N = len(grid[0])

        def cell_value(ri: int, ci: int) -> int:
            return 1 if grid[ri][ci] == "(" else -1

        @lru_cache(None)
        def helper(ri: int, ci: int, psum: int) -> bool:
            if ri == M - 1 and ci == N - 1:
                return psum == 0

            if psum < 0:
                return False

            check = False

            if not check and ci + 1 < N:
                # right
                check = helper(ri, ci + 1, psum + cell_value(ri, ci + 1))

            if not check and ri + 1 < M:
                # down
                check = helper(ri + 1, ci, psum + cell_value(ri + 1, ci))

            return check

        return helper(0, 0, cell_value(0, 0))

        # Complexity analysis
        # Time : O(2^(N + M))
        # Space : O(N + M)


def p1():
    # Problem 1 : POTD Leetcode 2267. Check if There Is a Valid Parentheses String Path - https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/description/?envType=daily-question&envId=2026-09-29

    testcase = [
        [[["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]], True],
        [[[")", ")"], ["(", "("]], False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.hasValidPath(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minStepToReachTarget(
        self, knightPos: list[int], targetPos: list[int], n: int
    ) -> int:
        # Code here

        # source/current - 0 based index
        x = knightPos[0] - 1
        y = knightPos[1] - 1

        # target - 0 based index
        tx = targetPos[0] - 1
        ty = targetPos[1] - 1

        # all 8 possible Knight moves
        MOVES = [
            [2, 1],
            [2, -1],
            [-2, 1],
            [-2, -1],
            [1, 2],
            [1, -2],
            [-1, 2],
            [-1, -2],
        ]

        # stores position and number of steps (xi, yi, steps)
        q = deque()

        # visited cells
        visited = [[False] * n for _ in range(n)]

        # Start BFS from the initial position
        q.append((x, y, 0))
        visited[x][y] = True

        while q:
            xi, yi, steps = q.popleft()

            # target is reached
            if xi == tx and yi == ty:
                return steps

            for move in MOVES:
                nx = xi + move[0]
                ny = yi + move[1]

                # if the new position is valid and unvisited
                if nx >= 0 and nx < n and ny >= 0 and ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True

                    # new position with updated steps
                    q.append((nx, ny, steps + 1))

        return -1

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(N * N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Min Steps by Knight - https://www.geeksforgeeks.org/problems/steps-by-knight5927/1

    testcase = [
        [[3, 3], [1, 2], 3, 1],
        [[1, 3], [5, 1], 6, 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minStepToReachTarget(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        M = len(matrix)
        N = len(matrix[0])

        # first row, column has 0
        first_row = first_col = False

        # check if first row has any 0 cell
        for c in range(N):
            first_row = matrix[0][c] == 0
            if first_row:
                break

        # check if first col has any 0 cell
        for r in range(M):
            first_col = matrix[r][0] == 0
            if first_col:
                break

        # mark first row, col cell 0 if cell is zero
        for r in range(M):
            for c in range(N):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # if any first row, col contains 0 make its col, row 0
        for r in range(1, M):
            for c in range(1, N):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # mark first row all cells 0 if first row is 0
        for c in range(N):
            if not first_row:
                break
            matrix[0][c] = 0

        # mark first col all cells 0 if first col is 0
        for r in range(M):
            if not first_col:
                break
            matrix[r][0] = 0

        return

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
        ],
        [
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        s3.setZeroes(*inputs)
        result = inputs[0]
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 29 of September 2026

    p1()

    p2()

    p3()
