from collections import defaultdict, deque
from typing import List, Optional


class Solution1:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])

        result = 0

        prev_row = [0] * N
        for r in range(M):
            curr_row = list(matrix[r])

            for c in range(N):
                if curr_row[c] == 1:
                    curr_row[c] += prev_row[c]

            sorted_row = sorted(curr_row, reverse=True)
            for c in range(N):
                base = c + 1
                height = sorted_row[c]

                result = max(result, base * height)

            prev_row = curr_row

        return result

        # Complexity analysis
        # Time : (M * N * Log(N))
        # Space : O(M * 2)


def p1():
    # Problem 1 : POTD Leetcode 1727. Largest Submatrix With Rearrangements - https://leetcode.com/problems/largest-submatrix-with-rearrangements/description/?envType=daily-question&envId=2026-03-17

    testcase = [
        [
            [
                [0, 0, 1],
                [1, 1, 1],
                [1, 0, 1],
            ],
            4,
        ],
        [
            [
                [1, 0, 1, 0, 1],
            ],
            3,
        ],
        [
            [
                [1, 1, 0],
                [1, 0, 1],
            ],
            2,
        ],
    ]

    for line in testcase:
        [matrix, expected] = line
        s1 = Solution1()
        result = s1.largestSubmatrix(matrix)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


# Definition for a binary tree node.
class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @staticmethod
    def from_list(arr: List) -> Optional["Node"]:
        if not arr:
            return None

        root = Node(arr[0])
        q: deque[Node] = deque([root])

        i = 1
        while q and i < len(arr):
            node = q.popleft()

            if i < len(arr) and arr[i] is not None:
                node.left = Node(arr[i])
                q.append(node.left)
            i += 1

            if i < len(arr) and arr[i] is not None:
                node.right = Node(arr[i])
                q.append(node.right)
            i += 1

        return root


class Solution2:
    def minTime(self, root, target):
        # code here

        # adjacency map
        adj = defaultdict(list)

        def build_graph(node, parent):
            if not node:
                return

            if parent:
                adj[node.data].append(parent.data)
                adj[parent.data].append(node.data)

            build_graph(node.left, node)
            build_graph(node.right, node)

        build_graph(root, None)

        # BFS - calculate burning time
        visited = set()
        queue = deque()

        queue.append((target, 0))
        visited.add(target)

        burning_time = 0

        while queue:
            node, time = queue.popleft()
            burning_time = time

            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, time + 1))

        return burning_time

        # Complexity analysis
        # Time : O(V)
        # Space : O(V)


def p2():
    # Problem 2 : POTD Geeksforgeeks Burning Tree - https://www.geeksforgeeks.org/problems/burning-tree/1

    testcase = [
        [[1, 2, 3, 4, 5, 6, 7], 2, 3],
        [[1, 2, 3, 4, 5, None, 7, 8, None, None, 10], 10, 5],
    ]

    for line in testcase:
        [arr, target, expected] = line
        s2 = Solution2()
        root = Node.from_list(arr)
        result = s2.minTime(root, target)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 17 of March 2026

    p1()

    p2()
