class Solution1:
    def minMoves2(self, nums: list[int]) -> int:
        # sort nums
        # find mid value (any)
        # calculate sum of abs(num - mid)

        nums.sort()

        moves = 0

        mid_index = len(nums) // 2

        for num in nums:
            moves += abs(num - nums[mid_index])

        return moves

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 462. Minimum Moves to Equal Array Elements II - https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/?envType=daily-question&envId=2026-11-02

    testcase = [
        [[1, 2, 3], 2],
        [[1, 10, 2, 9], 16],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minMoves2(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def largestSumCycle(self, edges: list[int]) -> int:
        # code here

        N = len(edges)

        visited = [False] * N
        max_cycle_sum = -1

        for i in range(N):
            if visited[i]:
                continue

            curr = i
            path = []
            node_step = {}
            step = 0

            # traverse path iteratively
            while curr != -1 and not visited[curr]:
                visited[curr] = True
                node_step[curr] = step
                path.append(curr)
                step += 1
                curr = edges[curr]

            # if curr was visited during THIS traversal, we found a cycle
            if curr != -1 and curr in node_step:
                cycle_start_index = node_step[curr]
                cycle_sum = sum(path[cycle_start_index:])
                max_cycle_sum = max(max_cycle_sum, cycle_sum)

        return max_cycle_sum

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Largest Sum Cycle - https://www.geeksforgeeks.org/problems/largest-sum-cycle--170645/1

    testcase = [
        [[1, 2, 0, -1], 3],
        [[2, 0, -1, 2], -1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.largestSumCycle(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class DSU:

    def __init__(self):
        self.parent = {}

    def find(self, x: int) -> int:
        if x not in self.parent:
            self.parent[x] = x

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        self.parent[self.find(x)] = self.find(y)


class Solution3:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        redundant_connection = []

        # use union find
        dsu = DSU()

        for edge in edges:
            u, v = edge

            if dsu.find(u) == dsu.find(v):
                redundant_connection = [u, v]
                break

            dsu.union(u, v)

        return redundant_connection

        # Complexity analysis
        # Time : O(N * 4A)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 684. Redundant Connection - https://leetcode.com/problems/redundant-connection/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[[1, 2], [1, 3], [2, 3]], [2, 3]],
        [[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.findRedundantConnection(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 2 of November 2026

    p1()

    p2()

    p3()
