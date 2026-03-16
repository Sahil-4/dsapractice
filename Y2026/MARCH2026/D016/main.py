from collections import deque
from typing import List, Optional


class Solution1:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        # left->right diagonal prefix
        d1 = [[0] * n for _ in range(m)]

        # right->left diagonal prefix
        d2 = [[0] * n for _ in range(m)]

        # build d1
        for i in range(m):
            for j in range(n):
                d1[i][j] = grid[i][j]
                if i > 0 and j > 0:
                    d1[i][j] += d1[i - 1][j - 1]

        # build d2
        for i in range(m):
            for j in range(n - 1, -1, -1):
                d2[i][j] = grid[i][j]
                if i > 0 and j + 1 < n:
                    d2[i][j] += d2[i - 1][j + 1]

        st = set()

        def add_to_set(val):
            st.add(val)
            if len(st) > 3:
                st.remove(min(st))

        for r in range(m):
            for c in range(n):

                # side = 0 rhombus
                add_to_set(grid[r][c])

                side = 1
                while r - side >= 0 and r + side < m and c - side >= 0 and c + side < n:

                    top_r, top_c = r - side, c
                    right_r, right_c = r, c + side
                    bottom_r, bottom_c = r + side, c
                    left_r, left_c = r, c - side

                    total = 0

                    # top -> right
                    total += d1[right_r][right_c]
                    if top_r - 1 >= 0 and top_c - 1 >= 0:
                        total -= d1[top_r - 1][top_c - 1]

                    # right -> bottom
                    total += d2[bottom_r][bottom_c]
                    if right_r - 1 >= 0 and right_c + 1 < n:
                        total -= d2[right_r - 1][right_c + 1]

                    # bottom -> left
                    total += d1[bottom_r][bottom_c]
                    if left_r - 1 >= 0 and left_c - 1 >= 0:
                        total -= d1[left_r - 1][left_c - 1]

                    # left -> top
                    total += d2[left_r][left_c]
                    if top_r - 1 >= 0 and top_c + 1 < n:
                        total -= d2[top_r - 1][top_c + 1]

                    # remove corners counted twice
                    total -= grid[top_r][top_c]
                    total -= grid[right_r][right_c]
                    total -= grid[bottom_r][bottom_c]
                    total -= grid[left_r][left_c]

                    add_to_set(total)
                    side += 1

        return sorted(st, reverse=True)

        # Complexity analysis
        # Time : O(M * N * Min(M, N))
        # Space : O(M * N)


def p1():
    # Problem 1 : POTD Leetcode 1878. Get Biggest Three Rhombus Sums in a Grid - https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/description/?envType=daily-question&envId=2026-03-16

    testcase = [
        [
            [
                [3, 4, 5, 1, 3],
                [3, 3, 4, 2, 3],
                [20, 30, 200, 40, 10],
                [1, 5, 5, 4, 1],
                [4, 3, 2, 2, 5],
            ],
            [228, 216, 211],
        ],
        [
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            [20, 9, 8],
        ],
        [
            [
                [7, 7, 7],
            ],
            [7],
        ],
    ]

    for line in testcase:
        [grid, expected] = line
        s1 = Solution1()
        result = s1.getBiggestThree(grid)
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

    def countPathsUtil(self, node, k, currSum, prefSums):
        if node is None:
            return 0

        pathCount = 0
        currSum += node.data

        if currSum == k:
            pathCount += 1

        # The count of (curr_sum − k) gives the number
        # of paths with sum k up to the current node
        pathCount += prefSums.get(currSum - k, 0)

        # Add the current sum into the hashmap
        prefSums[currSum] = prefSums.get(currSum, 0) + 1

        pathCount += self.countPathsUtil(node.left, k, currSum, prefSums)
        pathCount += self.countPathsUtil(node.right, k, currSum, prefSums)

        # Remove the current sum from the hashmap
        prefSums[currSum] -= 1

        return pathCount

    def countAllPaths(self, root, k):
        prefSums = {}
        return self.countPathsUtil(root, k, 0, prefSums)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks K Sum Paths - https://www.geeksforgeeks.org/problems/k-sum-paths/1

    testcase = [
        [[8, 4, 5, 3, 2, None, 2, 3, -2, None, 1], 7, 3],
        [[1, 2, 3], 3, 2],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        root = Node.from_list(arr)
        result = s2.countAllPaths(root, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 16 of March 2026

    p1()

    p2()
