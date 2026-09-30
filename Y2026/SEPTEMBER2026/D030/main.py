class Solution1:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        N = len(seq)

        answer = [0] * N
        depth = 0

        for i, char in enumerate(seq):
            if char == "(":
                depth += 1
                answer[i] = depth % 2
            else:
                answer[i] = depth % 2
                depth -= 1

        return answer

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1111. Maximum Nesting Depth of Two Valid Parentheses Strings - https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/description/?envType=daily-question&envId=2026-09-30

    testcase = [
        ["(()())", [1, 0, 0, 0, 0, 1]],
        ["()(())()", [1, 1, 1, 0, 0, 1, 1, 1]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maxDepthAfterSplit(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def ways(self, x: int, y: int) -> int:
        # code here

        MOD = 1000000007

        # dp[i][j] = number of ways to reach (0, 0) from (i, j)
        dp = [[0] * (y + 1) for _ in range(x + 1)]

        # base cases
        # only one possible path along either axis
        for i in range(x + 1):
            dp[i][0] = 1

        # only one possible path along either axis
        for j in range(y + 1):
            dp[0][j] = 1

        # each cell can be reached by moving left or down
        for i in range(1, x + 1):
            for j in range(1, y + 1):
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

        return dp[x][y]

        # Complexity analysis
        # Time : O(X * Y)
        # Space : O(X * Y)


def p2():
    # Problem 2 : POTD Geeksforgeeks Ways to Reach Origin - https://www.geeksforgeeks.org/problems/paths-to-reach-origin3850/1

    testcase = [
        [3, 0, 1],
        [3, 6, 84],
        [25, 41, 939390319],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.ways(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])

        low = 0
        high = N * M - 1

        while low <= high:
            mid = (low + high) // 2

            r = mid // N
            c = mid % N

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

        # Complexity analysis
        # Time : O(Log(X * Y))
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 74. Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            3,
            True,
        ],
        [
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            13,
            False,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.searchMatrix(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 30 of September 2026

    p1()

    p2()

    p3()
