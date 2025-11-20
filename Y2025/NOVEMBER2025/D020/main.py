from typing import List
import functools


class Solution1:
    @staticmethod
    def check(a, b):
        if a[1] == b[1]:
            return b[0] - a[0]
        return a[1] - b[1]

    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=functools.cmp_to_key(Solution1.check))

        count = 2
        maxi = [intervals[0][1] - 1, intervals[0][1]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if maxi[1] < start:
                count += 2
                maxi = [end - 1, end]

            elif maxi[0] < start:
                count += 1
                maxi = [maxi[1], end]

        return count


def p1():
    # Problem 1 : POTD Leetcode 757. Set Intersection Size At Least Two - https://leetcode.com/problems/set-intersection-size-at-least-two/description/?envType=daily-question&envId=2025-11-20

    testcases = [
        [[[1, 3], [3, 7], [8, 9]], 5],
        [[[1, 3], [1, 4], [2, 5], [3, 5]], 3],
        [[[1, 2], [2, 3], [2, 4], [4, 5]], 5],
    ]

    for intervals, expected in testcases:
        s1 = Solution1()
        result = s1.intersectionSizeTwo(intervals)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def floyd_warshall(self, dist):
        n = 26
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist

    def minCost(self, s, t, transform, cost):
        INF = 10**18
        n = 26
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for (a, b), c in zip(transform, cost):
            x = ord(a) - 97
            y = ord(b) - 97
            if c < dist[x][y]:
                dist[x][y] = c

        dist = self.floyd_warshall(dist)

        total = 0
        for i in range(len(s)):
            a = ord(s[i]) - 97
            b = ord(t[i]) - 97
            best = INF
            for c in range(n):
                if dist[a][c] < INF and dist[b][c] < INF:
                    v = dist[a][c] + dist[b][c]
                    if v < best:
                        best = v
            if best == INF:
                return -1
            total += best

        return total

        # Complexity analysis
        # Time : O(N) and constant
        # Space : O(1) constant


def p2():
    # Problem 2 : POTD Geeksforgeeks Make Strings Equal - https://www.geeksforgeeks.org/problems/make-strings-equal--150209/1

    testcases = [
        ["abcc", "bccc", [["a", "b"], ["b", "c"], ["c", "a"]], [2, 1, 4], 3],
        [
            "az",
            "dc",
            [["a", "b"], ["b", "c"], ["c", "d"], ["a", "d"], ["z", "c"]],
            [5, 3, 2, 50, 10],
            20,
        ],
        ["xyz", "xzy", [["x", "y"], ["x", "z"]], [3, 3], -1],
    ]

    for s, t, transform, cost, expected in testcases:
        s2 = Solution2()
        result = s2.minCost(s, t, transform, cost)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 20 of November 2025

    p1()

    p2()
