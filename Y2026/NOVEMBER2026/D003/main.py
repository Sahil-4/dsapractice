class Solution1:
    def minMoves(self, nums: list[int]) -> int:
        moves = 0
        max_element = max(nums)

        for num in nums:
            moves += max_element - num

        return moves

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3736. Minimum Moves to Equal Array Elements III - https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/description/?envType=daily-question&envId=2026-11-03

    testcase = [
        [[2, 1, 3], 3],
        [[4, 4, 5], 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minMoves(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class DSU:

    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x: int) -> int:
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, x: int, y: int) -> int:
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return 0

        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx

        paths = self.size[rx] * self.size[ry]
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        return paths


class Solution2:

    def maximumWeight(
        self, n: int, edges: list[list[int]], queries: list[int]
    ) -> list[int]:
        E = len(edges)
        Q = len(queries)

        sorted_queries = sorted(zip(queries, range(Q)))
        sorted_edges = sorted(edges, key=lambda edge: edge[2])

        dsu = DSU(n)

        results = [0] * Q
        total_paths = 0
        edge_ptr = 0

        for query, original_index in sorted_queries:
            while edge_ptr < E and sorted_edges[edge_ptr][2] <= query:
                u, v = sorted_edges[edge_ptr][0], sorted_edges[edge_ptr][1]
                total_paths += dsu.union(u, v)
                edge_ptr += 1

            results[original_index] = total_paths

        return results

        # Complexity analysis
        # Time : O(N * Log(N) + Q * Log(Q))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count Tree Paths With Limited Max Edge Weight - https://www.geeksforgeeks.org/problems/possible-paths--141628/1

    testcase = [
        [
            3,
            [[1, 2, 1], [2, 3, 4]],
            [3],
            [1],
        ],
        [
            7,
            [[1, 2, 3], [2, 3, 1], [2, 4, 9], [3, 6, 7], [3, 5, 8], [5, 7, 4]],
            [1, 3, 5],
            [1, 3, 4],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maximumWeight(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        max_island_area = 0

        visited = [[False] * N for _ in range(M)]

        def get_island_area(r: int, c: int) -> int:

            # out of bound
            if r < 0 or r >= M or c < 0 or c >= N:
                return 0

            # already visited
            if visited[r][c] == True:
                return 0

            # not a land cell
            if grid[r][c] != 1:
                return 0

            # mark current cell visited
            visited[r][c] = True

            # current cell
            area = 1

            # top
            area += get_island_area(r - 1, c)

            # right
            area += get_island_area(r, c + 1)

            # bottom
            area += get_island_area(r + 1, c)

            # left
            area += get_island_area(r, c - 1)

            return area

        for r in range(M):
            for c in range(N):
                if grid[r][c] != 1 or visited[r][c] == True:
                    continue

                max_island_area = max(max_island_area, get_island_area(r, c))

        return max_island_area

        # Complexity analysis
        # Time : O(M * N)
        # Space : O(M * N)


def p3():
    # Problem 3 : NC150 Leetcode 695. Max Area of Island - https://leetcode.com/problems/max-area-of-island/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            ],
            6,
        ],
        [
            [
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            0,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.maxAreaOfIsland(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 3 of November 2026

    p1()

    p2()

    p3()
