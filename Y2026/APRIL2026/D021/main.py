from math import gcd
from collections import defaultdict
from typing import List


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        px, py = self.find(x), self.find(y)
        if px == py:
            return

        # Union by rank
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1


class Solution1:
    def minimumHammingDistance(
        self, source: List[int], target: List[int], allowedSwaps: List[List[int]]
    ) -> int:

        n = len(source)
        dsu = DSU(n)

        # Step 1: Build connected components via union
        for u, v in allowedSwaps:
            dsu.union(u, v)

        # Step 2: Group indices by root
        groups = defaultdict(list)
        for i in range(n):
            root = dsu.find(i)
            groups[root].append(i)

        # Step 3: Compute minimum Hamming distance
        ans = 0

        for indices in groups.values():
            freq = defaultdict(int)

            # Count source values
            for i in indices:
                freq[source[i]] += 1

            # Match target values
            for i in indices:
                if freq[target[i]] > 0:
                    freq[target[i]] -= 1
                else:
                    ans += 1

        return ans

        # Complexity analysis
        # Time : O(N + M)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1722. Minimize Hamming Distance After Swap Operations - https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/?envType=daily-question&envId=2026-04-21

    testcase = [
        [[1, 2, 3, 4], [2, 1, 4, 5], [[0, 1], [2, 3]], 1],
        [[1, 2, 3, 4], [1, 3, 2, 4], [], 2],
        [[5, 1, 2, 4, 3], [1, 5, 4, 2, 3], [[0, 4], [4, 2], [1, 3], [1, 4]], 0],
    ]

    for line in testcase:
        [source, target, allowedSwaps, expected] = line
        s1 = Solution1()
        result = s1.minimumHammingDistance(source, target, allowedSwaps)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def pour(self, source: int, destination: int, d_cap: int) -> int:

        source_cap = source
        destination_cap = 0

        step = 1

        while (source_cap != d_cap) and (destination_cap != d_cap):

            temp = min(source_cap, destination - destination_cap)

            destination_cap += temp
            source_cap -= temp
            step += 1

            if source_cap == d_cap or destination_cap == d_cap:
                break

            if source_cap == 0:
                source_cap = source
                step += 1

            if destination_cap == destination:
                destination_cap = 0
                step += 1

        return step

    def minSteps(self, m: int, n: int, d: int) -> int:
        # Code here

        if m > n:
            m, n = n, m

        if d > n:
            return -1

        if d % gcd(m, n) != 0:
            return -1

        return min(self.pour(n, m, d), self.pour(m, n, d))

        # Complexity analysis
        # Time : O(N + M)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Two water Jug problem - https://www.geeksforgeeks.org/problems/two-water-jug-problem3402/1

    testcase = [
        [3, 5, 4, 6],
        [8, 56, 46, -1],
    ]

    for line in testcase:
        [m, n, d, expected] = line
        s2 = Solution2()
        result = s2.minSteps(m, n, d)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 21 of April 2026

    p1()

    p2()
