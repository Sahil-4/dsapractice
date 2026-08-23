from collections import deque


class Solution1:
    def sumGame(self, num: str) -> bool:
        N = len(num)
        half = N // 2

        diff = 0
        q_left = 0
        q_right = 0

        for i, ch in enumerate(num):
            if i < half:
                if ch == "?":
                    q_left += 1
                else:
                    diff += int(ch)
            else:
                if ch == "?":
                    q_right += 1
                else:
                    diff -= int(ch)

        # avoid floating point
        return 2 * diff + 9 * (q_left - q_right) != 0

        # Complexity Analysis
        # Time: O(N)
        # Space: O(1)


def p1():
    # Problem 1 : POTD Leetcode 1927. Sum Game - https://leetcode.com/problems/sum-game/description/?envType=daily-question&envId=2026-08-23

    testcase = [
        ["5023", False],
        ["25??", True],
        ["?3295???", False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.sumGame(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def numberOfCells(
        self, r: int, c: int, u: int, d: int, mat: list[list[str]]
    ) -> int:
        # code here

        rows, cols = len(mat), len(mat[0])

        if mat[r][c] == "#":
            return 0

        # best[row][col] = (max remaining up, max remaining down)
        best = [[(-1, -1) for _ in range(cols)] for _ in range(rows)]

        queue = deque([(r, c, u, d)])
        best[r][c] = (u, d)

        count = 1

        while queue:
            row, col, up_left, down_left = queue.popleft()

            moves = [
                (row, col - 1, up_left, down_left),
                (row, col + 1, up_left, down_left),
            ]

            if up_left > 0:
                moves.append((row - 1, col, up_left - 1, down_left))

            if down_left > 0:
                moves.append((row + 1, col, up_left, down_left - 1))

            for next_row, next_col, next_up, next_down in moves:
                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    continue

                if mat[next_row][next_col] == "#":
                    continue

                old_up, old_down = best[next_row][next_col]

                if next_up <= old_up and next_down <= old_down:
                    continue

                if old_up == -1:
                    count += 1

                best[next_row][next_col] = (
                    max(old_up, next_up),
                    max(old_down, next_down),
                )

                queue.append((next_row, next_col, next_up, next_down))

        return count

        # Complexity Analysis
        # Time: O(N * M * log(N * M))
        # Space: O(N * M)


def p2():
    # Problem 2 : POTD Geeksforgeeks Geek in a Maze - https://www.geeksforgeeks.org/problems/geek-in-a-maze--170637/1

    testcase = [
        [1, 0, 1, 1, [[".", ".", "."], [".", "#", "."], ["#", ".", "."]], 5],
        [2, 1, 2, 2, [[".", ".", "."], [".", "#", "."], [".", ".", "."]], 8],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.numberOfCells(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 23 of August 2026

    p1()

    p2()
