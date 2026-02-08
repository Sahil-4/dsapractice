from typing import Optional, List, Tuple
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_list(arr: List[Optional[int]]) -> Optional["TreeNode"]:
        if not arr:
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


class Solution1:
    def checkBalanced(self, root: Optional[TreeNode]) -> Tuple[bool, int]:
        if not root:
            return True, 0

        [left_check, left_height] = self.checkBalanced(root.left)
        [right_check, right_height] = self.checkBalanced(root.right)

        return (
            left_check and right_check and abs(left_height - right_height) <= 1,
            max(left_height, right_height) + 1,
        )

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.checkBalanced(root)[0]

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 110. Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/?envType=daily-question&envId=2026-02-08

    testcase = [
        [[3, 9, 20, None, None, 15, 7], True],
        [[1, 2, 2, 3, 3, None, None, 4, 4], False],
        [[], True],
    ]

    for line in testcase:
        [arr, expected] = line
        s1 = Solution1()
        root = TreeNode.from_list(arr)
        result = s1.isBalanced(root)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxProduct(self, arr):
        # code here

        cur_max = cur_min = result = arr[0]

        for num in arr[1:]:
            if num < 0:
                cur_max, cur_min = cur_min, cur_max

            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)

            result = max(result, cur_max)

        return result

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Maximum Product Subarray - https://www.geeksforgeeks.org/problems/maximum-product-subarray3604/1

    testcase = [
        [[-2, 6, -3, -10, 0, 2], 180],
        [[-1, -3, -10, 0, 6], 30],
        [[2, 3, 4], 24],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.maxProduct(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 8 of February 2026

    p1()

    p2()
