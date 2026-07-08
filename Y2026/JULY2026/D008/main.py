from collections import deque


class Solution1:
    def sumAndMultiply(
        self,
        s: str,
        queries: list[list[int]],
    ) -> list[int]:
        MOD = 10**9 + 7

        string_length = len(s)

        # powers of 10 modulo MOD
        power_of_10 = [1] * (string_length + 1)

        for i in range(1, string_length + 1):
            power_of_10[i] = (power_of_10[i - 1] * 10) % MOD

        # prefix sum of digits
        prefix_sum = [0] * (string_length + 1)

        # prefix concatenation of non-zero digits
        prefix_number = [0] * (string_length + 1)

        # prefix count of non-zero digits
        prefix_non_zero_count = [0] * (string_length + 1)

        for index, character in enumerate(s):
            digit = int(character)

            prefix_sum[index + 1] = prefix_sum[index] + digit

            if digit == 0:
                prefix_number[index + 1] = prefix_number[index]
                prefix_non_zero_count[index + 1] = prefix_non_zero_count[index]
            else:
                prefix_number[index + 1] = (prefix_number[index] * 10 + digit) % MOD

                prefix_non_zero_count[index + 1] = prefix_non_zero_count[index] + 1

        answer = []

        for left, right in queries:
            right += 1

            non_zero_digits = prefix_non_zero_count[right] - prefix_non_zero_count[left]

            concatenated_number = (
                prefix_number[right]
                - prefix_number[left] * power_of_10[non_zero_digits]
            ) % MOD

            digit_sum = prefix_sum[right] - prefix_sum[left]

            answer.append((concatenated_number * digit_sum) % MOD)

        return answer

        # Complexity analysis
        # Time : O(N + Q)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3756. Concatenate Non-Zero Digits and Multiply by Sum II - https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/description/?envType=daily-question&envId=2026-07-08

    testcase = [
        ["10203004", [[0, 7], [1, 3], [4, 6]], [12340, 4, 9]],
        ["1000", [[0, 3], [1, 1]], [1, 0]],
        ["9876543210", [[0, 9]], [444444137]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.sumAndMultiply(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countCoordinates(self, mat: list[list[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(queue: deque, reachable: list[list[bool]]) -> None:
            while queue:
                current_row, current_col = queue.popleft()

                for row_offset, col_offset in directions:
                    next_row = current_row + row_offset
                    next_col = current_col + col_offset

                    if (
                        next_row < 0
                        or next_row >= rows
                        or next_col < 0
                        or next_col >= cols
                        or reachable[next_row][next_col]
                    ):
                        continue

                    # Reverse BFS:
                    # We can reach the neighbor only if its signal strength
                    # is greater than or equal to the current tower.
                    if mat[next_row][next_col] < mat[current_row][current_col]:
                        continue

                    reachable[next_row][next_col] = True
                    queue.append((next_row, next_col))

        station_p_queue = deque()
        station_q_queue = deque()

        reachable_from_station_p = [[False] * cols for _ in range(rows)]
        reachable_from_station_q = [[False] * cols for _ in range(rows)]

        # top and bottom boundaries
        for col in range(cols):
            station_p_queue.append((0, col))
            reachable_from_station_p[0][col] = True

            station_q_queue.append((rows - 1, col))
            reachable_from_station_q[rows - 1][col] = True

        # left and right boundaries
        for row in range(rows):
            station_p_queue.append((row, 0))
            reachable_from_station_p[row][0] = True

            station_q_queue.append((row, cols - 1))
            reachable_from_station_q[row][cols - 1] = True

        bfs(station_p_queue, reachable_from_station_p)
        bfs(station_q_queue, reachable_from_station_q)

        count = 0

        for row in range(rows):
            for col in range(cols):
                if (
                    reachable_from_station_p[row][col]
                    and reachable_from_station_q[row][col]
                ):
                    count += 1

        return count

        # Complexity analysis
        # Time : O(R * C)
        # Space : O(R * C)


def p2():
    # Problem 2 : POTD Geeksforgeeks Towers Reaching Both Stations - https://www.geeksforgeeks.org/problems/geeks-island--170646/1

    testcase = [
        [
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ],
            7,
        ],
        [
            [
                [2, 2],
                [2, 2],
            ],
            4,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.countCoordinates(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 8 of July 2026

    p1()

    p2()
