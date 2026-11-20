from collections import deque
from typing import Any, Optional


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


class Solution1:
    def maxSelectedElements(self, nums: list[int]) -> int:
        # dp[v] : longest run of consecutive values ending at value v,
        # using the elements processed so far (each element becomes x or x + 1)
        dp = {}

        for x in sorted(nums):
            # x + 1 is updated first so that this element is not used twice :
            # it reads dp[x] as it was before this element was placed at x
            dp[x + 1] = max(dp.get(x + 1, 0), dp.get(x, 0) + 1)
            dp[x] = max(dp.get(x, 0), dp.get(x - 1, 0) + 1)

        return max(dp.values())

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3041. Maximize Consecutive Elements in an Array After Modification - https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/?envType=daily-question&envId=2026-11-20

    testcase = [
        [[2, 1, 5, 1, 1], 3],
        [[1, 4, 7, 10], 1],
        [[1, 1, 1], 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maxSelectedElements(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minFlips(self, s: str) -> int:
        # an alternating string is either 0101... or 1010...
        # count mismatches against the first, the second needs the remaining positions
        mismatches = 0

        for i, ch in enumerate(s):
            if int(ch) != i % 2:
                mismatches += 1

        return min(mismatches, len(s) - mismatches)

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Min Flips for Alternate - https://www.geeksforgeeks.org/problems/min-number-of-flips3210/1

    testcase = [
        ["001", 1],
        ["0001010111", 2],
        ["0101", 0],
        ["1111", 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minFlips(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root

        # iterative in-order traversal visits the values in sorted order,
        # stop at the k-th visited node
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            k -= 1

            if k == 0:
                return node.val

            node = node.right

        return -1

        # Complexity analysis
        # Time : O(H + K), H = height of the tree
        # Space : O(H)


def p3():
    # Problem 3 : NC150 Leetcode 230. Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[3, 1, 4, None, 2], 1, 1],
        [[5, 3, 6, 2, 4, None, None, 1], 3, 3],
        [[1], 1, 1],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s3 = Solution3()
        result = s3.kthSmallest(TreeNode.from_list(arr), k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 20 of November 2026

    p1()

    p2()

    p3()
