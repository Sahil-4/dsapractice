from typing import List


class Solution1:
    # compute LCP matrix
    def longest_common_prefix_matrix(self, s: str) -> List[List[int]]:
        n = len(s)
        result = [[0] * n for _ in range(n)]

        # last row and column
        for j in range(n):
            val = 1 if s[j] == s[n - 1] else 0
            result[n - 1][j] = val
            result[j][n - 1] = val

        # rest of the matrix bottom up
        for i in range(n - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if s[i] == s[j]:
                    result[i][j] = 1 + result[i + 1][j + 1]
                else:
                    result[i][j] = 0

        return result

    def findTheString(self, lcp: List[List[int]]) -> str:
        N = len(lcp)

        # init result string with 'a...'
        result = ["a"] * N

        for i in range(1, N):
            # forbidden
            not_equal = [False] * 26
            matched = False

            for j in range(i):
                if lcp[j][i] == 0:
                    not_equal[ord(result[j]) - ord("a")] = True
                    continue

                matched = True
                result[i] = result[j]
                break

            if matched:
                continue

            # assign smallest possible character
            for j in range(26):
                if not_equal[j]:
                    continue
                result[i] = chr(ord("a") + j)
                break

        result_str = "".join(result)

        # validate by recomputing LCP
        if self.longest_common_prefix_matrix(result_str) == lcp:
            return result_str

        return ""

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(N * N)


def p1():
    # Problem 1 : POTD Leetcode 2573. Find the String with LCP - https://leetcode.com/problems/find-the-string-with-lcp/description/?envType=daily-question&envId=2026-03-28

    testcase = [
        [
            [[4, 0, 2, 0], [0, 3, 0, 1], [2, 0, 2, 0], [0, 1, 0, 1]],
            "abab",
        ],
        [
            [[4, 3, 2, 1], [3, 3, 2, 1], [2, 2, 2, 1], [1, 1, 1, 1]],
            "aaaa",
        ],
        [
            [[4, 3, 2, 1], [3, 3, 2, 1], [2, 2, 2, 1], [1, 1, 1, 3]],
            "",
        ],
    ]

    for line in testcase:
        [lcp, expected] = line
        s1 = Solution1()
        result = s1.findTheString(lcp)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def articulationPoints(self, V, edges):

        # adjacency list
        adjacency_list = [[] for _ in range(V)]
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        visited = [False] * V
        insertion_time = [0] * V
        lowest_time = [0] * V

        articulation_points = set()
        timer = 0

        def dfs(u, parent):
            nonlocal timer

            visited[u] = True
            insertion_time[u] = lowest_time[u] = timer
            timer += 1

            children = 0

            for v in adjacency_list[u]:
                if v == parent:
                    continue

                if visited[v]:
                    # back edge
                    lowest_time[u] = min(lowest_time[u], insertion_time[v])
                else:
                    children += 1
                    dfs(v, u)

                    # update low time
                    lowest_time[u] = min(lowest_time[u], lowest_time[v])

                    # articulation point condition (non-root)
                    if lowest_time[v] >= insertion_time[u] and parent != -1:
                        articulation_points.add(u)

            # root node condition
            if parent == -1 and children > 1:
                articulation_points.add(u)

        # DFS for all components
        for i in range(V):
            if not visited[i]:
                dfs(i, -1)

        # result
        if not articulation_points:
            return [-1]

        return sorted(articulation_points)

        # Complexity analysis
        # Time : O(V + E)
        # Space : O(V + E)


def p2():
    # Problem 2 : POTD Geeksforgeeks Articulation Point - II - https://www.geeksforgeeks.org/problems/articulation-point2616/1

    testcase = [
        [
            5,
            [[0, 1], [1, 4], [4, 3], [4, 2], [2, 3]],
            [1, 4],
        ],
        [
            4,
            [[0, 1], [0, 2]],
            [0],
        ],
    ]

    for line in testcase:
        [V, edges, expected] = line
        s2 = Solution2()
        result = s2.articulationPoints(V, edges)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 28 of March 2026

    p1()

    p2()
