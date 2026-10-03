class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        N = len(s)

        llen = 0

        # Left to right pass :
        # catches every valid substring
        # where '(' never trails behind ')'
        left, right = 0, 0
        for i in range(N):
            if s[i] == "(":
                left += 1
            else:
                right += 1

            if left == right:
                llen = max(llen, 2 * right)
            elif right > left:
                left, right = 0, 0

        # Right to left pass :
        # catches the cases
        # where '(' stays ahead, e.g. "(()"
        left, right = 0, 0
        for i in range(N - 1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1

            if left == right:
                llen = max(llen, 2 * left)
            elif left > right:
                left, right = 0, 0

        return llen

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 32. Longest Valid Parentheses - https://leetcode.com/problems/longest-valid-parentheses/?envType=daily-question&envId=2026-10-03

    testcase = [
        ["(()", 2],
        [")()())", 4],
        ["", 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.longestValidParentheses(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def formCoils(self, n: int) -> list[list[int]]:
        N = 4 * n
        total = 8 * n * n

        # Coil 1 walks : down, right, up, left, down, ...
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        r, c = 0, 0
        coil1 = [r * N + c + 1]

        move = 0
        while len(coil1) < total:
            # Step lengths : N - 1, N - 2, N - 2, N - 4, N - 4, ..., 2, 2
            steps = N - 1 if move == 0 else N - 2 * ((move + 1) // 2)
            dr, dc = dirs[move % 4]

            for _ in range(steps):
                r += dr
                c += dc
                coil1.append(r * N + c + 1)

            move += 1

        # Coil 2 is coil 1 rotated by 180 degrees, so the value v becomes (N * N + 1 - v)
        coil2 = [N * N + 1 - v for v in coil1]

        return [coil1, coil2]

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(N * N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Coils in Matrix - https://www.geeksforgeeks.org/problems/form-coils-in-a-matrix4726/1

    testcase = [
        [1, [[1, 5, 9, 13, 14, 15, 11, 7], [16, 12, 8, 4, 3, 2, 6, 10]]],
        [
            2,
            [
                [
                    1,
                    9,
                    17,
                    25,
                    33,
                    41,
                    49,
                    57,
                    58,
                    59,
                    60,
                    61,
                    62,
                    63,
                    55,
                    47,
                    39,
                    31,
                    23,
                    15,
                    14,
                    13,
                    12,
                    11,
                    19,
                    27,
                    35,
                    43,
                    44,
                    45,
                    37,
                    29,
                ],
                [
                    64,
                    56,
                    48,
                    40,
                    32,
                    24,
                    16,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    10,
                    18,
                    26,
                    34,
                    42,
                    50,
                    51,
                    52,
                    53,
                    54,
                    46,
                    38,
                    30,
                    22,
                    21,
                    20,
                    28,
                    36,
                ],
            ],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.formCoils(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)

        # Sorting groups the duplicates together
        nums.sort()

        result = []
        subset = []

        def backtrack(start: int) -> None:
            result.append(subset[:])

            for i in range(start, N):
                # Same value already tried at this position of the subset
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)

        return result

        # Complexity analysis
        # Time : O(N * 2^N)
        # Space : O(N) recursion stack, excluding the output


def p3():
    # Problem 3 : NC150 Leetcode 90. Subsets II - https://leetcode.com/problems/subsets-ii/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]],
        [[0], [[], [0]]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.subsetsWithDup(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def numDecodings(self, s: str) -> int:
        N = len(s)

        # ways[i] : number of ways to decode s[i:]
        # Only ways[i + 1] and ways[i + 2] are needed, so two variables are enough
        next1, next2 = 1, 0

        for i in range(N - 1, -1, -1):
            if s[i] == "0":
                curr = 0
            else:
                curr = next1

                if i + 1 < N and 10 <= int(s[i : i + 2]) <= 26:
                    curr += next2

            next1, next2 = curr, next1

        return next1

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p4():
    # Problem 4 : NC150 Leetcode 91. Decode Ways - https://leetcode.com/problems/decode-ways/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["12", 2],
        ["226", 3],
        ["06", 0],
        ["10", 1],
        ["27", 1],
        ["11106", 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.numDecodings(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 3 of October 2026

    p1()

    p2()

    p3()

    p4()
