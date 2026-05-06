from collections import deque
from typing import List, Optional


class Solution1:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])

        # apply gravity (rightward)
        for i in range(m):
            empty = n - 1
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == "*":
                    empty = j - 1
                elif boxGrid[i][j] == "#":
                    boxGrid[i][j] = "."
                    boxGrid[i][empty] = "#"
                    empty -= 1

        # rotate
        rotated = [["."] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - 1 - i] = boxGrid[i][j]

        return rotated

        # Complexity analysis
        # Time : O(M * N)
        # Space : O(M * N)


def p1():
    # Problem 1 : POTD Leetcode 1861. Rotating the Box - https://leetcode.com/problems/rotating-the-box/description/?envType=daily-question&envId=2026-05-06

    testcase = [
        [
            [
                ["#", ".", "#"],
            ],
            [
                ["."],
                ["#"],
                ["#"],
            ],
        ],
        [
            [
                ["#", ".", "*", "."],
                ["#", "#", "*", "."],
            ],
            [
                ["#", "."],
                ["#", "#"],
                ["*", "*"],
                [".", "."],
            ],
        ],
        [
            [
                ["#", "#", "*", ".", "*", "."],
                ["#", "#", "#", "*", ".", "."],
                ["#", "#", "#", ".", "#", "."],
            ],
            [
                [".", "#", "#"],
                [".", "#", "#"],
                ["#", "#", "*"],
                ["#", "*", "."],
                ["#", ".", "*"],
                ["#", ".", "."],
            ],
        ],
    ]

    for line in testcase:
        [boxGrid, expected] = line
        s1 = Solution1()
        result = s1.rotateTheBox(boxGrid)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


# Definition for Node
class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @staticmethod
    def from_list(arr: List[Optional[int]]) -> Optional["Node"]:
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
    def getSize(self, root):
        # code here

        nodes_count = 0

        q = deque([root])
        while q:
            node = q.popleft()
            nodes_count += 1

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return nodes_count

        # Complexity analysis
        # Time : O(N)
        # Space : O(W)


def p2():
    # Problem 2 : POTD Geeksforgeeks Size of Binary Tree - https://www.geeksforgeeks.org/problems/size-of-binary-tree/1

    testcase = [
        [[1, 2, 3, None, None, 4, 5], 5],
        [[1, 2, 3, 4, 5, 6, 7], 7],
    ]

    for line in testcase:
        [list_arr, expected] = line
        s2 = Solution2()
        root = Node.from_list(list_arr)
        result = s2.getSize(root)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 6 of May 2026

    p1()

    p2()
