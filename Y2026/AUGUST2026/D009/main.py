class Solution1:
    def stoneGameII(self, piles: list[int]) -> int:
        N = len(piles)

        # dp[person][i][M]
        # person = 1 -> Alice
        # person = 0 -> Bob
        dp = [[[-1] * (N + 1) for _ in range(N + 1)] for _ in range(2)]

        def solveForAlice(person: int, i: int, M: int) -> int:
            if i >= N:
                return 0

            if dp[person][i][M] != -1:
                return dp[person][i][M]

            if person == 1:  # Alice
                result = -1
            else:  # Bob
                result = float("inf")

            stones = 0

            for x in range(1, min(2 * M, N - i) + 1):
                stones += piles[i + x - 1]

                if person == 1:  # Alice
                    result = max(result, stones + solveForAlice(0, i + x, max(M, x)))

                else:  # Bob
                    result = min(result, solveForAlice(1, i + x, max(M, x)))

            dp[person][i][M] = int(result)
            return dp[person][i][M]

        return solveForAlice(1, 0, 1)

        # Complexity analysis
        # Time : O(N*N*N)
        # Space : O(N*N)


def p1():
    # Problem 1 : POTD Leetcode 1140. Stone Game II - https://leetcode.com/problems/stone-game-ii/description/?envType=daily-question&envId=2026-08-09

    testcase = [
        [[2, 7, 9, 4, 4], 10],
        [[1, 2, 3, 4, 5, 100], 104],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.stoneGameII(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def zigzagSequence(self, mat: list[list[int]]) -> int:
        # code here

        N = len(mat)

        prev = mat[0][:]

        for i in range(1, N):
            curr = [0] * N

            for j in range(N):
                curr[j] = mat[i][j] + max(prev[k] for k in range(N) if k != j)

            prev = curr

        return max(prev)

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Largest Zigzag Sequence - https://www.geeksforgeeks.org/problems/largest-zigzag-sequence5416/1

    testcase = [
        [[[3, 1, 2], [4, 8, 5], [6, 9, 7]], 18],
        [[[1, 2, 4], [3, 9, 6], [11, 3, 15]], 28],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.zigzagSequence(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 9 of August 2026

    p1()

    p2()
