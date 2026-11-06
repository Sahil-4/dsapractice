from collections import defaultdict, deque
from typing import Any, Optional


class Solution1:
    def countServers(
        self, n: int, logs: list[list[int]], x: int, queries: list[int]
    ) -> list[int]:
        Q = len(queries)
        L = len(logs)

        # sort logs = [[server_id, time], ...] based on time
        logs = sorted(logs, key=lambda log: log[1])

        # sort queries, preserve index for answer array
        sorted_queries = sorted(enumerate(queries), key=lambda query: query[1])

        answer = [0] * Q

        server_counts = defaultdict(int)
        left = 0
        right = 0

        for query_index, query_time in sorted_queries:

            low_time = query_time - x
            high_time = query_time

            # within upper bound
            while right < L and logs[right][1] <= high_time:
                server_counts[logs[right][0]] += 1
                right += 1

            # less then lower bound
            while left < L and logs[left][1] < low_time:
                server_id = logs[left][0]
                server_counts[server_id] -= 1
                if server_counts[server_id] == 0:
                    del server_counts[server_id]
                left += 1

            answer[query_index] = n - len(server_counts)

        return answer

        # Complexity analysis
        # Time : O(Q * Log(Q) + L * Log(L))
        # Space : O(Q + N)


def p1():
    # Problem 1 : POTD Leetcode 2747. Count Zero Request Servers - https://leetcode.com/problems/count-zero-request-servers/description/?envType=daily-question&envId=2026-11-06

    testcase = [
        [3, [[1, 3], [2, 6], [1, 5]], 5, [10, 11], [1, 2]],
        [3, [[2, 4], [2, 1], [1, 2], [3, 1]], 2, [3, 4], [0, 1]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.countServers(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countBT(self, h: int) -> int:
        # code here
        # h = 0 # T(0) = 0
        # h = 1 # T(1) = 1
        # h = 2 # T(2) = 3
        # h = 3 # T(3) = 15
        # T(h) = (h-1)^2 + 2*((h-1) * (h-2))

        MOD = 1000000007

        prev2 = 1  # T(0)
        prev1 = 1  # T(1)

        for _ in range(2, h + 1):
            curr = ((prev1 * prev1 % MOD) + (2 * prev1 * prev2 % MOD)) % MOD
            prev2 = prev1
            prev1 = curr

        return prev1

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Balanced Binary Tree Counter - https://www.geeksforgeeks.org/problems/bbt-counter4914/1

    testcase = [
        [1, 1],
        [2, 3],
        [3, 15],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.countBT(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_list(arr: list[Optional[int]]) -> Optional["TreeNode"]:
        if not arr or arr[0] is None:
            return None

        root = TreeNode(arr[0])
        q: deque[TreeNode] = deque([root])

        i = 1
        while q and i < len(arr):
            node = q.popleft()

            val = arr[i] if i < len(arr) else None
            if val is not None:
                node.left = TreeNode(val)
                q.append(node.left)
            i += 1

            val = arr[i] if i < len(arr) else None
            if val is not None:
                node.right = TreeNode(val)
                q.append(node.right)
            i += 1

        return root

    def to_list(self) -> list[Any]:
        result = []
        q: deque[Optional[TreeNode]] = deque([self])

        while q:
            node = q.popleft()

            if node:
                result.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                result.append(None)

        # remove trailing None values
        while result and result[-1] is None:
            result.pop()

        return result


class Solution3:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            N = len(queue)

            for i in range(N):
                node = queue.popleft()

                if i == 0:
                    result.append(node.val)

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return result

        # Complexity analysis
        # Time : O(N)
        # Space : O(W)


def p3():
    # Problem 3 : NC150 Leetcode 199. Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            TreeNode.from_list([1, 2, 3, None, 5, None, 4]),
            [1, 3, 4],
        ],
        [
            TreeNode.from_list([1, 2, 3, 4, None, None, None, 5]),
            [1, 3, 4, 5],
        ],
        [
            TreeNode.from_list([1, None, 3]),
            [1, 3],
        ],
        [
            TreeNode.from_list([]),
            [],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.rightSideView(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def numIslands(self, grid: list[list[str]]) -> int:
        M = len(grid)
        N = len(grid[0])

        visited = [[False] * N for _ in range(M)]

        def span(r: int, c: int):

            if r < 0 or r >= M or c < 0 or c >= N:
                return

            if visited[r][c] == True or grid[r][c] != "1":
                return

            visited[r][c] = True

            span(r - 1, c)
            span(r, c + 1)
            span(r + 1, c)
            span(r, c - 1)

        island_count = 0

        for r in range(M):
            for c in range(N):

                if grid[r][c] != "1" or visited[r][c] == True:
                    continue

                island_count += 1
                span(r, c)

        return island_count

        # Complexity analysis
        # Time : O(M*N)
        # Space : O(M*N)


def p4():
    # Problem 4 : NC150 Leetcode 200. Number of Islands - https://leetcode.com/problems/number-of-islands/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ],
        [
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.numIslands(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 6 of November 2026

    p1()

    p2()

    p3()

    p4()
