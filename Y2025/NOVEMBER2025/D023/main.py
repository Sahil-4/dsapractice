from typing import List


class Solution1:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)

        # smallest remainder-1 and remainder-2 numbers
        r1 = []
        r2 = []

        for num in nums:
            if num % 3 == 1:
                r1.append(num)
            elif num % 3 == 2:
                r2.append(num)

        r1.sort()
        r2.sort()

        rem = total % 3

        if rem == 0:
            return total

        # removing smallest valid option
        remove_cost = float("inf")

        if rem == 1:
            if len(r1) >= 1:
                remove_cost = min(remove_cost, r1[0])
            if len(r2) >= 2:
                remove_cost = min(remove_cost, r2[0] + r2[1])
        else:
            if len(r2) >= 1:
                remove_cost = min(remove_cost, r2[0])
            if len(r1) >= 2:
                remove_cost = min(remove_cost, r1[0] + r1[1])

        # remove_cost is still inf → no valid removal
        if remove_cost == float("inf"):
            return 0

        return int(total - remove_cost)

        # Complexity analysis
        # Time : O(N) + O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1262. Greatest Sum Divisible by Three - https://leetcode.com/problems/greatest-sum-divisible-by-three/description/?envType=daily-question&envId=2025-11-23

    testcase = [
        [[3, 6, 5, 1, 8], 18],
        [[4], 0],
        [[1, 2, 3, 4, 4], 12],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.maxSumDivThree(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class DSU:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


class Solution2:
    def maxRemove(self, stones):
        dsu = DSU()

        for x, y in stones:
            dsu.union(x, y + 10001)

        components = set()

        for x, y in stones:
            components.add(dsu.find(x))

        return len(stones) - len(components)

        # Complexity analysis
        # Time : O(S * 4A)
        # Space : O(S)


def p2():
    # Problem 2 : POTD Geeksforgeeks Maximum Stone Removal - https://www.geeksforgeeks.org/problems/maximum-stone-removal-1662179442/1

    testcase = [
        [[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]], 5],
        [[[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]], 3],
    ]

    for line in testcase:
        [stones, expected] = line
        s2 = Solution2()
        result = s2.maxRemove(stones)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 23 of November 2025

    p1()

    p2()
