from collections import defaultdict


class Solution1:
    def checkValidString(self, s: str) -> bool:
        N = len(s)

        dp_curr = [False] * (N + 1)
        dp_curr[0] = True

        for si in range(N - 1, -1, -1):
            dp_next = [False] * (N + 1)

            for psum in range(N - 1, -1, -1):
                is_valid = False

                if s[si] == "(" or s[si] == "*":
                    is_valid = is_valid or dp_curr[psum + 1]

                if (s[si] == ")" or s[si] == "*") and psum > 0:
                    is_valid = is_valid or dp_curr[psum - 1]

                if s[si] == "*":
                    is_valid = is_valid or dp_curr[psum]

                dp_next[psum] = is_valid

            dp_curr = dp_next

        return dp_curr[0]

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 678. Valid Parenthesis String - https://leetcode.com/problems/valid-parenthesis-string/description/?envType=daily-question&envId=2026-10-04

    testcase = [
        ["()", True],
        ["(*)", True],
        ["(*))", True],
        ["(", False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.checkValidString(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findPerimeter(self, mat: list[list[int]]) -> int:
        # code here
        # 4 + 4 - 2 + 2 - 1 + 3 - 1 + 3
        # 4 - 1 + 3 - 1 + 3
        # traverse matrix
        # skip 0 cells
        # increment total sum by 4
        # if cell is not adjacent to any other 1 cell
        # else decrement number of adjacent 1 cells
        # and increment 4 - number of adjacent 1 cells
        # adjacent only in top and left (because bottom and right are not yet filled)

        N = len(mat)
        M = len(mat[0])

        tsum = 0

        for ri in range(N):
            for ci in range(M):
                if mat[ri][ci] == 0:
                    continue

                adjacent_1_count = 0

                # top
                if ri > 0 and mat[ri - 1][ci] == 1:
                    adjacent_1_count += 1

                # left
                if ci > 0 and mat[ri][ci - 1] == 1:
                    adjacent_1_count += 1

                tsum -= adjacent_1_count
                tsum += 4
                tsum -= adjacent_1_count

        return tsum

        # Complexity analysis
        # Time : O(N*M)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Perimeter of Shapes in Binary Matrix - https://www.geeksforgeeks.org/problems/find-perimeter-of-shapes/1

    testcase = [
        [[[0, 1, 0, 0, 0], [1, 1, 1, 0, 0], [1, 0, 0, 0, 0]], 12],
        [[[1, 0], [1, 1]], 8],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.findPerimeter(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class DetectSquares:

    def __init__(self):
        self.points = list()
        self.points_count = defaultdict(int)

        # Complexity analysis
        # Time : O(1)
        # Space : O(1)

    def add(self, point: list[int]) -> None:
        self.points.append(point)
        self.points_count[tuple(point)] += 1

        # Complexity analysis
        # Time : O(1)
        # Space : O(1)

    def count(self, point: list[int]) -> int:
        c = 0

        px, py = point
        for x, y in self.points:
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            c += self.points_count[(x, py)] * self.points_count[(px, y)]

        return c

        # Complexity analysis
        # Time : O(P)
        # Space : O(1)


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)


def p3():
    # Problem 3 : NC150 Leetcode 2013. Detect Squares - https://leetcode.com/problems/detect-squares/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"],
            [
                [],
                [[3, 10]],
                [[11, 2]],
                [[3, 2]],
                [[11, 10]],
                [[14, 8]],
                [[11, 2]],
                [[11, 10]],
            ],
            [None, None, None, None, 1, 0, None, 2],
        ]
    ]

    for operations, params, expected in testcase:
        obj = None
        result = []

        for operation, param, exp in zip(operations, params, expected):
            actual = None

            if operation == "DetectSquares":
                obj = DetectSquares()

            elif operation == "add":
                if isinstance(obj, DetectSquares):
                    obj.add(param[0])

            elif operation == "count":
                if isinstance(obj, DetectSquares):
                    actual = obj.count(param[0])

            result.append(actual)
            assert actual == exp, (
                f"Operation: {operation}, "
                f"Input: {param}, "
                f"Expected: {exp}, Got: {actual}"
            )

        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N = len(s1)
        M = len(s2)
        K = len(s3)

        if N + M != K:
            return False

        dp_next = [False] * (M + 1)

        for i1 in range(N, -1, -1):
            dp_curr = [False] * (M + 1)

            for i2 in range(M, -1, -1):
                if i1 + i2 >= K:
                    dp_curr[i2] = True

                else:
                    check = False

                    if i1 < N and s1[i1] == s3[i1 + i2]:
                        check = check or dp_next[i2]

                    if i2 < M and s2[i2] == s3[i1 + i2]:
                        check = check or dp_curr[i2 + 1]

                    dp_curr[i2] = check

            dp_next = dp_curr

        return dp_next[0]

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(M)


def p4():
    # Problem 4 : NC150 Leetcode 97. Interleaving String - https://leetcode.com/problems/interleaving-string/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["aabcc", "dbbca", "aadbbcbcac", True],
        ["aabcc", "dbbca", "aadbbbaccc", False],
        ["", "", "", True],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.isInterleave(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 4 of October 2026

    p1()

    p2()

    p3()

    p4()
