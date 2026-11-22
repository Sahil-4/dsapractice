from collections import deque
from typing import List, Any, Optional


class Solution1:
    def checkString(self, s: str) -> bool:
        # every 'a' is before every 'b'
        # exactly when a 'b' is never directly followed by an 'a'
        # (a "ba" substring exists as soon as some 'a' appears after some 'b')

        return "ba" not in s

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2124. Check if All A's Appears Before All B's - https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/description/?envType=daily-question&envId=2026-11-22

    testcase = [
        ["aaabbb", True],
        ["abab", False],
        ["bbb", True],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.checkString(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def longestSubarrayDivK(self, arr: list[int], k: int) -> int:
        # first_index[r] : first prefix position whose prefix sum has remainder r
        # two prefixes with the same remainder enclose a subarray with sum divisible by k

        first_index = {0: -1}

        prefix = 0
        longest = 0

        for i, value in enumerate(arr):
            # python's % gives a non-negative remainder for negative sums as well
            prefix = (prefix + value) % k

            if prefix in first_index:
                longest = max(longest, i - first_index[prefix])
            else:
                first_index[prefix] = i

        return longest

        # Complexity analysis
        # Time : O(N)
        # Space : O(min(N, K))


def p2():
    # Problem 2 : POTD Geeksforgeeks Longest Subarray Sum Divisible by K - https://www.geeksforgeeks.org/problems/longest-subarray-with-sum-divisible-by-k1259/1

    testcase = [
        [[2, 7, 6, 1, 4, 5], 3, 4],
        [[-2, 2, -5, 12, -11, -1, 7], 3, 5],
        [[1, 2, 4], 3, 2],
        [[1, 1], 5, 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.longestSubarrayDivK(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


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

            if i < len(arr):
                val = arr[i]
                if val is not None:
                    node.left = TreeNode(val)
                    q.append(node.left)
            i += 1

            if i < len(arr):
                val = arr[i]
                if val is not None:
                    node.right = TreeNode(val)
                    q.append(node.right)
            i += 1

        return root

    def to_list(self) -> List[Any]:
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
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        node = root

        # in a BST the LCA is the first node on the way down whose value lies
        # between p and q (inclusive), otherwise both targets are on the same side
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node

        return root

        # Complexity analysis
        # Time : O(H), H = height of the tree
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 235. Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/?envType=problem-list-v2&envId=plakya4j

    def find(root: TreeNode, val: int) -> TreeNode:
        # nodes are passed as TreeNode objects, locate them by value in the BST
        node = root
        while node and node.val != val:
            node = node.left if val < node.val else node.right
        assert node is not None
        return node

    testcase = [
        [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6],
        [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2],
        [[2, 1], 2, 1, 2],
    ]

    for line in testcase:
        [arr, p, q, expected] = line
        s3 = Solution3()
        root = TreeNode.from_list(arr)
        assert root is not None
        result = s3.lowestCommonAncestor(root, find(root, p), find(root, q)).val
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 22 of November 2026

    p1()

    p2()

    p3()
