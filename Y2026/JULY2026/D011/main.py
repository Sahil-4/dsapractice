from collections import deque


class Solution1:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        answer = 0

        for start in range(n):

            if visited[start]:
                continue

            queue = deque([start])
            visited[start] = True

            nodes = 0
            degree_sum = 0

            while queue:

                node = queue.popleft()

                nodes += 1
                degree_sum += len(graph[node])

                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        queue.append(nei)

            edge_count = degree_sum // 2

            if edge_count == nodes * (nodes - 1) // 2:
                answer += 1

        return answer

        # Complexity analysis
        # Time : O(N + E)
        # Space : O(N + E)


def p1():
    # Problem 1 : POTD Leetcode 2685. Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/description/?envType=daily-question&envId=2026-07-11

    testcase = [
        [6, [[0, 1], [0, 2], [1, 2], [3, 4]], 3],
        [6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]], 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.countCompleteComponents(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def longestPath(
        self, mat: list[list[int]], xs: int, ys: int, xd: int, yd: int
    ) -> int:
        # code here

        rows = len(mat)
        cols = len(mat[0])

        if mat[xs][ys] == 0 or mat[xd][yd] == 0:
            return -1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r: int, c: int) -> int:

            # reached destination
            if r == xd and c == yd:
                return 0

            # invalid / blocked / already visited
            if r < 0 or r >= rows or c < 0 or c >= cols or mat[r][c] == 0:
                return -1

            # mark visited
            mat[r][c] = 0

            longest = -1

            for dr, dc in directions:
                length = dfs(r + dr, c + dc)

                if length != -1:
                    longest = max(longest, length + 1)

            # backtrack
            mat[r][c] = 1

            return longest

        return dfs(xs, ys)

        # Complexity analysis
        # Time : O(4^(N*M)) (worst case, backtracking)
        # Space : O(N*M) (recursion stack)


def p2():
    # Problem 2 : POTD Geeksforgeeks Longest Possible Route in a Matrix with Hurdles - https://www.geeksforgeeks.org/problems/longest-possible-route-in-a-matrix-with-hurdles/1

    testcase = [
        [
            [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ],
            0,
            0,
            1,
            7,
            24,
        ],
        [
            [
                [1, 0, 0, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 1, 1, 0, 0],
            ],
            0,
            3,
            2,
            2,
            -1,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.longestPath(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 11 of July 2026

    p1()

    p2()
