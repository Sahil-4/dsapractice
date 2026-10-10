from collections import deque
from typing import Any, Optional


class Solution1:
    def minSumSquareDiff(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int
    ) -> int:
        N = len(nums1)

        # a +/-1 on either array changes |nums1[i] - nums2[i]| by exactly 1,
        # hence k1 and k2 pool into a single budget
        k = k1 + k2

        diffs = [abs(nums1[i] - nums2[i]) for i in range(N)]
        max_diff = max(diffs)

        # freq[d] = number of indices whose absolute difference is d
        freq = [0] * (max_diff + 1)
        for d in diffs:
            freq[d] += 1

        # always shave the largest differences first (square is convex)
        for d in range(max_diff, 0, -1):
            if k == 0:
                break

            if freq[d] == 0:
                continue

            moved = min(k, freq[d])
            freq[d] -= moved
            freq[d - 1] += moved
            k -= moved

        return sum(freq[d] * d * d for d in range(max_diff + 1))

        # Complexity analysis
        # Time : O(N + M), M = max absolute difference
        # Space : O(M)


def p1():
    # Problem 1 : POTD Leetcode 2333. Minimum Sum of Squared Difference - https://leetcode.com/problems/minimum-sum-of-squared-difference/?envType=daily-question&envId=2026-10-10

    testcase = [
        [[1, 2, 3, 4], [2, 10, 20, 19], 0, 0, 579],
        [[1, 4, 10, 12], [5, 8, 6, 9], 1, 1, 43],
        [[1, 2], [3, 4], 5, 5, 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minSumSquareDiff(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def balancePan(self, a: int, b: int) -> bool:
        # code here

        # all powers of 1 are equal to 1, hence unit weights are unlimited
        if a == 1:
            return True

        # write b in base a; every digit must be 0, 1 or (a - 1)
        # 0     : weight not used
        # 1     : weight on the opposite pan of b
        # a - 1 : weight on the same pan as b, carry 1 to the next power
        while b > 0:
            rem = b % a

            if rem == 0 or rem == 1:
                b //= a
            elif rem == a - 1:
                b = b // a + 1
            else:
                return False

        return True

        # Complexity analysis
        # Time : O(log_a(b))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Balancing with Distinct Powers - https://www.geeksforgeeks.org/problems/balancing-pan5038/1

    testcase = [
        [4, 11, True],
        [3, 5, True],
        [3, 7, True],
        [5, 2, False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.balancePan(*inputs)
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # returns height of the subtree, or -1 if it is not balanced
        def helper(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left_height = helper(node.left)
            if left_height == -1:
                return -1

            right_height = helper(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)

        return helper(root) != -1

        # Complexity analysis
        # Time : O(N)
        # Space : O(H)


def p3():
    # Problem 3 : NC150 Leetcode 110. Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [TreeNode.from_list([3, 9, 20, None, None, 15, 7]), True],
        [TreeNode.from_list([1, 2, 2, 3, 3, None, None, 4, 4]), False],
        [TreeNode.from_list([]), True],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.isBalanced(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 10 of October 2026

    p1()

    p2()

    p3()
