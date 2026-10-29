import heapq


class Solution1:
    def palindromePath(
        self, n: int, edges: list[list[int]], s: str, queries: list[str]
    ) -> list[bool]:
        # build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = 1
        while (1 << LOG) <= n:
            LOG += 1

        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        in_time = [0] * n
        out_time = [0] * n
        timer = 0

        # iterative DFS for Euler Tour and Binary Lifting table
        stack = [(0, -1, 0, False)]  # (node, parent, depth, is_visited)
        while stack:
            u, p, d, is_visited = stack.pop()
            if not is_visited:
                timer += 1
                in_time[u] = timer
                depth[u] = d
                up[u][0] = p if p != -1 else 0

                for i in range(1, LOG):
                    up[u][i] = up[up[u][i - 1]][i - 1]

                stack.append((u, p, d, True))
                for v in graph[u]:
                    if v != p:
                        stack.append((v, u, d + 1, False))
            else:
                out_time[u] = timer

        # fenwick Tree (Binary Indexed Tree) for Range XOR Updates and Point Queries
        bit = [0] * (n + 2)

        def add(idx, val):
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)

        def update_range(L, R, val):
            if val == 0:
                return
            add(L, val)
            add(R + 1, val)

        def query_point(idx):
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        # initialize the BIT with the starting string characters
        chars = list(s)
        for i in range(n):
            val = 1 << (ord(chars[i]) - 97)
            update_range(in_time[i], out_time[i], val)

        # process queries
        results = []
        for query in queries:
            parts = query.split()
            if parts[0] == "query":
                u, v = int(parts[1]), int(parts[2])

                # fetch masks and compute path
                lca = get_lca(u, v)
                mask_u = query_point(in_time[u])
                mask_v = query_point(in_time[v])
                char_lca = chars[lca]

                # path XOR = mask(u) ^ mask(v) ^ char(LCA)
                path_mask = mask_u ^ mask_v ^ (1 << (ord(char_lca) - 97))

                # palindromic anagram condition: at most 1 bit is set
                is_palindrome = (path_mask & (path_mask - 1)) == 0
                results.append(is_palindrome)

            elif parts[0] == "update":
                u, c = int(parts[1]), parts[2]
                old_c = chars[u]
                if old_c != c:
                    # XOR out the old character and XOR in the new one
                    diff = (1 << (ord(old_c) - 97)) ^ (1 << (ord(c) - 97))
                    update_range(in_time[u], out_time[u], diff)
                    chars[u] = c

        return results

        # Complexity Analysis
        # Time : O(N * Log(N) + Q * Log(N))
        # Space : O(N * Log(N) + Q * Log(N))


def p1():
    # Problem 1 : POTD Leetcode 3841. Palindromic Path Queries in a Tree - https://leetcode.com/problems/palindromic-path-queries-in-a-tree/description/?envType=daily-question&envId=2026-10-29

    testcase = [
        [
            3,
            [
                [0, 1],
                [1, 2],
            ],
            "aac",
            ["query 0 2", "update 1 b", "query 0 2"],
            [True, False],
        ],
        [
            4,
            [
                [0, 1],
                [0, 2],
                [0, 3],
            ],
            "abca",
            ["query 1 2", "update 0 b", "query 2 3", "update 3 a", "query 1 3"],
            [False, False, True],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.palindromePath(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minComputation(self, files):
        # code here

        t = 0
        heap = []

        for f in files:
            heapq.heappush(heap, f)

        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)

            t += a + b
            heapq.heappush(heap, a + b)

        return t

        # Complexity Analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Optimal File Merge - https://www.geeksforgeeks.org/problems/optimal-file-merge/1

    testcase = [
        [[3, 2, 4], 14],
        [[2, 3, 6, 5, 7, 4], 68],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minComputation(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class MinStack:

    def __init__(self):
        self.current_min = None
        self.stack = []

    def push(self, value: int) -> None:
        if self.current_min == None or value < self.current_min:
            self.current_min = value
        self.stack.append([value, self.current_min])

    def pop(self) -> None:
        if not self.stack:
            return

        self.stack.pop()
        if self.stack:
            self.current_min = self.stack[-1][1]
        else:
            self.current_min = None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return -1

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return -1


def p3():
    # Problem 3 : NC150 Leetcode 155. Min Stack - https://leetcode.com/problems/min-stack/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
            [[], [-2], [0], [-3], [], [], [], []],
            [None, None, None, None, -3, None, 0, -2],
        ],
        [
            ["MinStack", "push", "top", "getMin", "push", "top", "getMin"],
            [[], [-1], [], [], [1], [], []],
            [None, None, -1, -1, None, 1, -1],
        ],
    ]

    for line in testcase:
        [inputs, args, output] = line
        s3 = MinStack()
        result: list = [None]
        for i, input_val in enumerate(inputs):
            if input_val == "push":
                s3.push(args[i][0])
                result.append(None)
            elif input_val == "pop":
                s3.pop()
                result.append(None)
            elif input_val == "top":
                result.append(s3.top())
            elif input_val == "getMin":
                result.append(s3.getMin())
        assert result == output, f"Test failed: expected {output}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 29 of October 2026

    p1()

    p2()

    p3()
