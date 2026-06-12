from collections import deque
from typing import List


class Solution1:
    def assignEdgeWeights(
        self, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:

        MOD = 10**9 + 7
        n = len(edges) + 1
        LOG = n.bit_length()

        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        depth = [0] * (n + 1)
        up = [[0] * LOG for _ in range(n + 1)]

        q = deque([1])
        seen = [False] * (n + 1)
        seen[1] = True

        while q:
            node = q.popleft()

            for nxt in graph[node]:
                if seen[nxt]:
                    continue

                seen[nxt] = True
                depth[nxt] = depth[node] + 1
                up[nxt][0] = node

                for j in range(1, LOG):
                    up[nxt][j] = up[up[nxt][j - 1]][j - 1]

                q.append(nxt)

        powers = [1] * n
        for i in range(1, n):
            powers[i] = (powers[i - 1] * 2) % MOD

        def get_lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]
            bit = 0
            while diff:
                if diff & 1:
                    a = up[a][bit]
                diff >>= 1
                bit += 1

            if a == b:
                return a

            for j in range(LOG - 1, -1, -1):
                if up[a][j] != up[b][j]:
                    a = up[a][j]
                    b = up[b][j]

            return up[a][0]

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            ancestor = get_lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[ancestor]
            ans.append(powers[dist - 1])

        return ans

        # Complexity analysis
        # Time : O(N * Log(N) + Q * Log(N))
        # Space : O(N * Log(N))


def p1():
    # Problem 1 : POTD Leetcode 3559. Number of Ways to Assign Edge Weights II - https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/description/?envType=daily-question&envId=2026-06-12

    testcase = [
        [[[1, 2]], [[1, 1], [1, 2]], [0, 1]],
        [[[1, 2], [1, 3], [3, 4], [3, 5]], [[1, 4], [3, 4], [2, 5]], [2, 1, 4]],
    ]

    for line in testcase:
        [edges, queries, expected] = line
        s1 = Solution1()
        result = s1.assignEdgeWeights(edges, queries)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def kSubstr(self, s: str, k: int) -> bool:
        # code here

        N = len(s)
        if N % k != 0:
            return False

        substr_map = {}
        for i in range(0, N, k):
            sub = s[i : i + k]
            substr_map[sub] = substr_map.get(sub, 0) + 1

        if len(substr_map) == 1:
            return True

        if len(substr_map) != 2:
            return False

        for val in substr_map.values():
            if val == 1 or val == (N // k - 1):
                return True

        return False

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Check Repeated Substring with K Replacements - https://www.geeksforgeeks.org/problems/check-if-a-string-is-repetition-of-its-substring-of-k-length3302/1

    testcase = [
        ["abcbedabcabc", 3, True],
        ["bdac", 2, True],
        ["abcdabcd", 2, False],
    ]

    for line in testcase:
        [s, k, expected] = line
        s2 = Solution2()
        result = s2.kSubstr(s, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 12 of June 2026

    p1()

    p2()
