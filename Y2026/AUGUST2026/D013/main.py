class Solution1:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: list[int]
    ) -> list[int]:
        N = len(s)

        # node:
        # (left_char, right_char, prefix, suffix, best, length)
        tree: list = [None] * (4 * N)

        def make_leaf(ch: str):
            return (ch, ch, 1, 1, 1, 1)

        def merge(left, right):
            if left is None:
                return right
            if right is None:
                return left

            lch, rch, lp, ls, lb, llen = left
            r_lch, r_rch, rp, rs, rb, rlen = right

            prefix = lp
            suffix = rs
            best = max(lb, rb)

            # run can cross the boundary only
            # if the two boundary characters are equal
            if rch == r_lch:
                cross = ls + rp
                best = max(best, cross)

                if lp == llen:
                    prefix = llen + rp

                if rs == rlen:
                    suffix = rlen + ls

            return (
                lch,
                r_rch,
                prefix,
                suffix,
                best,
                llen + rlen,
            )

        def build(node, lo, hi):
            if lo == hi:
                tree[node] = make_leaf(s[lo])
                return

            mid = (lo + hi) // 2
            build(node * 2, lo, mid)
            build(node * 2 + 1, mid + 1, hi)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, lo, hi, index, ch):
            if lo == hi:
                tree[node] = make_leaf(ch)
                return

            mid = (lo + hi) // 2

            if index <= mid:
                update(node * 2, lo, mid, index, ch)
            else:
                update(node * 2 + 1, mid + 1, hi, index, ch)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, N - 1)

        lengths = []

        for ch, index in zip(queryCharacters, queryIndices):
            update(1, 0, N - 1, index, ch)
            lengths.append(tree[1][4])

        return lengths

        # Complexity analysis
        # Time : O(N + K * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2213. Longest Substring of One Repeating Character - https://leetcode.com/problems/longest-substring-of-one-repeating-character/description/?envType=daily-question&envId=2026-08-13

    testcase = [
        ["babacc", "bcb", [1, 3, 3], [3, 3, 4]],
        ["abyzz", "aa", [2, 1], [2, 3]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.longestRepeating(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


INF = -(2**31)


class Solution2:
    def maxDistance(self, V: int, src: int, edges: list[list[int]]):
        # code here

        # adjacency list
        graph = [[] for _ in range(V)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # topological sort using DFS
        visited = [False] * V
        topo = []

        def dfs(u):
            visited[u] = True

            for v, _ in graph[u]:
                if not visited[v]:
                    dfs(v)

            # add after processing all descendants
            topo.append(u)

        for vertex in range(V):
            if not visited[vertex]:
                dfs(vertex)

        # reverse post-order gives topological order
        topo.reverse()

        # longest distance from src
        distance = [INF] * V
        distance[src] = 0

        for u in topo:
            # ignore unreachable vertices from src
            if distance[u] == INF:
                continue

            for v, weight in graph[u]:
                distance[v] = max(distance[v], distance[u] + weight)

        return distance

        # Complexity analysis
        # Time : O(V + E)
        # Space : O(V + E)


def p2():
    # Problem 2 : POTD Geeksforgeeks Longest Path in a Directed Acyclic Graph - https://www.geeksforgeeks.org/problems/longest-path-in-a-directed-acyclic-graph/1

    testcase = [
        [
            4,
            0,
            [[0, 1, 1], [0, 2, 1], [1, 2, 5], [3, 1, 2], [3, 2, -1]],
            [0, 1, 6, INF],
        ],
        [
            5,
            1,
            [[0, 1, 1], [0, 2, 2], [1, 4, 4], [3, 2, -1], [4, 2, 3], [4, 3, 6]],
            [INF, 0, 9, 10, 4],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxDistance(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 13 of August 2026

    p1()

    p2()
