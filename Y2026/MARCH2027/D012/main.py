from typing import List


# Disjoint Set Union
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return False

        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        elif self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        else:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1

        return True


class Solution1:
    def check(self, mid: int, n: int, edges: List[List[int]], k: int) -> bool:
        dsu = DSU(n)

        optional = []

        # mandatory edges
        for u, v, s, m in edges:
            if m == 1:
                if s < mid:
                    return False
                if not dsu.union(u, v):
                    return False
            else:
                optional.append((u, v, s))

        # pass1: no upgrade needed
        for u, v, s in optional:
            if s >= mid:
                dsu.union(u, v)

        # pass2: upgrade edges
        for u, v, s in optional:
            if s < mid and s * 2 >= mid:
                if dsu.find(u) != dsu.find(v):
                    if k == 0:
                        return False
                    dsu.union(u, v)
                    k -= 1

        root = dsu.find(0)
        for i in range(1, n):
            if dsu.find(i) != root:
                return False

        return True

    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        result = -1
        l = 1
        r = 2 * 1e5

        while l <= r:
            mid = int((l + r) // 2)

            if self.check(mid, n, edges, k):
                result = mid
                l = mid + 1
            else:
                r = mid - 1

        return result

        # Complexity analysis
        # Time : O(N * Log(S))
        # Space : O(N + E)


def p1():
    # Problem 1 : POTD Leetcode 3600. Maximize Spanning Tree Stability with Upgrades - https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/description/?envType=daily-question&envId=2026-03-12

    testcase = [
        [
            3,
            [[0, 1, 2, 1], [1, 2, 3, 0]],
            1,
            2,
        ],
        [
            3,
            [[0, 1, 4, 0], [1, 2, 3, 0], [0, 2, 1, 0]],
            2,
            6,
        ],
        [
            3,
            [[0, 1, 1, 1], [1, 2, 1, 1], [2, 0, 1, 1]],
            0,
            -1,
        ],
        [
            3,
            [[0, 1, 27955, 0], [0, 2, 96441, 1], [1, 2, 13682, 1]],
            3,
            13682,
        ],
    ]

    for line in testcase:
        [n, edges, k, expected] = line
        s1 = Solution1()
        result = s1.maxStability(n, edges, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def kBitFlips(self, arr: List[int], k: int) -> int:
        # code here
        N = len(arr)

        count = 0
        prefix = [0] * (N + 2)

        for i in range(0, N - k + 1):
            if i > 0:
                prefix[i] += prefix[i - 1]

            if arr[i] == 0 and not (prefix[i] & 1):
                prefix[i] += 1
                prefix[i + k] -= 1
                count += 1

            if arr[i] == 1 and (prefix[i] & 1):
                prefix[i] += 1
                prefix[i + k] -= 1
                count += 1

        for i in range(N - k + 1, N):
            prefix[i] += prefix[i - 1]

            if arr[i] == 0 and not (prefix[i] & 1):
                return -1

            if arr[i] == 1 and (prefix[i] & 1):
                return -1

        return count

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum K Consecutive Bit Flips - https://www.geeksforgeeks.org/problems/minimum-number-of-k-consecutive-bit-flips--171650/1

    testcase = [
        [[1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1], 2, 4],
        [[0, 0, 1, 1, 1, 0, 0], 3, -1],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.kBitFlips(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 12 of March 2026

    p1()

    p2()
