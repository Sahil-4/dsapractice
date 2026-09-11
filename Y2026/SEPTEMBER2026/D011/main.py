from collections import deque
from math import gcd, isqrt
from typing import Any, Optional


class Solution1:
    def totalNumbers(self, digits: list[int]) -> int:
        # digits[i] >= 0 and <= 9
        digits_frequency = [0] * 10
        for digit in digits:
            digits_frequency[digit] += 1

        def helper(t: int = 0) -> int:
            if t == 3:
                return 1

            count = 0
            for digit in range(10):
                # can not use digit 0 at the beginning
                if t == 0 and digit == 0:
                    continue

                # can not use odd digits at position 2
                if t == 2 and digit & 1:
                    continue

                # can not use digit if count is 0
                if digits_frequency[digit] == 0:
                    continue

                digits_frequency[digit] -= 1
                count += helper(t + 1)
                digits_frequency[digit] += 1

            return count

        return helper()

        # Complexity analysis
        # Time : O(3^10)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3483. Unique 3-Digit Even Numbers - https://leetcode.com/problems/unique-3-digit-even-numbers/description/?envType=daily-question&envId=2026-09-11

    testcase = [
        [[1, 2, 3, 4], 12],
        [[0, 2, 2], 2],
        [[6, 6, 6], 1],
        [[1, 3, 5], 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.totalNumbers(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def sameMod(self, arr: list[int]) -> int:
        # code here

        # GCD of all differences from arr[0]
        g = 0

        for num in arr[1:]:
            g = gcd(g, abs(num - arr[0]))

        # g == 0 means all elements are equal
        # therefore infinitely many k work
        if g == 0:
            return -1

        # count positive divisors of g
        count = 0

        for d in range(1, isqrt(g) + 1):
            if g % d == 0:
                count += 1

                # d and g // d are two distinct divisors
                if d != g // d:
                    count += 1

        return count

        # Complexity analysis
        # Time : O(N * Log(M) + SQRT(M))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Values with Equal Array Remainders - https://www.geeksforgeeks.org/problems/k-modulus-array-element0255/1

    testcase = [
        [[38, 6, 34], 3],
        [[3, 2], 1],
        [[5, 5, 5], -1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.sameMod(*inputs)
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

            val = arr[i]
            if i < len(arr) and val is not None:
                node.left = TreeNode(val)
                q.append(node.left)
            i += 1

            val = arr[i]
            if i < len(arr) and val is not None:
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if node is None:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # longest path passing through this node
            diameter = max(diameter, left_height + right_height)

            # height of this subtree
            return 1 + max(left_height, right_height)

        dfs(root)

        return diameter
        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 543. Diameter of Binary Tree - https://leetcode.com/problems/diameter-of-binary-tree/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [TreeNode.from_list([1, 2, 3, 4, 5]), 3],
        [TreeNode.from_list([1, 2, None]), 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.diameterOfBinaryTree(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 11 of September 2026

    p1()

    p2()

    p3()
