from typing import List


class Solution1:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        M = len(mat)
        N = len(mat[0])

        k = k % N

        if k == 0:
            return True

        for i in range(M):
            for j in range(N):

                curr_index = j
                final_index = j

                if i & 1:
                    final_index = (j - k + N) % N
                else:
                    final_index = (j + k) % N

                if mat[i][curr_index] != mat[i][final_index]:
                    return False

        return True

        # Complexity analysis
        # Time : O(M * N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2946. Matrix Similarity After Cyclic Shifts - https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/description/?envType=daily-question&envId=2026-03-27

    testcase = [
        [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, False],
        [[[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], 2, True],
        [[[2, 2], [2, 2]], 3, True],
    ]

    for line in testcase:
        [mat, k, expected] = line
        s1 = Solution1()
        result = s1.areSimilar(mat, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxChocolate(self, grid):
        N = len(grid)
        M = len(grid[0])

        # 3D DP array initialized with -1
        dp = [[[-1 for _ in range(M)] for _ in range(M)] for _ in range(N)]

        def memoization(grid, r, c1, c2, N, M, dp):
            # Out of bounds
            if (c1 < 0 or c1 >= M) or (c2 < 0 or c2 >= M):
                return -1

            # Last row
            if r == N - 1:
                if c1 == c2:
                    return grid[r][c1]
                return grid[r][c1] + grid[r][c2]

            # Already computed
            if dp[r][c1][c2] != -1:
                return dp[r][c1][c2]

            max_pick = -1

            # Explore all 9 possibilities
            for d1 in range(-1, 2):
                for d2 in range(-1, 2):
                    pickup = memoization(grid, r + 1, c1 + d1, c2 + d2, N, M, dp)
                    max_pick = max(max_pick, pickup)

            # Add current cell(s)
            max_pick += grid[r][c1]
            if c1 != c2:
                max_pick += grid[r][c2]

            dp[r][c1][c2] = max_pick
            return max_pick

        # Start from row 0, col1 = 0, col2 = last column
        return memoization(grid, 0, 0, M - 1, N, M, dp)

        # Complexity analysis
        # Time : O(9 * M * M * N)
        # Space : O(M * M * N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Chocolates Pickup - https://www.geeksforgeeks.org/problems/chocolates-pickup/1

    testcase = [
        [
            [[4, 1, 2], [3, 6, 1], [1, 6, 6], [3, 1, 2]],
            32,
        ],
        [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            32,
        ],
    ]

    for line in testcase:
        [grid, expected] = line
        s2 = Solution2()
        result = s2.maxChocolate(grid)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 27 of March 2026

    p1()

    p2()
