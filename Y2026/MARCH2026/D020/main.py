from collections import deque
from typing import List, Optional


class Solution1:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        result = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):

                # Collect elements in a list
                vals = []

                for r in range(i, i + k):
                    for c in range(j, j + k):
                        vals.append(grid[r][c])

                # Sort the list
                vals.sort()

                # Remove duplicates (since set was used originally)
                unique_vals = []
                for val in vals:
                    if not unique_vals or unique_vals[-1] != val:
                        unique_vals.append(val)

                # If only one unique element, skip
                if len(unique_vals) == 1:
                    continue

                min_abs_diff = float("inf")

                for idx in range(1, len(unique_vals)):
                    diff = unique_vals[idx] - unique_vals[idx - 1]
                    if diff < min_abs_diff:
                        min_abs_diff = diff

                result[i][j] = min_abs_diff

        return result

        # Complexity analysis
        # Time : O(M * N * K * K * Log(K))
        # Space : O(K * K)


def p1():
    # Problem 1 : POTD Leetcode 3567. Minimum Absolute Difference in Sliding Submatrix - https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/description/?envType=daily-question&envId=2026-03-20

    testcase = [
        [[[1, 8], [3, -2]], 2, [[2]]],
        [[[3, -1]], 1, [[0, 0]]],
        [[[1, -2, 3], [2, 3, 5]], 2, [[1, 2]]],
    ]

    for line in testcase:
        [grid, k, expected] = line
        s1 = Solution1()
        result = s1.minAbsDiff(grid, k)
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

    def _successor(self, root, key):

        successor: Optional[Node] = None

        while root:
            if root.data <= key:
                root = root.right
            else:
                successor = root
                root = root.left

        return successor

    def _predecessor(self, root, key):

        predecessor: Optional[Node] = None

        while root:
            if root.data >= key:
                root = root.left
            else:
                predecessor = root
                root = root.right

        return predecessor

    def findPreSuc(self, root, key):
        # code here

        successor = self._successor(root, key)
        predecessor = self._predecessor(root, key)

        return [predecessor, successor]

        # Complexity analysis
        # Time : O(H)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Predecessor and Successor - https://www.geeksforgeeks.org/problems/predecessor-and-successor/1

    testcase = [
        [[50, 30, 70, 20, 40, 60, 80], 65, [60, 70]],
        [[8, 1, 9, None, 4, None, 10, 3], 8, [4, 9]],
    ]

    for line in testcase:
        [arr, key, expected] = line
        s2 = Solution2()
        root = Node.from_list(arr)
        result = s2.findPreSuc(root, key)
        result = [result[0].data, result[1].data]
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 20 of March 2026

    p1()

    p2()
