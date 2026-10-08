from collections import defaultdict, deque
from typing import Any, Optional


class Solution1:
    def removeOuterParentheses(self, s: str) -> str:
        # "(()())(())(()(()))"
        # "(()()) + (()) + (()(()))"
        # "()() + () + ()(())"
        # "()()()()(())"

        blocks: list[str] = []
        curr_block: list[str] = []

        counter = 0
        for c in s:
            counter += 1 if c == "(" else -1
            curr_block.append(c)

            if counter == 0:
                curr_block.pop(0)
                curr_block.pop()
                blocks.append("".join(curr_block))
                curr_block.clear()

        return "".join(blocks)

        # Complexity analysis
        # Time : O(N) + string overhead
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1021. Remove Outermost Parentheses - https://leetcode.com/problems/remove-outermost-parentheses/description/?envType=daily-question&envId=2026-10-08

    testcase = [
        ["(()())(())", "()()()"],
        ["(()())(())(()(()))", "()()()()(())"],
        ["()()", ""],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.removeOuterParentheses(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxFrequency(self, arr: list[int], k: int) -> int:
        # code here

        arr.sort()

        start = 0
        current_cost = 0
        max_freq = 0

        for end, target in enumerate(arr):
            if end > 0:
                current_cost += (target - arr[end - 1]) * (end - start)

            while current_cost > k:
                current_cost -= target - arr[start]
                start += 1

            window_len = end - start + 1
            if window_len > max_freq:
                max_freq = window_len

        return max_freq

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Maximum Frequency with K Increments - https://www.geeksforgeeks.org/problems/maximum-frequency-1662528911/1

    testcase = [
        [[2, 2, 4], 4, 3],
        [[7, 7, 7, 7], 5, 4],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxFrequency(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_list(arr: list[Optional[int]]) -> Optional["TreeNode"]:
        if not arr or arr[0] is None:
            return None

        root = TreeNode(arr[0])
        q: deque[TreeNode] = deque([root])

        i = 1
        while q and i < len(arr):
            node = q.popleft()

            val = arr[i] if i < len(arr) else None
            if val is not None:
                node.left = TreeNode(val)
                q.append(node.left)
            i += 1

            val = arr[i] if i < len(arr) else None
            if val is not None:
                node.right = TreeNode(val)
                q.append(node.right)
            i += 1

        return root

    def to_list(self) -> list[Any]:
        result = []
        q: deque[Optional[TreeNode]] = deque([self])

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


class Solution3:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        N = len(preorder)

        inorder_map = defaultdict()
        for index, item in enumerate(inorder):
            inorder_map[item] = index

        def build(po_li: int, po_ri: int, io_li: int, io_ri: int) -> TreeNode | None:
            if po_li > po_ri or io_li > io_ri:
                return None

            root = TreeNode(preorder[po_li])

            nodes = inorder_map[preorder[po_li]] - io_li

            root.left = build(po_li + 1, po_li + nodes, io_li, io_li + nodes)
            root.right = build(po_li + nodes + 1, po_ri, io_li + nodes + 1, io_ri)

            return root

        return build(0, N - 1, 0, N - 1)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal - https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            [3, 9, 20, 15, 7],
            [9, 3, 15, 20, 7],
            [3, 9, 20, None, None, 15, 7],
        ],
        [
            [-1],
            [-1],
            [-1],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.buildTree(*inputs)
        result = TreeNode.to_list(result) if result else []
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 8 of October 2026

    p1()

    p2()

    p3()
