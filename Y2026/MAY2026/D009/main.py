from typing import List


class Solution1:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M = len(grid)
        N = len(grid[0])

        grid_copy = [row[:] for row in grid]

        for i in range(min(M, N) // 2):
            start_row = i
            start_col = i

            end_row = M - 1 - i
            end_col = N - 1 - i

            perimeter = (2 * (end_row - start_row + end_col - start_col + 2)) - 4
            _k = k % perimeter

            for _ in range(_k):
                curr_row = start_row
                curr_col = start_col
                prev_el = grid_copy[start_row][start_col + 1]

                # top -> bottom
                while curr_row <= end_row:
                    curr = grid_copy[curr_row][curr_col]
                    grid_copy[curr_row][curr_col] = prev_el
                    prev_el = curr
                    curr_row += 1
                curr_row -= 1
                curr_col += 1

                # left -> right
                while curr_col <= end_col:
                    curr = grid_copy[curr_row][curr_col]
                    grid_copy[curr_row][curr_col] = prev_el
                    prev_el = curr
                    curr_col += 1
                curr_col -= 1
                curr_row -= 1

                # bottom -> top
                while curr_row >= start_row:
                    curr = grid_copy[curr_row][curr_col]
                    grid_copy[curr_row][curr_col] = prev_el
                    prev_el = curr
                    curr_row -= 1
                curr_row += 1
                curr_col -= 1

                # right -> left
                while curr_col >= start_col:
                    curr = grid_copy[curr_row][curr_col]
                    grid_copy[curr_row][curr_col] = prev_el
                    prev_el = curr
                    curr_col -= 1

        return grid_copy

        # Complexity analysis
        # Time : O(N * NM * NM)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1914. Cyclically Rotating a Grid - https://leetcode.com/problems/cyclically-rotating-a-grid/description/?envType=daily-question&envId=2026-05-09

    testcase = [
        [
            [[40, 10], [30, 20]],
            1,
            [[10, 20], [40, 30]],
        ],
        [
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            2,
            [[3, 4, 8, 12], [2, 11, 10, 16], [1, 7, 6, 15], [5, 9, 13, 14]],
        ],
        [
            [
                [9, 1, 7, 7, 8, 4, 5, 10, 4, 5, 3, 9, 10, 9, 5, 2],
                [2, 3, 1, 8, 7, 1, 10, 9, 4, 6, 2, 1, 9, 7, 7, 2],
                [7, 3, 9, 9, 9, 8, 8, 10, 7, 10, 1, 10, 1, 7, 10, 4],
                [10, 4, 2, 3, 6, 5, 9, 7, 7, 5, 5, 8, 5, 1, 5, 2],
                [2, 9, 7, 6, 3, 7, 9, 1, 8, 2, 6, 10, 3, 3, 6, 8],
                [1, 4, 5, 6, 4, 8, 1, 7, 7, 5, 2, 2, 4, 4, 8, 9],
                [10, 7, 10, 9, 7, 4, 4, 4, 6, 9, 7, 6, 6, 10, 7, 10],
                [10, 4, 8, 8, 6, 6, 9, 3, 9, 6, 4, 6, 1, 7, 10, 1],
                [4, 9, 5, 7, 9, 3, 9, 3, 10, 6, 2, 10, 7, 1, 6, 9],
                [3, 4, 1, 10, 7, 2, 9, 1, 3, 2, 4, 6, 8, 3, 2, 6],
            ],
            5,
            [
                [4, 5, 10, 4, 5, 3, 9, 10, 9, 5, 2, 2, 4, 2, 8, 9],
                [8, 10, 9, 4, 6, 2, 1, 9, 7, 7, 10, 5, 6, 8, 7, 10],
                [7, 1, 10, 7, 10, 1, 10, 1, 7, 1, 3, 4, 10, 7, 10, 1],
                [7, 7, 8, 7, 5, 5, 8, 5, 3, 4, 6, 6, 7, 1, 6, 9],
                [1, 8, 8, 7, 2, 6, 10, 2, 2, 5, 7, 7, 9, 6, 1, 6],
                [9, 1, 9, 9, 8, 1, 9, 7, 3, 4, 8, 1, 6, 4, 7, 2],
                [2, 3, 9, 5, 6, 3, 6, 6, 9, 7, 4, 4, 4, 6, 10, 3],
                [7, 3, 9, 2, 7, 5, 10, 8, 8, 6, 6, 9, 3, 9, 2, 8],
                [10, 4, 9, 4, 7, 4, 9, 5, 7, 9, 3, 9, 3, 10, 6, 6],
                [2, 1, 10, 10, 4, 3, 4, 1, 10, 7, 2, 9, 1, 3, 2, 4],
            ],
        ],
    ]

    for line in testcase:
        [grid, k, expected] = line
        s1 = Solution1()
        result = s1.rotateGrid(grid, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countSpanTree(self, n: int, edges: List[List[int]]) -> int:
        # code here

        # Special case
        if n == 1:
            return 1

        # Laplacian matrix
        lap = [[0] * n for _ in range(n)]

        for u, v in edges:
            lap[u][u] += 1
            lap[v][v] += 1

            lap[u][v] -= 1
            lap[v][u] -= 1

        # cofactor matrix - remove last row and last column
        mat = [row[:-1] for row in lap[:-1]]

        # determinant - using Gaussian elimination
        size = n - 1
        det = 1.0

        for i in range(size):
            pivot = i

            # find non-zero pivot
            while pivot < size and abs(mat[pivot][i]) < 1e-9:
                pivot += 1

            if pivot == size:
                return 0

            # swap rows
            if pivot != i:
                mat[i], mat[pivot] = mat[pivot], mat[i]
                det *= -1

            pivot_val = mat[i][i]
            det *= pivot_val

            # normalize row
            for j in range(i + 1, size):
                factor = mat[j][i] / pivot_val

                for k in range(i, size):
                    mat[j][k] -= factor * mat[i][k]

        return round(det)

        # Complexity analysis
        # Time : O(N^3)
        # Space : O(N^2)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count Spanning Trees in a Graph - https://www.geeksforgeeks.org/problems/total-number-of-spanning-trees-in-a-graph/1

    testcase = [
        [6, [[0, 3], [0, 1], [1, 2], [1, 5], [3, 4]], 1],
        [3, [[0, 1], [0, 2], [1, 2]], 3],
        [1, [], 1],
    ]

    for line in testcase:
        [n, edges, expected] = line
        s2 = Solution2()
        result = s2.countSpanTree(n, edges)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 9 of May 2026

    p1()

    p2()
