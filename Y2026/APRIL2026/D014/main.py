import sys
from typing import List


class Solution1:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # sort input - number line
        robot.sort()
        factory.sort()

        # expand factory - multiple factory on same point, instead of a single factory with more then 1 cap
        factory_expanded = []

        for position, limit in factory:
            for _ in range(limit):
                factory_expanded.append(position)

        N = len(factory_expanded)
        M = len(robot)

        dp = [[-1] * (N + 1) for _ in range(M + 1)]

        def solve(ri: int, fi: int):
            # solved
            if ri >= M:
                return 0

            # factories exhausted
            if fi >= N:
                return sys.maxsize

            # pre-calculated
            if dp[ri][fi] != -1:
                return dp[ri][fi]

            # take - use this factory
            take = abs(robot[ri] - factory_expanded[fi]) + solve(ri + 1, fi + 1)

            # skip - dont use this factory
            skip = solve(ri, fi + 1)

            dp[ri][fi] = min(take, skip)

            return dp[ri][fi]

        return solve(0, 0)

        # Complexity analysis
        # Time : O(2 * M * N)
        # Space : O(M * N)


def p1():
    # Problem 1 : POTD Leetcode 2463. Minimum Total Distance Traveled - https://leetcode.com/problems/minimum-total-distance-traveled/description/?envType=daily-question&envId=2026-04-14

    testcase = [
        [[0, 4, 6], [[2, 2], [6, 2]], 4],
        [[1, -1], [[-2, 1], [2, 1]], 2],
    ]

    for line in testcase:
        [robot, factory, expected] = line
        s1 = Solution1()
        result = s1.minimumTotalDistance(robot, factory)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def removeSpaces(self, s: str) -> str:
        # code here

        spaces_removed: list[str] = []

        for c in s:
            if c != " ":
                spaces_removed.append(c)

        return "".join(spaces_removed)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Remove Spaces - https://www.geeksforgeeks.org/problems/remove-spaces0128/1

    testcase = [
        ["g eeks for ge eks", "geeksforgeeks"],
        ["abc d ", "abcd"],
    ]

    for line in testcase:
        [s, expected] = line
        s2 = Solution2()
        result = s2.removeSpaces(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 14 of April 2026

    p1()

    p2()
