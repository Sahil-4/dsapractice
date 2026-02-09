from typing import Optional, List, Any
from collections import deque


# Definition for a binary tree node.
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
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vals = []

        # inorder traversal to get sorted values
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

        # construct balanced BST from sorted list
        def build(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            node = TreeNode(vals[mid])

            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)

            return node

        inorder(root)
        return build(0, len(vals) - 1)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1382. Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/?envType=daily-question&envId=2026-02-09

    testcase = [
        [[1, None, 2, None, 3, None, 4, None, None], [2, 1, 3, None, None, None, 4]],
        [[2, 1, 3], [2, 1, 3]],
    ]

    for line in testcase:
        [arr, expected] = line
        s1 = Solution1()
        root = TreeNode.from_list(arr)
        result = s1.balanceBST(root)
        result = result.to_list() if result else []
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findKRotation(self, arr):
        # code here
        # find smallest element
        # and return index

        N = len(arr)

        if arr[0] <= arr[N - 1]:
            return 0

        low = 0
        high = N - 1

        while low < high:
            mid = (low + high) // 2

            # pivot is on right
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid

        return low

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Find Kth Rotation - https://www.geeksforgeeks.org/problems/rotation4723/1

    testcase = [
        [[5, 1, 2, 3, 4], 1],
        [[1, 2, 3, 4, 5], 0],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.findKRotation(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 9 of February 2026

    p1()

    p2()
