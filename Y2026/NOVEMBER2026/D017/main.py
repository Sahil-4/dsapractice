from collections import deque
from typing import List, Any, Optional


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

            if i < len(arr) and arr[i] is not None:
                node.left = TreeNode(arr[i])
                q.append(node.left)
            i += 1

            if i < len(arr) and arr[i] is not None:
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1

        return root

    def to_list(self) -> List[Any]:
        result = []
        q = deque([self])

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
    def minimumChanges(self, s: str, k: int) -> int:
        N = len(s)
        INF = float("inf")

        # divisors[length] : every d with 1 <= d < length and length % d == 0
        divisors = [[] for _ in range(N + 1)]
        for length in range(2, N + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)

        # cost[i][j] : minimum changes to make s[i..j] a semi-palindrome
        cost = [[INF] * N for _ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                length = j - i + 1

                for d in divisors[length]:
                    changes = 0

                    # indices with the same remainder modulo d form one group,
                    # every group has to be a palindrome
                    for r in range(d):
                        low = i + r
                        high = i + r + ((length // d) - 1) * d

                        while low < high:
                            if s[low] != s[high]:
                                changes += 1
                            low += d
                            high -= d

                    cost[i][j] = min(cost[i][j], changes)

        # dp[p][j] : minimum changes to split the first j characters into p parts
        dp = [[INF] * (N + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for j in range(2 * p, N + 1):
                for i in range(2 * (p - 1), j - 1):
                    if dp[p - 1][i] != INF and cost[i][j - 1] != INF:
                        dp[p][j] = min(dp[p][j], dp[p - 1][i] + cost[i][j - 1])

        return dp[k][N]

        # Complexity analysis
        # Time : O(N^3 + N^2 * K), N = len(s)
        # Space : O(N^2)


def p1():
    # Problem 1 : POTD Leetcode 2911. Minimum Changes to Make K Semi-palindromes - https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/description/?envType=daily-question&envId=2026-11-17

    testcase = [
        ["abcac", 2, 1],
        ["abcdef", 2, 2],
        ["aabbaa", 3, 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minimumChanges(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findPattern(self, s: str) -> bool:
        N = len(s)
        i = 0

        while i < N:
            # every block is a run of x followed by a run of y of the same length
            x_count = 0
            while i < N and s[i] == "x":
                x_count += 1
                i += 1

            y_count = 0
            while i < N and s[i] == "y":
                y_count += 1
                i += 1

            if x_count == 0 or x_count != y_count:
                return False

        return True

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Repeated Pattern Check - https://www.geeksforgeeks.org/problems/the-pattern-matcher/1

    testcase = [
        ["xxyyxy", True],
        ["xxyyxxyy", True],
        ["xxxyyyxxyyxy", True],
        ["xy", True],
        ["xxyyx", False],
        ["xyx", False],
        ["yx", False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.followsPattern(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        q = deque([root])

        while q:
            node = q.popleft()

            # swap the two children, then continue with the (swapped) children
            node.left, node.right = node.right, node.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root

        # Complexity analysis
        # Time : O(N)
        # Space : O(W), W = maximum width of the tree


def p3():
    # Problem 3 : NC150 Leetcode 226. Invert Binary Tree - https://leetcode.com/problems/invert-binary-tree/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]],
        [[2, 1, 3], [2, 3, 1]],
        [[], []],
    ]

    for line in testcase:
        [arr, expected] = line
        s3 = Solution3()
        root = s3.invertTree(TreeNode.from_list(arr))
        result = root.to_list() if root else []
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 17 of November 2026

    p1()

    p2()

    p3()
