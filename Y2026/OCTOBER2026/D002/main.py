class Solution1:
    def generateParenthesis(self, n: int) -> list[str]:
        # open, close

        parentheses = []

        def backtrack(open_count: int, close_count: int, current: str):
            if len(current) == 2 * n:
                parentheses.append(current)
                return

            if open_count < n:
                backtrack(open_count + 1, close_count, current + "(")

            if close_count < open_count:
                backtrack(open_count, close_count + 1, current + ")")

        backtrack(0, 0, "")
        return parentheses

        # Complexity Analysis
        # Time : O(2^N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 22. Generate Parentheses - https://leetcode.com/problems/generate-parentheses/submissions/2159792576/?envType=daily-question&envId=2026-10-02

    testcase = [
        [3, ["((()))", "(()())", "(())()", "()(())", "()()()"]],
        [1, ["()"]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.generateParenthesis(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def lexiString(self, s: str) -> str:
        # code here
        # booths algorithm

        N = len(s)

        i, j, k = 0, 1, 0

        while i < N and j < N and k < N:
            a = s[(i + k) % N]
            b = s[(j + k) % N]

            if a == b:
                k += 1
            elif a > b:
                i = i + k + 1
                if i <= j:
                    i = j + 1
                k = 0
            else:
                j = j + k + 1
                if j <= i:
                    j = i + 1
                k = 0

        start = min(i, j)
        return s[start:] + s[:start]

        # Complexity Analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Lexicographically Smallest Rotation - https://www.geeksforgeeks.org/problems/lexicographically-smallest-string--151951/1

    testcase = [
        # ["abcd", "abcd"],
        # ["baca", "abac"],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.lexiString(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def exist(self, board: list[list[str]], word: str) -> bool:

        M = len(board)
        N = len(board[0])
        W = len(word)

        MOVEMENTS = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1),
        ]

        def is_valid_index(ri: int, ci: int) -> bool:
            return ri < M and ri >= 0 and ci < N and ci >= 0

        def search(ri: int, ci: int, wi: int, visited: set[tuple[int, int]]) -> bool:
            if wi == W:
                return True

            for y, x in MOVEMENTS:
                n_ri = ri + y
                n_ci = ci + x

                if not is_valid_index(n_ri, n_ci):
                    continue

                if (n_ri, n_ci) in visited:
                    continue

                if board[n_ri][n_ci] != word[wi]:
                    continue

                visited.add((n_ri, n_ci))

                if search(n_ri, n_ci, wi + 1, visited):
                    return True

                visited.remove((n_ri, n_ci))

            return False

        for ri in range(M):
            for ci in range(N):
                if board[ri][ci] != word[0]:
                    continue

                if search(ri, ci, 1, set([(ri, ci)])):
                    return True

        return False

        # Complexity Analysis
        # Time : O(M * N * W)
        # Space : O(W + W)


def p3():
    # Problem 3 : NC150 Leetcode 79. Word Search - https://leetcode.com/problems/word-search/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
            True,
        ],
        [
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "SEE",
            True,
        ],
        [
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCB",
            False,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.exist(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def largestRectangleArea(self, heights: list[int]) -> int:
        N = len(heights)

        left = [0] * N
        right = [N - 1] * N

        # x > y > ...
        stack = []
        for i in range(N):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                left[i] = stack[-1] + 1

            stack.append(i)

        # x > y > ...
        stack = []
        for i in range(N - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                right[i] = stack[-1] - 1

            stack.append(i)

        largest_area = 0

        for i in range(N):
            # (r - l) * height_cap
            area = (right[i] - left[i] + 1) * heights[i]
            largest_area = max(largest_area, area)

        return largest_area

        # Complexity Analysis
        # Time : O(N)
        # Space : O(N)


def p4():
    # Problem 4 : NC150 Leetcode 84. Largest Rectangle in Histogram - https://leetcode.com/problems/largest-rectangle-in-histogram/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[2, 1, 5, 6, 2, 3], 10],
        [[2, 4], 4],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.largestRectangleArea(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 2 of October 2026

    p1()

    p2()

    p3()

    p4()
