from itertools import accumulate


class Solution1:
    MOD = 1_000_000_007

    def multiply_matrices(
        self, left_matrix: list[list[int]], right_matrix: list[list[int]]
    ) -> list[list[int]]:
        row_count = len(left_matrix)
        col_count = len(right_matrix[0])

        result = [[0] * col_count for _ in range(row_count)]

        for row in range(row_count):
            for middle in range(len(left_matrix[0])):
                value = left_matrix[row][middle]
                if value == 0:
                    continue

                for col in range(col_count):
                    result[row][col] = (
                        result[row][col] + value * right_matrix[middle][col]
                    ) % self.MOD

        return result

    def matrix_power_multiply(
        self,
        transition_matrix: list[list[int]],
        exponent: int,
        state_vector: list[list[int]],
    ) -> list[list[int]]:
        while exponent > 0:
            if exponent & 1:
                state_vector = self.multiply_matrices(state_vector, transition_matrix)

            transition_matrix = self.multiply_matrices(
                transition_matrix, transition_matrix
            )
            exponent >>= 1

        return state_vector

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        value_count = r - l + 1

        if n == 1:
            return value_count

        state_size = 2 * value_count

        transition_matrix = [[0] * state_size for _ in range(state_size)]

        for decrease_value in range(value_count):
            for smaller_value in range(decrease_value):
                transition_matrix[decrease_value][smaller_value + value_count] = 1

        for increase_value in range(value_count):
            for larger_value in range(increase_value + 1, value_count):
                transition_matrix[increase_value + value_count][larger_value] = 1

        initial_state = [[1] * state_size]

        final_state = self.matrix_power_multiply(
            transition_matrix, n - 1, initial_state
        )

        answer = 0

        for state_count in final_state[0]:
            answer = (answer + state_count) % self.MOD

        return answer

        # Complexity analysis
        # Time : O(M * M * M * Log(N))
        # Space : O(M * M)


def p1():
    # Problem 1 : POTD Leetcode 3700. Number of ZigZag Arrays II - https://leetcode.com/problems/number-of-zigzag-arrays-ii/description/?envType=daily-question&envId=2026-06-24

    testcase = [
        [3, 4, 5, 2],
        [3, 1, 3, 10],
    ]

    for line in testcase:
        [n, l, r, expected] = line
        s1 = Solution1()
        result = s1.zigZagArrays(n, l, r)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:

    def findPath(
        self,
        mat: list[list[int]],
        N: int,
        r: int,
        c: int,
        path: list[list[int]],
        bad: list[list[bool]],
    ) -> bool:
        # reached to destination
        if r == N - 1 and c == N - 1:
            path[r][c] = 1
            return True

        # invalid or blocked cell
        if not (0 <= r < N and 0 <= c < N and mat[r][c] != 0 and path[r][c] == 0):
            return False

        if bad[r][c]:
            return False

        # mark path
        path[r][c] = 1

        for jump in range(1, mat[r][c] + 1):
            if jump >= N:
                break

            # move right
            if c + jump < N and self.findPath(mat, N, r, c + jump, path, bad):
                return True

            # move down
            if r + jump < N and self.findPath(mat, N, r + jump, c, path, bad):
                return True

        # backtrack
        path[r][c] = 0
        bad[r][c] = True

        return False

    def shortestDist(self, mat: list[list[int]]) -> list[list[int]]:
        # code here
        N = len(mat)

        path = [[0] * N for _ in range(N)]
        bad = [[False] * N for _ in range(N)]

        if not self.findPath(mat, N, 0, 0, path, bad):
            return [[-1]]

        return path

        # Complexity analysis
        # Time : O(N * N * N)
        # Space : O(N * N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Rat Maze With Multiple Jumps - https://www.geeksforgeeks.org/problems/rat-maze-with-multiple-jumps3852/1

    testcase = [
        [
            [[2, 1, 0, 0], [3, 0, 0, 1], [0, 1, 0, 1], [0, 0, 0, 1]],
            [[1, 0, 0, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]],
        ],
        [
            [[2, 1, 0, 0], [2, 0, 0, 1], [0, 1, 0, 1], [0, 0, 0, 1]],
            [[-1]],
        ],
    ]

    for line in testcase:
        [mat, expected] = line
        s2 = Solution2()
        result = s2.shortestDist(mat)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 24 of June 2026

    p1()

    p2()
