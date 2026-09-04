from collections import deque
from typing import Any, Optional


class Solution1:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        N = len(nums)

        for i in range(N):
            instability_score = max(nums[0 : i + 1]) - min(nums[i:])
            if instability_score <= k:
                return i

        return -1

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3903. Smallest Stable Index I - https://leetcode.com/problems/smallest-stable-index-i/description/?envType=daily-question&envId=2026-09-04

    testcase = [
        [[5, 0, 1, 4], 3, 3],
        [[3, 2, 1], 1, -1],
        [[0], 0, 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.firstStableIndex(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxFruits(self, arr: list[int], M: int) -> int:
        """code here"""

        N = len(arr)

        maximum_total_fruits = sum(arr[:M])
        temp_maximum_total_fruits = maximum_total_fruits

        for i in range(M, 2 * N):
            temp_maximum_total_fruits -= arr[(i - M) % N]
            temp_maximum_total_fruits += arr[i % N]

            maximum_total_fruits = max(maximum_total_fruits, temp_maximum_total_fruits)

        return maximum_total_fruits

        # Complexity analysis
        # Time : O(2N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Bird and Max Fruit Gathering - https://www.geeksforgeeks.org/problems/bird-and-maximum-fruit-gathering--170645/1

    testcase = [
        [[2, 1, 3, 5, 0, 1, 4], 3, 9],
        [[1, 6, 2, 5, 3, 4], 2, 8],
        [[7, 2, 1, 3, 4], 2, 11],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxFruits(*inputs)
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
    def goodNodes(self, root: TreeNode) -> int:

        def helper(node: Optional[TreeNode], max_val: int) -> int:
            # base case
            if node is None:
                return 0

            count = 0

            count += 1 if node.val >= max_val else 0

            count += helper(node.left, max(max_val, node.val))
            count += helper(node.right, max(max_val, node.val))

            return count

        return helper(root, root.val)

        # Complexity analysis
        # Time : O(N)
        # Space : O(H)


def p3():
    # Problem 3 : NC150 Leetcode 1448. Count Good Nodes in Binary Tree - https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [TreeNode.from_list([3, 1, 4, 3, None, 1, 5]), 4],
        [TreeNode.from_list([3, 3, None, 4, 2]), 3],
        [TreeNode.from_list([1]), 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.goodNodes(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def isMatch(self, s: str, p: str) -> bool:
        SN = len(s)
        PN = len(p)

        def helper(si: int, pi: int) -> bool:

            # case 1:
            # pattern is completely consumed
            # match succeeds only if string is also consumed
            if pi == PN:
                return si == SN

            # case 2:
            # does current pattern character match current string character?
            first_match = si < SN and (s[si] == p[pi] or p[pi] == ".")

            # case 3:
            # current pattern element is followed by '*'
            # example:
            #   p = "a*"
            #        ^
            #       pi
            #
            if pi + 1 < PN and p[pi + 1] == "*":

                # case 3A:
                # '*' matches zero occurrences
                # skip the entire "a*" / ".*"
                zero = helper(si, pi + 2)

                # case 3B:
                # '*' matches one or more occurrences
                # consume one character from s,
                # but stay on the same pattern element
                one_or_more = first_match and helper(si + 1, pi)

                return zero or one_or_more

            # case 4:
            # normal character or '.'
            # both consume exactly one character
            return first_match and helper(si + 1, pi + 1)

        return helper(0, 0)

        # Complexity analysis
        # Time : O(2^(T + P))
        # Space : O(T + P)


def p4():
    # Problem 3 : NC150 Leetcode 10. Regular Expression Matching - https://leetcode.com/problems/regular-expression-matching/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["aa", "a", False],
        ["aa", "a*", True],
        ["ab", ".*", True],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.isMatch(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 4 of September 2026

    p1()

    p2()

    p3()

    p4()
