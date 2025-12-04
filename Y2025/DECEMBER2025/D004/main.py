class Solution1:
    def countCollisions(self, directions: str) -> int:
        stack = []
        collisions = 0

        for d in directions:
            if d == "R":
                stack.append("R")
            elif d == "S":
                while stack and stack[-1] == "R":
                    collisions += 1
                    stack.pop()
                stack.append("S")
            else:  # d == "L"
                if not stack or stack[-1] == "L" or stack[-1] == "S":
                    if stack and stack[-1] == "S":
                        collisions += 1
                        stack.append("S")
                else:
                    collisions += 2
                    stack.pop()
                    while stack and stack[-1] == "R":
                        collisions += 1
                        stack.pop()
                    stack.append("S")

        return collisions

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2211. Count Collisions on a Road - https://leetcode.com/problems/count-collisions-on-a-road/description/?envType=daily-question&envId=2025-12-04

    testcase = [
        ["RLRSLL", 5],
        ["LLRR", 0],
        ["LRLRLRLSLSLRLLLLR", 13],
        ["LRLRLRLRLLLLRLLLLLLSSLSSLSLSRRRRRRLRLLLLRLRLRL", 39],
    ]

    for line in testcase:
        [directions, expected] = line
        s1 = Solution1()
        result = s1.countCollisions(directions)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def optimal_bst(self, keys, freq):
        n = len(keys)

        dp = [[0.0] * n for _ in range(n)]

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + freq[i]

        def range_sum(i, j):
            return prefix[j + 1] - prefix[i]

        for i in range(n):
            dp[i][i] = freq[i]

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i][j] = float("inf")

                total_freq = range_sum(i, j)

                for r in range(i, j + 1):
                    left = dp[i][r - 1] if r > i else 0
                    right = dp[r + 1][j] if r < j else 0
                    cost = left + right + total_freq

                    dp[i][j] = min(dp[i][j], cost)

        return int(dp[0][n - 1])

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(N*N)

    def minCost(self, keys, freq):
        # code here
        return self.optimal_bst(keys, freq)


def p2():
    # Problem 2 : POTD Geeksforgeeks Optimal binary search tree - https://www.geeksforgeeks.org/problems/optimal-binary-search-tree2214/1

    testcase = [
        [[10, 12], [34, 50], 118],
        [[10, 12, 20], [34, 8, 50], 142],
    ]

    for line in testcase:
        [keys, freq, expected] = line
        s2 = Solution2()
        result = s2.minCost(keys, freq)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 4 of December 2025

    p1()

    p2()
