from typing import List


class Solution1:
    def minMoves(self, nums: List[int], limit: int) -> int:
        N = len(nums)

        # diff[c] - change in required operations when target sum moves to c
        diff = [0] * (2 * limit + 2)

        for i in range(N // 2):
            a = min(nums[i], nums[N - 1 - i])
            b = max(nums[i], nums[N - 1 - i])

            # Initially assume 2 operations for every target sum
            # in [2, 2 * limit]
            diff[2] += 2

            # [a + 1, ...] -> can reduce to 1 operation
            diff[a + 1] -= 1

            # [a + b] -> can reduce to 0 operation
            diff[a + b] -= 1

            # [a + b + 1, ...] -> back to 1 operation
            diff[a + b + 1] += 1

            # [b + limit + 1, ...] -> back to 2 operations
            diff[b + limit + 1] += 1

        min_ops = N
        current_ops = 0

        # prefix sum over all possible target sums
        for target_sum in range(2, 2 * limit + 1):
            current_ops += diff[target_sum]
            min_ops = min(min_ops, current_ops)

        return min_ops

        # Complexity analysis
        # Time : O(N + limit)
        # Space : O(limit)


def p1():
    # Problem 1 : POTD Leetcode 1674. Minimum Moves to Make Array Complementary - https://leetcode.com/problems/minimum-moves-to-make-array-complementary/description/?envType=daily-question&envId=2026-05-13

    testcase = [
        [[1, 2, 4, 3], 4, 1],
        [[1, 2, 2, 1], 2, 2],
        [[1, 2, 1, 2], 2, 0],
    ]

    for line in testcase:
        [nums, limit, expected] = line
        s1 = Solution1()
        result = s1.minMoves(nums, limit)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findMotherVertex(self, V: int, edges: list[list[int]]) -> int:
        # code here

        # graph
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)

        # dfs
        def dfs(node, visited):
            visited[node] = True

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, visited)

        # find candidate
        visited = [False] * V
        candidate = -1

        for node in range(V):
            if not visited[node]:
                dfs(node, visited)
                candidate = node

        # verify
        visited = [False] * V
        dfs(candidate, visited)

        if all(visited):
            return candidate

        return -1

        # Complexity analysis
        # Time : O(V + E)
        # Space : O(V)


def p2():
    # Problem 2 : POTD Geeksforgeeks Mother Vertex - https://www.geeksforgeeks.org/problems/mother-vertex/1

    testcase = [
        [5, [[0, 2], [0, 3], [1, 0], [2, 1], [3, 4]], 0],
        [3, [[0, 1], [2, 1]], -1],
    ]

    for line in testcase:
        [V, edges, expected] = line
        s2 = Solution2()
        result = s2.findMotherVertex(V, edges)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 13 of May 2026

    p1()

    p2()
