from collections import deque
from typing import List, Optional


class Solution1:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        count = 0

        N = len(grid)
        M = len(grid[0])
        sumx = [[0] * M for _ in range(N)]
        sumy = [[0] * M for _ in range(N)]

        for i in range(N):
            for j in range(M):
                if grid[i][j] == "X":
                    sumx[i][j] += 1
                elif grid[i][j] == "Y":
                    sumy[i][j] += 1

                if i > 0:
                    sumx[i][j] += sumx[i - 1][j]
                    sumy[i][j] += sumy[i - 1][j]

                if j > 0:
                    sumx[i][j] += sumx[i][j - 1]
                    sumy[i][j] += sumy[i][j - 1]

                if i > 0 and j > 0:
                    sumx[i][j] -= sumx[i - 1][j - 1]
                    sumy[i][j] -= sumy[i - 1][j - 1]

                if sumx[i][j] >= 1 and sumx[i][j] == sumy[i][j]:
                    count += 1

        return count

        # Complexity analysis
        # Time : O(M*N)
        # Space : O(2*M*N)


def p1():
    # Problem 1 : POTD Leetcode 3212. Count Submatrices With Equal Frequency of X and Y - https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/description/?envType=daily-question&envId=2026-03-19

    testcase = [
        [[["X", "Y", "."], ["Y", ".", "."]], 3],
        [[["X", "X"], ["X", "Y"]], 0],
        [[["X", "."], [".", "."]], 0],
        [[["X", "."], [".", "Y"]], 1],
    ]

    for line in testcase:
        [grid, expected] = line
        s1 = Solution1()
        result = s1.numberOfSubmatrices(grid)
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
    def largestBst(self, root):
        # Your code here

        def find_largest_bst(node):
            if not node:
                return 0, float("inf"), float("-inf")

            left_size, left_min, left_max = find_largest_bst(node.left)
            right_size, right_min, right_max = find_largest_bst(node.right)

            if left_max < node.data and right_min > node.data:
                return (
                    left_size + right_size + 1,
                    min(left_min, node.data),
                    max(right_max, node.data),
                )

            return (max(left_size, right_size), float("-inf"), float("inf"))

        largest_bst_size, _, __ = find_largest_bst(root)

        return largest_bst_size

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Largest BST - https://www.geeksforgeeks.org/problems/largest-bst/1

    testcase = [
        [[5, 2, 4, 1, 3], 3],
        [[6, 7, 3, None, 2, 2, 4], 3],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        root = Node.from_list(arr)
        result = s2.largestBst(root)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 19 of March 2026

    p1()

    p2()
