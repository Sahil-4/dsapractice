from typing import List


class Solution1:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        N = len(nums)
        answer = [False for _ in range(N)]

        decimal = 0
        for i in range(N):
            binary = nums[i]
            decimal = decimal << 1
            decimal = decimal | binary

            if decimal % 5 == 0:
                answer[i] = True

        return answer

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1018. Binary Prefix Divisible By 5 - https://leetcode.com/problems/binary-prefix-divisible-by-5/description/?envType=daily-question&envId=2025-11-24

    testcase = [
        [[0, 1, 1], [True, False, False]],
        [[1, 1, 1], [False, False, False]],
        [
            [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
            [
                True,
                False,
                False,
                False,
                True,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                True,
            ],
        ],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.prefixesDivBy5(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    class DSU:
        def __init__(self, n):
            self.p = list(range(n))
            self.r = [0] * n

        def find(self, x):
            if self.p[x] != x:
                self.p[x] = self.find(self.p[x])
            return self.p[x]

        def unite(self, a, b):
            a, b = self.find(a), self.find(b)
            if a == b:
                return False
            if self.r[a] < self.r[b]:
                a, b = b, a
            self.p[b] = a
            if self.r[a] == self.r[b]:
                self.r[a] += 1
            return True

    def runKruskalSkip(self, V, edges, skipU, skipV):
        dsu = self.DSU(V)
        cost = 0
        used = 0

        for u, v, w in edges:
            if (u == skipU and v == skipV) or (u == skipV and v == skipU):
                continue

            if dsu.unite(u, v):
                cost += w
                used += 1

        if used != V - 1:
            return float("inf")
        return cost

    def secondMST(self, V, edges):
        edges.sort(key=lambda x: x[2])

        dsu = self.DSU(V)
        mstCost = 0
        mstEdges = []

        for u, v, w in edges:
            if dsu.unite(u, v):
                mstCost += w
                mstEdges.append([u, v, w])

        second = float("inf")

        for u, v, w in mstEdges:
            newCost = self.runKruskalSkip(V, edges, u, v)
            if mstCost < newCost < second:
                second = newCost

        return -1 if second == float("inf") else second

        # Complexity analysis
        # Time : O(E log E)
        # Space : O(V + E)


def p2():
    # Problem 2 : POTD Geeksforgeeks Second Best Minimum Spanning Tree - https://www.geeksforgeeks.org/problems/second-best-minimum-spanning-tree/1

    testcase = [
        [
            5,
            7,
            [
                [0, 1, 4],
                [0, 2, 3],
                [1, 2, 1],
                [1, 3, 5],
                [2, 4, 10],
                [2, 3, 7],
                [3, 4, 2],
            ],
            12,
        ],
        [5, 4, [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]], -1],
        [
            6,
            9,
            [
                [4, 2, 0],
                [1, 2, 6],
                [3, 4, 2],
                [0, 4, 4],
                [5, 0, 6],
                [5, 4, 4],
                [4, 1, 2],
                [1, 3, 1],
                [5, 2, 6],
            ],
            12,
        ],
    ]

    for line in testcase:
        [V, E, edges, expected] = line
        s2 = Solution2()
        result = s2.secondMST(V, edges)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 24 of November 2025

    p1()

    p2()
