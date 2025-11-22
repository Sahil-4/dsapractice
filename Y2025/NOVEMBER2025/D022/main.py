from typing import List


class Solution1:
    def minimumOperations(self, nums: List[int]) -> int:
        # approach
        # init toperations = 0
        # iterate on nums
        # for num in nums
        # operations = min(num % 3, 3 - (num % 3))
        # increment toperations by operations
        # return toperations

        toperations = 0

        for num in nums:
            operations = min(num % 3, 3 - (num % 3))
            toperations += operations

        return toperations

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3190. Find Minimum Operations to Make All Elements Divisible by Three - https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/?envType=daily-question&envId=2025-11-22

    testcase = [
        [[1, 2, 3, 4], 3],
        [[3, 6, 9], 0],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.minimumOperations(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class DisjointSet:
    def __init__(self, V):
        self.parent = [i for i in range(V)]
        self.rank = [1] * V
        self.size = [1] * V

    def findUParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findUParent(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        pu = self.findUParent(u)
        pv = self.findUParent(v)

        if pu == pv:
            return False

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1

        return True


class Solution2:
    def minConnect(self, V, edges):
        # code here
        dsu = DisjointSet(V)

        extra_edges = 0

        for u, v in edges:
            if not dsu.unionByRank(u, v):
                extra_edges += 1

        components = 0
        for i in range(V):
            if dsu.findUParent(i) == i:
                components += 1

        needed = components - 1

        if extra_edges >= needed:
            return needed

        return -1


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Operations to Connect Hospitals - https://www.geeksforgeeks.org/problems/minimize-connections/1

    testcase = [
        [4, 3, [[0, 1], [0, 2], [1, 2]], 1],
        [5, 4, [[0, 1], [0, 2], [2, 3], [3, 4]], 0],
    ]

    for line in testcase:
        [V, E, edges, expected] = line
        s2 = Solution2()
        result = s2.minConnect(V, edges)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 22 of November 2025

    p1()

    p2()
