from typing import List


class Solution1:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        # area of square1 >= area of overlapping_part(square1, square1)
        # and similarly if we take more squares this area will get reduced more
        # hence to find best possible answer we have to take only two rectangles
        # now we just have to take rectangle pairs
        # find overlapping/intersecting part
        # find square inside this region
        # and update maximum answer

        max_side = 0

        N = len(bottomLeft)

        for i in range(N):
            for j in range(i + 1, N):
                # bottom left coordinates
                lx = max(bottomLeft[i][0], bottomLeft[j][0])
                ly = max(bottomLeft[i][1], bottomLeft[j][1])

                # top right coordinates
                rx = min(topRight[i][0], topRight[j][0])
                ry = min(topRight[i][1], topRight[j][1])

                # height and width
                width = rx - lx
                height = ry - ly

                # update max size (for answer)
                max_side = max(max_side, min(width, height))

        return max_side * max_side

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3047. Find the Largest Area of Square Inside Two Rectangles - https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/description/?envType=daily-question&envId=2026-01-17

    testcase = [
        [[[1, 1], [2, 2], [3, 1]], [[3, 3], [4, 4], [6, 6]], 1],
        [[[1, 1], [1, 3], [1, 5]], [[5, 5], [5, 7], [5, 9]], 4],
        [[[1, 1], [2, 2], [1, 2]], [[3, 3], [4, 4], [3, 4]], 1],
        [[[1, 1], [3, 3], [3, 1]], [[2, 2], [4, 4], [4, 2]], 0],
    ]

    for line in testcase:
        [bottomLeft, topRight, expected] = line
        s1 = Solution1()
        result = s1.largestSquareArea(bottomLeft, topRight)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def checkRedundancy(self, s):
        # code here
        # s = "((a+b))"
        # stack =
        # Problem : find parens with zero operators
        # use stack
        # traverse from left to right
        # if char != "("
        # put it into stack
        # else
        # init operators count = 0
        # pop chars from stack until char != "("
        # if operator found increment operators count
        # upon hitting "(" if operators count is 0 return true
        # at the end return false (as we do not found any paren with zero operators)

        stack = []

        for char in s:
            if char != ")":
                stack.append(char)
            else:
                operators_count = 0
                while stack[-1] != "(":
                    if stack[-1] in ["+", "-", "*", "/"]:
                        operators_count += 1
                    stack.pop()
                stack.pop()

                if operators_count == 0:
                    return True

        return False

        # Complexity analysis
        # Time : O(2N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Expression contains redundant bracket or not - https://www.geeksforgeeks.org/problems/expression-contains-redundant-bracket-or-not/1

    testcase = [
        ["((a+b))", True],
        ["(a+(b)/c)", True],
        ["(a+b+(c+d))", False],
    ]

    for line in testcase:
        [s, expected] = line
        s2 = Solution2()
        result = s2.checkRedundancy(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 17 of January 2026

    p1()

    p2()
