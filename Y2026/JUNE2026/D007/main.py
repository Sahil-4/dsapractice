# Definition for a binary tree node.
from collections import deque
from typing import Any, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_list(arr: List[Optional[int]]) -> Optional["TreeNode"]:
        if not arr or arr[0] is None:
            return None

        root = TreeNode(arr[0])
        q: deque[TreeNode] = deque([root])

        i = 1
        while q and i < len(arr):
            node = q.popleft()

            if i < len(arr) and arr[i] is not None:
                node.left = TreeNode(arr[i])
                q.append(node.left)
            i += 1

            if i < len(arr) and arr[i] is not None:
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1

        return root

    def to_list(self) -> List[Any]:
        result = []
        q = deque([self])

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


class Solution1:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # val -> TreeNode
        nodes = {}
        # all values that appear as a child
        children = set()

        for parent_val, child_val, is_left in descriptions:
            # ensure both nodes exist
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)

            # attach child to parent
            if is_left:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]

            children.add(child_val)

        # Root is the only node never assigned as a child
        for val, node in nodes.items():
            if val not in children:
                return node

        return None

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2196. Create Binary Tree From Descriptions - https://leetcode.com/problems/create-binary-tree-from-descriptions/description/?envType=daily-question&envId=2026-06-07

    testcase = [
        [
            [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]],
            [50, 20, 80, 15, 17, 19],
        ],
        [
            [[1, 2, 1], [2, 3, 0], [3, 4, 1]],
            [1, 2, None, None, 3, 4],
        ],
    ]

    for line in testcase:
        [descriptions, expected] = line
        s1 = Solution1()
        root = s1.createBinaryTree(descriptions)
        result = root.to_list() if root else []
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def profession(self, level, pos):
        # code here
        pos_binary = bin(pos - 1)
        hamming_weight = pos_binary.count("1")
        return "Doctor" if hamming_weight & 1 else "Engineer"

        # Complexity analysis
        # Time : O(Log(pos))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Finding Profession - https://www.geeksforgeeks.org/problems/finding-profession3834/1

    testcase = [
        [4, 2, "Doctor"],
        [3, 4, "Engineer"],
    ]

    for line in testcase:
        [level, pos, expected] = line
        s2 = Solution2()
        result = s2.profession(level, pos)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 7 of June 2026

    p1()

    p2()
