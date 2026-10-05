from collections import deque
from typing import Any, Optional


class Solution1:
    def scoreOfParentheses(self, s: str) -> int:
        # ()
        # if len == 2 or only one pair: return 1
        # call recursion for inner portion of (A), ie. 'A'
        # and return 2 * solve(A)

        N = len(s)

        closing_point = [-1] * N
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                oi = stack.pop()
                closing_point[oi] = i

        def solve(i: int, j: int) -> int:
            # base case: "()"
            if j - i == 1:
                return 1

            # case 1 : (A)
            if closing_point[i] == j:
                return 2 * solve(i + 1, j - 1)

            # case 2 : AB
            score_sum = 0
            curr = i
            while curr <= j:
                nxt = closing_point[curr]
                score_sum += solve(curr, nxt)
                curr = nxt + 1

            return score_sum

        return solve(0, N - 1)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 856. Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/description/?envType=daily-question&envId=2026-10-05

    testcase = [
        ["()", 1],
        ["(())", 2],
        ["()()", 2],
        ["(()()())", 6],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.scoreOfParentheses(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def socialNetwork(self, arr: list[int]) -> list[list[int]]:
        # code here

        N = len(arr) + 1

        result = []

        for i in range(2, N + 1):
            # friend of user i is arr[i - 2], friend always has a smaller number
            # so the chain i -> friend -> friend of friend ... strictly decreases
            chain = []

            j = arr[i - 2]
            k = 1

            while True:
                chain.append([i, j, k])

                # user 1 has no friend, chain ends here
                if j == 1:
                    break

                j = arr[j - 2]
                k += 1

            # chain is in decreasing order of j, need increasing order
            chain.reverse()
            result.extend(chain)

        return result

        # Complexity Analysis
        # Time : O(N^2)
        # Space : O(N^2)


def p2():
    # Problem 2 : POTD Geeksforgeeks Your Social Network - https://www.geeksforgeeks.org/problems/your-social-network0328/1

    testcase = [
        [
            [1, 2],
            [[2, 1, 1], [3, 1, 2], [3, 2, 1]],
        ],
        [
            [1, 1],
            [[2, 1, 1], [3, 1, 1]],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.socialNetwork(*inputs)
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(
            node: Optional[TreeNode], low: Optional[int], high: Optional[int]
        ) -> bool:
            if node is None:
                return True

            # every value must lie strictly within (low, high)
            if low is not None and node.val <= low:
                return False

            if high is not None and node.val >= high:
                return False

            return helper(node.left, low, node.val) and helper(
                node.right, node.val, high
            )

        return helper(root, None, None)

        # Complexity analysis
        # Time : O(N)
        # Space : O(H)


def p3():
    # Problem 3 : NC150 Leetcode 98. Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [TreeNode.from_list([2, 1, 3]), True],
        [TreeNode.from_list([5, 1, 4, None, None, 3, 6]), False],
        [TreeNode.from_list([2, 2, 2]), False],
        [TreeNode.from_list([5, 4, 6, None, None, 3, 7]), False],
        [TreeNode.from_list([1]), True],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.isValidBST(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # Complexity analysis
        # Time : O(N)
        # Space : O(H)


def p4():
    # Problem 4 : NC150 Leetcode 100. Same Tree - https://leetcode.com/problems/same-tree/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [TreeNode.from_list([1, 2, 3]), TreeNode.from_list([1, 2, 3]), True],
        [TreeNode.from_list([1, 2]), TreeNode.from_list([1, None, 2]), False],
        [TreeNode.from_list([1, 2, 1]), TreeNode.from_list([1, 1, 2]), False],
        [TreeNode.from_list([]), TreeNode.from_list([]), True],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.isSameTree(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 5 of October 2026

    p1()

    p2()

    p3()

    p4()
