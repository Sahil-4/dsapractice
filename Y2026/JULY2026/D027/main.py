from typing import Optional


class Solution1:
    def maxProduct(self, nums: list[int]) -> int:
        max_1 = 0
        max_2 = 0

        for num in nums:
            if num > max_1:
                max_2 = max_1
                max_1 = num
            elif num > max_2:
                max_2 = num

        return (max_1 - 1) * (max_2 - 1)

        # Complexity Analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1464. Maximum Product of Two Elements in an Array - https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/?envType=daily-question&envId=2026-07-27

    testcase = [
        [[3, 4, 5, 2], 12],
        [[1, 5, 4, 5], 16],
        [[3, 7], 12],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maxProduct(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


# Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    @staticmethod
    def build(values: list) -> Optional["Node"]:
        """Level-order construction from a list (None = missing node)."""
        if not values:
            return None
        root = Node(values[0])
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            if i < len(values) and values[i] is not None:
                node.left = Node(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = Node(values[i])
                queue.append(node.right)
            i += 1
        return root

    def to_list(self) -> list:
        """Level-order serialization for assertion comparison."""
        result, queue = [], [self]
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def preorder(self) -> list:
        """Preorder serialization (Root -> Left -> Right)."""
        result = [self.data]
        if self.left:
            result.extend(self.left.preorder())
        if self.right:
            result.extend(self.right.preorder())
        return result


class Solution2:
    def buildTree(
        self,
        pre: list[int],
        preMirror: list[int],
        preIndex: list[int],
        left: int,
        right: int,
        mp: dict[int, int],
        n: int,
    ) -> Optional["Node"]:

        # Base case
        if preIndex[0] >= n or left > right:
            return None

        # Create current node
        root = Node(pre[preIndex[0]])
        preIndex[0] += 1

        # If leaf node
        if left == right:
            return root

        # Find next preorder element index in preMirror
        mirrorIndex = mp[pre[preIndex[0]]]

        # Construct left and right subtree
        if mirrorIndex >= left and mirrorIndex <= right:

            # Construct left subtree
            root.left = self.buildTree(
                pre, preMirror, preIndex, mirrorIndex, right, mp, n
            )

            # Construct right subtree
            root.right = self.buildTree(
                pre, preMirror, preIndex, left + 1, mirrorIndex - 1, mp, n
            )

        return root

    def constructBinaryTree(
        self, pre: list[int], preMirror: list[int]
    ) -> Optional["Node"]:
        # code here

        N = len(pre)

        # mirror preorder traversal
        mp = {}
        for i in range(N):
            mp[preMirror[i]] = i

        preIndex = [0]

        return self.buildTree(pre, preMirror, preIndex, 0, N - 1, mp, N)

        # Complexity Analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Construct a Full Binary Tree - https://www.geeksforgeeks.org/problems/construct-a-full-binary-tree--170648/1

    testcase = [
        [
            [0, 1, 2],
            [0, 2, 1],
            [0, 1, 2],
        ],
        [
            [1, 2, 4, 5, 3, 6, 7],
            [1, 3, 7, 6, 2, 5, 4],
            [1, 2, 4, 5, 3, 6, 7],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        bt = s2.constructBinaryTree(*inputs)
        result = bt.preorder() if bt else []
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 27 of July 2026

    p1()

    p2()
