class Solution1:
    def minimumDistance(self, word: str) -> int:
        # char - index (0–25)
        def idx(c):
            return ord(c) - ord("A")

        # positions on keyboard
        def pos(i):
            return (i // 6, i % 6)

        # manhattan distance
        def dist(a, b):
            x1, y1 = pos(a)
            x2, y2 = pos(b)
            return abs(x1 - x2) + abs(y1 - y2)

        N = len(word)

        # dp[j] = min cost where:
        # - one finger is at previous character
        # - other finger is at letter j
        dp = [0] * 26

        for i in range(1, N):
            curr = idx(word[i])
            prev = idx(word[i - 1])

            new_dp = [float("inf")] * 26

            for j in range(26):
                # case 1: same finger presses current char
                cost_same = dp[j] + dist(prev, curr)
                if cost_same < new_dp[j]:
                    new_dp[j] = cost_same

                # case 2: other finger presses current char
                cost_other = dp[j] + dist(j, curr)
                if cost_other < new_dp[prev]:
                    new_dp[prev] = cost_other

            dp = new_dp

        return int(min(dp))

        # Complexity analysis
        # Time : O(N * 26)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1320. Minimum Distance to Type a Word Using Two Fingers - https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/description/?envType=daily-question&envId=2026-04-12

    testcase = [
        ["CAKE", 3],
        ["HAPPY", 6],
    ]

    for line in testcase:
        [word, expected] = line
        s1 = Solution1()
        result = s1.minimumDistance(word)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def isToeplitz(self, mat):
        # code here
        N = len(mat)
        M = len(mat[0])

        for i in range(N - 1):
            for j in range(M - 1):
                if mat[i][j] != mat[i + 1][j + 1]:
                    return False

        return True

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Toeplitz matrix - https://www.geeksforgeeks.org/problems/toeplitz-matrix/1

    testcase = [
        [
            [[6, 7, 8], [4, 6, 7], [1, 4, 6]],
            True,
        ],
        [
            [[6, 3, 8], [4, 9, 7], [1, 4, 6]],
            False,
        ],
    ]

    for line in testcase:
        [mat, expected] = line
        s2 = Solution2()
        result = s2.isToeplitz(mat)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 12 of April 2026

    p1()

    p2()
