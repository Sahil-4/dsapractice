from collections import defaultdict
from typing import List


class Solution1:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def getMaxDepth(node: int, parent: int) -> int:
            depth = 0

            for neighbor in adj[node]:
                if neighbor != parent:
                    depth = max(depth, getMaxDepth(neighbor, node) + 1)

            return depth

        maxDepth = getMaxDepth(1, 0)

        return pow(2, maxDepth - 1, 10**9 + 7)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3558. Number of Ways to Assign Edge Weights I - https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/description/?envType=daily-question&envId=2026-06-11

    testcase = [
        [[[1, 2]], 1],
        [[[1, 2], [1, 3], [3, 4], [3, 5]], 2],
    ]

    for line in testcase:
        [edges, expected] = line
        s1 = Solution1()
        result = s1.assignEdgeWeights(edges)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findIndex(self, s: str) -> int:
        # code here
        N = len(s)

        sum_closing = 0
        for i in range(N):
            sum_closing += 1 if s[i] == ")" else 0
        sum_opening = 0
        for i in range(N):
            if sum_opening == sum_closing:
                return i

            sum_opening += 1 if s[i] == "(" else 0
            sum_closing -= 1 if s[i] == ")" else 0

        if sum_opening == sum_closing:
            return N

        return -1

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Equal Point in Brackets - https://www.geeksforgeeks.org/problems/find-equal-point-in-string-of-brackets2542/1

    testcase = [
        ["(())))(", 4],
        ["))", 2],
    ]

    for line in testcase:
        [s, expected] = line
        s2 = Solution2()
        result = s2.findIndex(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 11 of June 2026

    p1()

    p2()
