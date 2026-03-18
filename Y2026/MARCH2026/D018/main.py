from collections import deque
from typing import List, Optional


class Solution1:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        count = 0

        N = len(grid)
        M = len(grid[0])
        grid_copy = [[0] * M for _ in range(N)]

        for i in range(N):
            for j in range(M):
                grid_copy[i][j] = grid[i][j]

                if i > 0:
                    grid_copy[i][j] += grid_copy[i - 1][j]

                if j > 0:
                    grid_copy[i][j] += grid_copy[i][j - 1]

                if i > 0 and j > 0:
                    grid_copy[i][j] -= grid_copy[i - 1][j - 1]

                if grid_copy[i][j] <= k:
                    count += 1
                else:
                    break

        return count

        # Complexity analysis
        # Time : O(M*N)
        # Space : O(M*N)


def p1():
    # Problem 1 : POTD Leetcode 3070. Count Submatrices with Top-Left Element and Sum Less Than k - https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/description/?envType=daily-question&envId=2026-03-18

    testcase = [
        [[[7, 6, 3], [6, 6, 1]], 18, 4],
        [[[7, 2, 9], [1, 5, 0], [2, 6, 6]], 20, 6],
    ]

    for line in testcase:
        [grid, k, expected] = line
        s1 = Solution1()
        result = s1.countSubmatrices(grid, k)
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
    def distCandy(self, root):
        # code here
        # balance load across nodes - each should have 1 load
        # excess nodes = (candies at node i) - 1
        # if excess > 0
        # node has extra candies - needs to send out
        # if excess < 0
        # node needs candies - must receive
        # if excess = 0
        # perfectly balanced
        # to balance any (parent, or child) we must have to perform an operation
        # hence direction does not matter
        # each node will take one and pass rest to parent
        # send to parent = (node candies + left balance + right balance) - 1

        tmoves = 0

        def solve(node):
            nonlocal tmoves

            if not node:
                return 0

            l = solve(node.left)
            r = solve(node.right)

            tmoves += abs(l)
            tmoves += abs(r)

            return node.data + l + r - 1

        solve(root)
        return tmoves

        # Complexity analysis
        # Time : O(N)
        # Space : O(H)


def p2():
    # Problem 2 : POTD Geeksforgeeks Distribute Candies - https://www.geeksforgeeks.org/problems/distribute-candies-in-a-binary-tree/1

    testcase = [
        [[5, 0, 0, None, None, 0, 0], 6],
        [[2, 0, 0, None, None, 3, 0], 4],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        root = Node.from_list(arr)
        result = s2.distCandy(root)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 18 of March 2026

    p1()

    p2()
