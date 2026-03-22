from typing import List


class Solution1:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # there can only be three cases
        # rotate +90 -> [0 times, 1 times, 2 times, 3 times]

        N = len(mat)

        for _ in range(4):
            equal = True

            for i in range(N):
                for j in range(N):
                    if mat[i][j] != target[i][j]:
                        equal = False
                        break

                if not equal:
                    break

            if equal:
                return True

            # rotate +90
            for i in range(N):
                for j in range(i, N):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            for i in range(N):
                for j in range(N // 2):
                    mat[i][j], mat[i][N - 1 - j] = mat[i][N - 1 - j], mat[i][j]

        return False

        # Complexity analysis
        # Time : O(2 * N*M)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1886. Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description/?envType=daily-question&envId=2026-03-22

    testcase = [
        [
            [[0, 1], [1, 0]],
            [[1, 0], [0, 1]],
            True,
        ],
        [
            [[0, 1], [1, 1]],
            [[1, 0], [0, 1]],
            False,
        ],
        [
            [[0, 0, 0], [0, 1, 0], [1, 1, 1]],
            [[1, 1, 1], [0, 1, 0], [0, 0, 0]],
            True,
        ],
    ]

    for line in testcase:
        [mat, target, expected] = line
        s1 = Solution1()
        result = s1.findRotation(mat, target)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def orangesRot(self, mat):
        # code here
        N = len(mat)
        M = len(mat[0])

        __directions = [[-1, 0], [0, +1], [+1, 0], [0, -1]]

        def is_valid_cell_index(r, c) -> bool:
            return (r >= 0 and r < N) and (c >= 0 and c < M)

        copy_grid = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                copy_grid[i][j] = mat[i][j]

        time_grid = [[0.0 for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                time_grid[i][j] = float("inf") if mat[i][j] == 1 else 0

        stack = []
        for i in range(N):
            for j in range(M):
                if copy_grid[i][j] == 2:
                    stack.append((i, j, 0))

        while stack:
            x, y, t = stack.pop()

            for dx, dy in __directions:
                new_x = x + dx
                new_y = y + dy
                new_t = t + 1

                if (
                    is_valid_cell_index(new_x, new_y)
                    and copy_grid[new_x][new_y] != 0
                    and time_grid[new_x][new_y] > new_t
                ):
                    copy_grid[new_x][new_y] = 2
                    time_grid[new_x][new_y] = new_t
                    stack.append((new_x, new_y, new_t))

        for i in range(N):
            for j in range(M):
                if copy_grid[i][j] == 1:
                    return -1

        mtime = 0
        for i in range(N):
            for j in range(M):
                mtime = max(mtime, time_grid[i][j])

        return mtime

        # Complexity analysis
        # Time : O(6 * N*M)
        # Space : O(3 * N*M)


def p2():
    # Problem 2 : POTD Geeksforgeeks Rotten Oranges - https://www.geeksforgeeks.org/problems/rotten-oranges2536/1

    testcase = [
        [
            [[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]],
            2,
        ],
        [
            [[2, 1, 0, 2, 1], [0, 0, 1, 2, 1], [1, 0, 0, 2, 1]],
            -1,
        ],
    ]

    for line in testcase:
        [mat, expected] = line
        s2 = Solution2()
        result = s2.orangesRot(mat)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 22 of March 2026

    p1()

    p2()
