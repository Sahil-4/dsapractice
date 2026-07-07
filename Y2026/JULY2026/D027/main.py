class Solution1:
    def sumAndMultiply(self, n: int) -> int:
        str_n = str(n)
        str_n = str_n.replace("0", "")

        x = int(str_n) if str_n else 0
        dsum = sum(int(d) for d in str_n)

        return x * dsum

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(Log(N))


def p1():
    # Problem 1 : POTD Leetcode 3754. Concatenate Non-Zero Digits and Multiply by Sum I - https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/description/?envType=daily-question&envId=2026-07-07

    testcase = [
        [10203004, 12340],
        [1000, 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.sumAndMultiply(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def largestArea(self, n: int, m: int, arr: list[list[int]]) -> int:
        blocked_rows = [0, n + 1]
        blocked_cols = [0, m + 1]

        # collect all blocked rows and columns
        for row, col in arr:
            blocked_rows.append(row)
            blocked_cols.append(col)

        blocked_rows.sort()
        blocked_cols.sort()

        maximum_row_gap = 0

        for index in range(1, len(blocked_rows)):
            maximum_row_gap = max(
                maximum_row_gap,
                blocked_rows[index] - blocked_rows[index - 1] - 1,
            )

        maximum_column_gap = 0

        for index in range(1, len(blocked_cols)):
            maximum_column_gap = max(
                maximum_column_gap,
                blocked_cols[index] - blocked_cols[index - 1] - 1,
            )

        return maximum_row_gap * maximum_column_gap

        # Complexity analysis
        # Time : O(K * Log(K))
        # Space : O(K)


def p2():
    # Problem 2 : POTD Geeksforgeeks Largest Unblocked Submatrix - https://www.geeksforgeeks.org/problems/largest-unblocked-submatrix/1

    testcase = [
        [5, 5, [[2, 3], [5, 1]], 4],
        [2, 2, [[2, 2]], 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.largestArea(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 7 of July 2026

    p1()

    p2()
