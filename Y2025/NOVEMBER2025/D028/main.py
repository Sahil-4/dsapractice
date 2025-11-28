from typing import List


class Solution1:
    def maxKDivisibleComponents(self, n, edges, values, k):
        self.adj = [[] for _ in range(n)]
        self.values = values
        self.k = k
        self.answer = 0

        for a, b in edges:
            self.adj[a].append(b)
            self.adj[b].append(a)

        self._dfs(0, -1)

        return self.answer

    def _dfs(self, node, parent):
        subtree_sum = self.values[node]

        for neighbor in self.adj[node]:
            if neighbor == parent:
                continue
            subtree_sum += self._dfs(neighbor, node)

        if subtree_sum % self.k == 0:
            self.answer += 1
            return 0

        return subtree_sum


def p1():
    # Problem 1 : POTD Leetcode 2872. Maximum Number of K-Divisible Components - https://leetcode.com/problems/maximum-number-of-k-divisible-components/description/?envType=daily-question&envId=2025-11-28

    testcase = [
        [5, [[0, 2], [1, 2], [1, 3], [2, 4]], [1, 8, 1, 4, 4], 6, 2],
        [
            7,
            [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]],
            [3, 0, 6, 1, 5, 2, 1],
            3,
            3,
        ],
    ]

    for line in testcase:
        [n, edges, values, k, expected] = line
        s1 = Solution1()
        result = s1.maxKDivisibleComponents(n, edges, values, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution2:
    def xor_upto(self, x):
        if x % 4 == 0:
            return x
        if x % 4 == 1:
            return 1
        if x % 4 == 2:
            return x + 1
        return 0  # x % 4 == 3

    def subsetXOR(self, n: int) -> List[int]:
        # code here
        X = self.xor_upto(n)
        R = X ^ n

        if R == 0:
            return list(range(1, n + 1))

        # Remove exactly R
        return [i for i in range(1, n + 1) if i != R]

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Subset XOR - https://www.geeksforgeeks.org/problems/subset-xor--175953/1

    testcase = [
        [4, [1, 2, 3, 4]],
        [3, [1, 2]],
        [2, [2]],
        [12, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],
        [15, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]],
    ]

    for line in testcase:
        [n, expected] = line
        s2 = Solution2()
        result = s2.subsetXOR(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 28 of November 2025

    p1()

    p2()
