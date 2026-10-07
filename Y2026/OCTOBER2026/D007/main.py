from collections import deque
from typing import Any, Optional


class Solution1:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Step 1: Count misplaced '(' and ')'
        rem_l = 0
        rem_r = 0
        for char in s:
            if char == "(":
                rem_l += 1
            elif char == ")":
                if rem_l > 0:
                    rem_l -= 1
                else:
                    rem_r += 1

        result = []
        N = len(s)

        def backtrack(
            index: int, left_rem: int, right_rem: int, open_count: int, path: list[str]
        ):
            if index == N:
                if left_rem == 0 and right_rem == 0 and open_count == 0:
                    result.append("".join(path))
                return

            char = s[index]

            # Option A: Discard the character (only valid for parentheses)
            if char == "(" and left_rem > 0:
                backtrack(index + 1, left_rem - 1, right_rem, open_count, path)
            elif char == ")" and right_rem > 0:
                backtrack(index + 1, left_rem, right_rem - 1, open_count, path)

            # Option B: Keep the character
            path.append(char)
            if char != "(" and char != ")":
                backtrack(index + 1, left_rem, right_rem, open_count, path)
            elif char == "(":
                backtrack(index + 1, left_rem, right_rem, open_count + 1, path)
            elif char == ")" and open_count > 0:
                backtrack(index + 1, left_rem, right_rem, open_count - 1, path)
            path.pop()

        backtrack(0, rem_l, rem_r, 0, [])
        return list(set(result))

        # Complexity analysis
        # Time : O(2^N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 301. Remove Invalid Parentheses - https://leetcode.com/problems/remove-invalid-parentheses/description/?envType=daily-question&envId=2026-10-07

    testcase = [
        ["()())()", ["(())()", "()()()"]],
        ["(a)())()", ["(a())()", "(a)()()"]],
        [")(", [""]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.removeInvalidParentheses(*inputs)
        assert sorted(result) == sorted(
            expected
        ), f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


# Binary Tree Node Structure
class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @staticmethod
    def from_list(arr: list[Optional[int]]) -> Optional["Node"]:
        if not arr or arr[0] is None:
            return None

        root = Node(arr[0])
        q: deque[Node] = deque([root])

        i = 1
        while q and i < len(arr):
            node = q.popleft()

            data = arr[i] if i < len(arr) else None
            if data is not None:
                node.left = Node(data)
                q.append(node.left)
            i += 1

            data = arr[i] if i < len(arr) else None
            if data is not None:
                node.right = Node(data)
                q.append(node.right)
            i += 1

        return root

    def to_list(self) -> list[Any]:
        result = []
        q: deque[Optional[Node]] = deque([self])

        while q:
            node = q.popleft()

            if node:
                result.append(node.data)
                q.append(node.left)
                q.append(node.right)
            else:
                result.append(None)

        # remove trailing None values
        while result and result[-1] is None:
            result.pop()

        return result


class Solution2:
    def maxPathSum(self, root: Node) -> int:
        # code here
        max_sum = float("-inf")
        leaf_count = 0

        def dfs(node: Node):
            nonlocal max_sum, leaf_count

            if not node:
                return float("-inf")

            # Check if this node is a leaf
            if not node.left and not node.right:
                leaf_count += 1
                return node.data

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # A leaf-to-leaf path through this node requires both children
            if node.left and node.right:
                max_sum = max(max_sum, left_sum + right_sum + node.data)
                return max(left_sum, right_sum) + node.data

            # If only one child exists, pass up the valid path through that child
            return (left_sum if node.left else right_sum) + node.data

        dfs(root)

        # A path between two distinct leaves requires at least 2 leaves in the tree
        if leaf_count < 2 or max_sum == float("-inf"):
            return -1

        return max_sum

        # Complexity analysis
        # Time : O(N)
        # Space : O(H)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Path Sum Between Two Leaves - https://www.geeksforgeeks.org/problems/maximum-path-sum/1

    testcase = [
        [
            Node.from_list([3, 4, 5, -10, 4, None, None]),
            16,
        ],
        [
            Node.from_list(
                [
                    -15,
                    5,
                    6,
                    -8,
                    1,
                    3,
                    9,
                    2,
                    -3,
                    None,
                    None,
                    None,
                    None,
                    None,
                    0,
                    None,
                    None,
                    None,
                    None,
                    4,
                    -1,
                    None,
                    None,
                    10,
                ]
            ),
            27,
        ],
        [
            Node.from_list([3, 4, 1, -10, 4, None, None]),
            12,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxPathSum(*inputs)
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
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 104. Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            TreeNode.from_list([3, 9, 20, None, None, 15, 7]),
            3,
        ],
        [
            TreeNode.from_list([1, None, 2]),
            2,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.maxDepth(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 7 of October 2026

    p1()

    p2()

    p3()
