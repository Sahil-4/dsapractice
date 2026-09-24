from collections import deque
from typing import Any, Optional


class Solution1:
    def smallestIndex(self, nums: list[int]) -> int:
        N = len(nums)

        def digits_sum(num: int) -> int:
            _sum = 0

            while num > 0:
                digit = num % 10
                _sum += digit
                num //= 10

            return _sum

        for i in range(N):
            if digits_sum(nums[i]) == i:
                return i

        return -1

        # Complexity analysis
        # Time : O(N * Log(M))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3550. Smallest Index With Digit Sum Equal to Index - https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/description/?envType=daily-question&envId=2026-09-24

    testcase = [
        [[1, 3, 2], 2],
        [[1, 10, 11], 1],
        [[1, 2, 3], -1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.smallestIndex(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxStackHeight(self, r: list[int], h: list[int]) -> int:
        discs = sorted(zip(r, h), key=lambda x: (x[0], -x[1]))

        dp = [0] * 1002

        def query(index: int) -> int:
            result = 0

            while index > 0:
                result = max(result, dp[index])
                index -= index & -index

            return result

        def update(index: int, value: int):
            while index < len(dp):
                dp[index] = max(dp[index], value)
                index += index & -index

        for _radius, height in discs:
            current = query(height - 1) + height
            update(height, current)

        return query(1000)

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Maximum Height Disc Stack - https://www.geeksforgeeks.org/problems/stacking-up-discs1315/1

    testcase = [
        [[5, 7, 3], [6, 5, 4], 10],
        [[3, 7], [7, 4], 7],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxStackHeight(*inputs)
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
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def same_tree(root: TreeNode | None, sub_root: TreeNode | None) -> bool:
            if root is None and sub_root is None:
                return True

            if root is None or sub_root is None:
                return False

            if root.val != sub_root.val:
                return False

            return same_tree(root.left, sub_root.left) and same_tree(
                root.right, sub_root.right
            )

        def helper(root: TreeNode | None) -> bool:
            if root is None:
                return False

            if same_tree(root, subRoot):
                return True

            return helper(root.left) or helper(root.right)

        return helper(root)

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(N + M) stack


def p3():
    # Problem 3 : NC150 Leetcode 572. Subtree of Another Tree - https://leetcode.com/problems/subtree-of-another-tree/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            TreeNode.from_list([3, 4, 5, 1, 2]),
            TreeNode.from_list([4, 1, 2]),
            True,
        ],
        [
            TreeNode.from_list([3, 4, 5, 1, 2, None, None, None, None, 0]),
            TreeNode.from_list([4, 1, 2]),
            False,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.isSubtree(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 24 of September 2026

    p1()

    p2()

    p3()
