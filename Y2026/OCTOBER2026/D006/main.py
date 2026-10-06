from collections import deque
import heapq
from typing import Any, Optional


class Solution1:
    def minAddToMakeValid(self, s: str) -> int:
        adds = 0
        stack = []

        for c in s:
            if c == "(":
                stack.append(c)
            elif stack:
                stack.pop()
            else:
                adds += 1

        adds += len(stack)

        return adds

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 921. Minimum Add to Make Parentheses Valid - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/?envType=daily-question&envId=2026-10-06

    testcase = [
        ["())", 1],
        ["(((", 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minAddToMakeValid(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def longIncPath(self, matrix: list[list[int]], n: int, m: int) -> int:
        # code here

        DELTA_DIRECTIONS = [
            (-1, 0),
            (0, +1),
            (+1, 0),
            (0, -1),
        ]

        memo = [[0] * m for _ in range(n)]

        def solve(ri: int, ci: int) -> int:
            if memo[ri][ci] != 0:
                return memo[ri][ci]

            path_len = 0

            for rc, cc in DELTA_DIRECTIONS:
                nri = ri + rc
                nci = ci + cc

                # invalid coordinates
                if nri < 0 or nri >= n or nci < 0 or nci >= m:
                    continue

                # smaller
                if matrix[nri][nci] <= matrix[ri][ci]:
                    continue

                path_len = max(path_len, solve(nri, nci))

            memo[ri][ci] = 1 + path_len

            return memo[ri][ci]

        ans = -1

        for ri in range(n):
            for ci in range(m):
                ans = max(ans, solve(ri, ci))

        return ans

        # Complexity analysis
        # Time : O(N*M)
        # Space : O(N*M)


def p2():
    # Problem 2 : POTD Geeksforgeeks Longest Increasing Path in Matrix - https://www.geeksforgeeks.org/problems/longest-increasing-path-in-a-matrix/1

    testcase = [
        [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            3,
            3,
            5,
        ],
        [
            [[3, 4, 5], [6, 2, 6], [2, 2, 1]],
            3,
            3,
            4,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.longIncPath(*inputs)
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
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        result = []

        queue: deque[TreeNode] = deque()

        if root:
            queue.append(root)

        while queue:
            N = len(queue)

            level_result = []

            for _ in range(N):
                node = queue.popleft()

                level_result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level_result)

        return result

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 102. Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            TreeNode.from_list([3, 9, 20, None, None, 15, 7]),
            [[3], [9, 20], [15, 7]],
        ],
        [
            TreeNode.from_list([1]),
            [[1]],
        ],
        [
            TreeNode.from_list([]),
            [],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.levelOrder(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_queue: list[int] = []
        for stone_weight in stones:
            heapq.heappush(max_queue, -stone_weight)

        while len(max_queue) > 1:

            high1 = -heapq.heappop(max_queue)
            high2 = -heapq.heappop(max_queue)

            diff = abs(high1 - high2)

            if diff != 0:
                heapq.heappush(max_queue, -diff)

        return -max_queue[0] if max_queue else 0

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p4():
    # Problem 4 : NC150 Leetcode 1046. Last Stone Weight - https://leetcode.com/problems/last-stone-weight/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[2, 7, 4, 1, 8, 1], 1],
        [[1], 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.lastStoneWeight(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 6 of October 2026

    p1()

    p2()

    p3()

    p4()
