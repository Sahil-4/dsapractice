from collections import deque
from typing import Any, Optional


class Solution1:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        N = len(nums)

        # sign of the number does not matter, only its square
        squares = sorted(x * x for x in nums)

        # ceil(N / 2) positions are added, floor(N / 2) positions are subtracted;
        # add the largest squares, subtract the smallest ones
        subtract_count = N // 2

        return sum(squares[subtract_count:]) - sum(squares[:subtract_count])

        # Complexity analysis
        # Time : O(N log N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3727. Maximum Alternating Sum of Squares - https://leetcode.com/problems/maximum-alternating-sum-of-squares/description/?envType=daily-question&envId=2026-10-13

    testcase = [
        [[1, 2, 3], 12],
        [[1, -1, 2, -2, 3, -3], 16],
        [[-5], 25],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maxAlternatingSum(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def update(self, n: int, updates: list[int]) -> list[int]:
        # code here

        # arr itself is used as the difference array, then turned into prefix sums in place
        arr = [0] * n

        # update j (1-based) adds 1 to every index >= j
        for j in updates:
            arr[j - 1] += 1

        for i in range(1, n):
            arr[i] += arr[i - 1]

        return arr

        # Complexity analysis
        # Time : O(N + K)
        # Space : O(1) auxiliary (only the output array)


def p2():
    # Problem 2 : POTD Geeksforgeeks Adding Ones - https://www.geeksforgeeks.org/problems/adding-ones3628/1

    testcase = [
        [3, [1, 1, 2, 3], [2, 3, 4]],
        [1, [1], [1]],
        [4, [4, 4], [0, 0, 0, 2]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.update(*inputs)
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
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = root.val

        # returns the best downward path sum starting at node
        def helper(node: Optional[TreeNode]) -> int:
            nonlocal max_sum

            if node is None:
                return 0

            # a negative branch only hurts, drop it
            left_gain = max(helper(node.left), 0)
            right_gain = max(helper(node.right), 0)

            # best path that bends at this node
            max_sum = max(max_sum, node.val + left_gain + right_gain)

            # a path extended to the parent can use only one branch
            return node.val + max(left_gain, right_gain)

        helper(root)

        return max_sum

        # Complexity analysis
        # Time : O(N)
        # Space : O(H)


def p3():
    # Problem 3 : NC150 Leetcode 124. Binary Tree Maximum Path Sum - https://leetcode.com/problems/binary-tree-maximum-path-sum/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [TreeNode.from_list([1, 2, 3]), 6],
        [TreeNode.from_list([-10, 9, 20, None, None, 15, 7]), 42],
        [TreeNode.from_list([-3]), -3],
        [TreeNode.from_list([2, -1]), 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.maxPathSum(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 13 of October 2026

    p1()

    p2()

    p3()
