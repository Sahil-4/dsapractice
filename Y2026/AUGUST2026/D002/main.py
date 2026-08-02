from functools import cache


class Solution1:
    def stoneGame(self, piles: list[int]) -> bool:

        @cache
        def solve(l: int, r: int) -> int:
            # one pile remain
            if l == r:
                return piles[l]

            take_left = piles[l] - solve(l + 1, r)
            take_right = piles[r] - solve(l, r - 1)

            return max(take_left, take_right)

        return solve(0, len(piles) - 1) > 0

        # Complexity Analysis
        # Time : O(N * N)
        # Space : O(N * N) + O(N)


def p1():
    # Problem 1 : POTD Leetcode 877. Stone Game - https://leetcode.com/problems/stone-game/description/?envType=daily-question&envId=2026-08-02

    testcase = [
        [[5, 3, 4, 5], True],
        [[3, 7, 2, 3], True],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.stoneGame(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def count(self, n: int, m: int) -> int:
        # adj[x] = all values y such that x | y or y | x
        adj = [[] for _ in range(m + 1)]

        for x in range(1, m + 1):
            seen = set()

            # multiples of x
            multiple = x
            while multiple <= m:
                seen.add(multiple)
                multiple += x

            # divisors of x
            for divisor in range(1, x + 1):
                if x % divisor == 0:
                    seen.add(divisor)

            adj[x] = list(seen)

        @cache
        def dfs(index: int, prev: int) -> int:
            if index == n:
                return 1

            _total = 0
            for nxt in adj[prev]:
                _total += dfs(index + 1, nxt)

            return _total

        total = 0
        for first in range(1, m + 1):
            total += dfs(1, first)

        return total

        # Complexity Analysis
        # Time : O(N * M * M)
        # Space : O(N * M + M * M)


def p2():
    # Problem 2 : POTD Geeksforgeeks Sequences where Adjacent Divide - https://www.geeksforgeeks.org/problems/count-in-array2138/1

    testcase = [
        [3, 3, 17],
        [1, 10, 10],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.count(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 2 of August 2026

    p1()

    p2()
