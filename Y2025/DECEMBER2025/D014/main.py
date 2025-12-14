class Solution1:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1000000007

        ways_count = 0
        seeds_count = 0
        answer = 1

        for c in corridor:
            if c == "S":
                seeds_count += 1

            if seeds_count == 2:
                ways_count += 1

            if seeds_count == 3:
                answer = (answer * ways_count) % MOD
                ways_count = 0
                seeds_count = 1

        if seeds_count != 2:
            return 0

        return answer

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2147. Number of Ways to Divide a Long Corridor - https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/description/?envType=daily-question&envId=2025-12-14

    testcase = [
        ["SSPPSPS", 3],
        ["PPSPSP", 1],
        ["S", 0],
    ]

    for line in testcase:
        [corridor, expected] = line
        s1 = Solution1()
        result = s1.numberOfWays(corridor)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def prefixSum2D(self, mat, queries):
        n = len(mat)
        m = len(mat[0])

        for i in range(n):
            for j in range(m):
                top = mat[i - 1][j] if i > 0 else 0
                left = mat[i][j - 1] if j > 0 else 0
                diag = mat[i - 1][j - 1] if i > 0 and j > 0 else 0
                mat[i][j] += top + left - diag

        result = []
        for r1, c1, r2, c2 in queries:
            total = mat[r2][c2]
            if r1 > 0:
                total -= mat[r1 - 1][c2]
            if c1 > 0:
                total -= mat[r2][c1 - 1]
            if r1 > 0 and c1 > 0:
                total += mat[r1 - 1][c1 - 1]
            result.append(total)

        return result

        # Complexity analysis
        # Time : O(N*M) + O(Q)
        # Space : O(N*M)


def p2():
    # Problem 2 : POTD Geeksforgeeks 2D Submatrix Sum Queries - https://www.geeksforgeeks.org/problems/2d-submatrix-sum-queries/1

    testcase = [
        [
            [
                [1, 2, 3],
                [1, 1, 0],
                [4, 2, 2],
            ],
            [
                [0, 0, 1, 1],
                [1, 0, 2, 2],
            ],
            [5, 10],
        ],
        [
            [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1],
            ],
            [
                [1, 1, 2, 2],
                [0, 0, 2, 2],
                [0, 2, 2, 2],
            ],
            [4, 9, 3],
        ],
    ]

    for line in testcase:
        [mat, queries, expected] = line
        s2 = Solution2()
        result = s2.prefixSum2D(mat, queries)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 14 of December 2025

    p1()

    p2()
