from typing import List


class Solution1:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Row-wise prefix sum
        row_cumsum = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            row_cumsum[i][0] = grid[i][0]
            for j in range(1, cols):
                row_cumsum[i][j] = row_cumsum[i][j - 1] + grid[i][j]

        # Column-wise prefix sum
        col_cumsum = [[0] * cols for _ in range(rows)]
        for j in range(cols):
            col_cumsum[0][j] = grid[0][j]
            for i in range(1, rows):
                col_cumsum[i][j] = col_cumsum[i - 1][j] + grid[i][j]

        # Try largest square first
        for side in range(min(rows, cols), 1, -1):
            for i in range(rows - side + 1):
                for j in range(cols - side + 1):

                    target_sum = row_cumsum[i][j + side - 1] - (
                        row_cumsum[i][j - 1] if j > 0 else 0
                    )

                    all_same = True

                    # Check rows
                    for r in range(i + 1, i + side):
                        row_sum = row_cumsum[r][j + side - 1] - (
                            row_cumsum[r][j - 1] if j > 0 else 0
                        )
                        if row_sum != target_sum:
                            all_same = False
                            break
                    if not all_same:
                        continue

                    # Check columns
                    for c in range(j, j + side):
                        col_sum = col_cumsum[i + side - 1][c] - (
                            col_cumsum[i - 1][c] if i > 0 else 0
                        )
                        if col_sum != target_sum:
                            all_same = False
                            break
                    if not all_same:
                        continue

                    # Check diagonals
                    diag = anti_diag = 0
                    for k in range(side):
                        diag += grid[i + k][j + k]
                        anti_diag += grid[i + k][j + side - 1 - k]

                    if diag == target_sum and anti_diag == target_sum:
                        return side

        return 1

        # Complexity analysis
        # Time : O(N * M * min(N, M))
        # Space : O(2 * N * M)


def p1():
    # Problem 1 : POTD Leetcode 1895. Largest Magic Square - https://leetcode.com/problems/largest-magic-square/description/?envType=daily-question&envId=2026-01-18

    testcase = [
        [[[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]], 3],
        [[[5, 1, 3, 1], [9, 3, 3, 1], [1, 3, 3, 8]], 2],
    ]

    for line in testcase:
        [grid, expected] = line
        s1 = Solution1()
        result = s1.largestMagicSquare(grid)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def nextFreqGreater(self, arr):
        # code here
        frequency = dict()
        for e in arr:
            if e not in frequency:
                frequency[e] = 0
            frequency[e] += 1

        N = len(arr)
        monotonic_stack = []
        answer = [-1] * N

        for i in range(N - 1, -1, -1):
            while (
                monotonic_stack and frequency[monotonic_stack[-1]] <= frequency[arr[i]]
            ):
                monotonic_stack.pop()

            if monotonic_stack:
                answer[i] = monotonic_stack[-1]

            monotonic_stack.append(arr[i])

        return answer

        # Complexity analysis
        # Time : O(3N)
        # Space : O(2N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Next element with greater frequency - https://www.geeksforgeeks.org/problems/next-element-with-greater-frequency--170637/1

    testcase = [
        [[2, 1, 1, 3, 2, 1], [1, -1, -1, 2, 1, -1]],
        [[5, 1, 5, 6, 6], [-1, 5, -1, -1, -1]],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.nextFreqGreater(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 18 of January 2026

    p1()

    p2()
