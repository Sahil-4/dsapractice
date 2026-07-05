class Solution1:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        MOD = 10**9 + 7

        board_size = len(board)

        # dp[row][col] = [maximum_score, number_of_paths]
        dp = [[[-1, 0] for _ in range(board_size)] for _ in range(board_size)]

        # start from the destination
        dp[board_size - 1][board_size - 1] = [0, 1]

        def update(
            current_row: int,
            current_col: int,
            next_row: int,
            next_col: int,
        ) -> None:
            if (
                next_row >= board_size
                or next_col >= board_size
                or dp[next_row][next_col][0] == -1
            ):
                return

            next_score, next_paths = dp[next_row][next_col]
            current_score, current_paths = dp[current_row][current_col]

            if next_score > current_score:
                dp[current_row][current_col] = [next_score, next_paths]

            elif next_score == current_score:
                dp[current_row][current_col][1] = (current_paths + next_paths) % MOD

        for row in range(board_size - 1, -1, -1):
            for col in range(board_size - 1, -1, -1):
                if (row == board_size - 1 and col == board_size - 1) or board[row][
                    col
                ] == "X":
                    continue

                # reach current cell from down, right or diagonal
                update(row, col, row + 1, col)
                update(row, col, row, col + 1)
                update(row, col, row + 1, col + 1)

                if dp[row][col][0] == -1:
                    continue

                if board[row][col] != "E":
                    dp[row][col][0] += int(board[row][col])

        if dp[0][0][0] == -1:
            return [0, 0]

        return dp[0][0]

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(N * N)


def p1():
    # Problem 1 : POTD Leetcode 1301. Number of Paths with Max Score - https://leetcode.com/problems/number-of-paths-with-max-score/description/?envType=daily-question&envId=2026-07-05

    testcase = [
        [["E23", "2X2", "12S"], [7, 1]],
        [["E12", "1X1", "21S"], [4, 2]],
        [["E11", "XXX", "11S"], [0, 0]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.pathsWithMaxScore(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxCharGap(self, s: str) -> int:
        # code here

        N = len(s)

        frequency_first_last = dict()

        for i in range(N):
            ch = s[i]

            if ch not in frequency_first_last:
                frequency_first_last[ch] = [i, i - 1]
            else:
                frequency_first_last[ch][1] = i

        max_diff = -1
        for i in range(26):
            ch = chr(ord("a") + i)

            if ch not in frequency_first_last:
                continue

            max_diff = max(
                max_diff, frequency_first_last[ch][1] - frequency_first_last[ch][0] - 1
            )

        return max_diff

        # Complexity analysis
        # Time : O(N)
        # Space : O(26)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Gap Between Two Same - https://www.geeksforgeeks.org/problems/maximum-number-of-characters-between-any-two-same-character4552/1

    testcase = [
        ["socks", 3],
        ["for", -1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxCharGap(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 5 of July 2026

    p1()

    p2()
