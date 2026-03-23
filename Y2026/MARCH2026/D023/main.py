from typing import List, Tuple


class Solution1:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        self.MOD = 10**9 + 7

        # initialize DP table
        self.dp = [
            [(float("-inf"), float("inf")) for _ in range(self.n)]
            for _ in range(self.m)
        ]

        def solve(i: int, j: int) -> Tuple[int, int]:
            # base case: bottom-right cell
            if i == self.m - 1 and j == self.n - 1:
                return (grid[i][j], grid[i][j])

            # already computed
            if self.dp[i][j] != (float("-inf"), float("inf")):
                return self.dp[i][j]

            max_val = float("-inf")
            min_val = float("inf")

            # Down
            if i + 1 < self.m:
                down_max, down_min = solve(i + 1, j)
                candidates = [grid[i][j] * down_max, grid[i][j] * down_min]
                max_val = max(max_val, *candidates)
                min_val = min(min_val, *candidates)

            # Right
            if j + 1 < self.n:
                right_max, right_min = solve(i, j + 1)
                candidates = [grid[i][j] * right_max, grid[i][j] * right_min]
                max_val = max(max_val, *candidates)
                min_val = min(min_val, *candidates)

            self.dp[i][j] = (max_val, min_val)

            return self.dp[i][j]

        max_prod, _ = solve(0, 0)

        return -1 if max_prod < 0 else max_prod % self.MOD

        # Complexity analysis
        # Time : O(M * N)
        # Space : O(M * N)


def p1():
    # Problem 1 : POTD Leetcode 1594. Maximum Non Negative Product in a Matrix - https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/description/?envType=daily-question&envId=2026-03-23

    testcase = [
        [
            [[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]],
            -1,
        ],
        [
            [[1, -2, 1], [1, -2, 1], [3, -4, 1]],
            8,
        ],
        [
            [[1, 3], [0, -4]],
            0,
        ],
    ]

    for line in testcase:
        [grid, expected] = line
        s1 = Solution1()
        result = s1.maxProductPath(grid)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def longestCycle(self, V, edges):
        # code here

        # adjacency - since at most 1 outgoing edge, store as array
        next_node = [-1] * V
        for u, v in edges:
            next_node[u] = v

        # 0 = unvisited, 1 = visiting, 2 = processed
        state = [0] * V

        max_cycle = -1

        for i in range(V):
            if state[i] != 0:
                continue

            curr = i
            step_map = {}  # node -> step index
            step = 0

            # traverse current path
            while curr != -1:
                if state[curr] == 2:
                    break

                if curr in step_map:
                    # cycle detected
                    cycle_length = step - step_map[curr]
                    max_cycle = max(max_cycle, cycle_length)
                    break

                step_map[curr] = step
                state[curr] = 1
                step += 1
                curr = next_node[curr]

            # mark all nodes in this path as processed
            for node in step_map:
                state[node] = 2

        return max_cycle

        # Complexity analysis
        # Time : O(V)
        # Space : O(V)


def p2():
    # Problem 2 : POTD Geeksforgeeks Length of Longest Cycle in a Graph - https://www.geeksforgeeks.org/problems/length-of-longest-cycle-in-a-graph/1

    testcase = [
        [7, [[0, 5], [1, 0], [2, 4], [3, 1], [4, 6], [5, 6], [6, 3]], 5],
        [8, [[0, 1], [1, 2], [2, 3], [3, 0], [4, 1], [5, 4], [6, 2], [7, 6]], 4],
    ]

    for line in testcase:
        [V, edges, expected] = line
        s2 = Solution2()
        result = s2.longestCycle(V, edges)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 23 of March 2026

    p1()

    p2()
