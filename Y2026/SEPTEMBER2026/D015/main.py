from collections import deque
from typing import Any, Optional


class Solution1:
    def maxPalindromes(self, s: str, k: int) -> int:
        N = len(s)

        # pal[i][j] == True iff s[i:j+1] is a palindrome
        pal = [[False] * N for _ in range(N)]

        # palindrome table by increasing substring length
        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                if s[i] == s[j] and (j - i <= 1 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        # dp[i] = maximum number of valid non-overlapping
        # palindromes in s[:i]
        dp = [0] * (N + 1)

        for j in range(N):
            # do not select a palindrome ending at j
            dp[j + 1] = dp[j]

            # try every palindrome ending at j
            for i in range(j + 1):
                length = j - i + 1

                if length >= k and pal[i][j]:
                    # s[i:j+1] is selected
                    # dp[i] only uses characters before i,
                    # so the selected substrings cannot overlap
                    dp[j + 1] = max(dp[j + 1], dp[i] + 1)

        return dp[N]

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(N*N)


def p1():
    # Problem 1 : POTD Leetcode 2472. Maximum Number of Non-overlapping Palindrome Substrings - https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/description/?envType=daily-question&envId=2026-09-15

    testcase = [
        ["abaccdbbd", 3, 2],
        ["adbcda", 2, 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maxPalindromes(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
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

            data = arr[i]
            if i < len(arr) and data is not None:
                node.left = Node(data)
                q.append(node.left)
            i += 1

            data = arr[i]
            if i < len(arr) and data is not None:
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
    def getCount(self, root: Node, k: int) -> int:
        # code here

        leaf_nodes_cost = []

        def collect_leafs(node: Node, level: int):
            if not node.left and not node.right:
                leaf_nodes_cost.append(level)
                return

            if node.left:
                collect_leafs(node.left, level + 1)

            if node.right:
                collect_leafs(node.right, level + 1)

        collect_leafs(root, 1)

        leaf_nodes_cost.sort()
        count = 0
        for cost in leaf_nodes_cost:
            if cost > k:
                break

            count += 1
            k -= cost

        return count

        # Complexity analysis
        # Time : O(N)
        # Space : O(N) stack


def p2():
    # Problem 2 : POTD Geeksforgeeks Visit Leaves with Budget - https://www.geeksforgeeks.org/problems/leaf-under-budget/1

    testcase = [
        [Node.from_list([10, 8, 2, 3, None, 3, 6, None, None, None, 4]), 8, 2],
        [Node.from_list([1, 2, 3, 4, 5, 6, 7]), 5, 1],
        [Node.from_list([1]), 1, 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.getCount(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def add(self, arr1: list[int], arr2: list[int]) -> list[int]:
        result: list[int] = []

        N = len(arr1)
        M = len(arr2)

        carry = 0
        i = 0
        j = 0

        while i < N or j < M or carry > 0:
            digits_sum = 0

            if i < N:
                digits_sum += arr1[i]
                i += 1

            if j < M:
                digits_sum += arr2[j]
                j += 1

            if carry > 0:
                digits_sum += carry

            carry = digits_sum // 10
            result_digit = digits_sum % 10

            result.append(result_digit)

        return result

    def multiply(self, num1: str, num2: str) -> str:
        result: list[int] = []

        N = len(num1)
        M = len(num2)

        for j in range(M - 1, -1, -1):
            carry = 0
            multiplication_result = [0] * (M - 1 - j)

            for i in range(N - 1, -1, -1):
                _mul = int(num2[j]) * int(num1[i]) + carry
                _carry = _mul // 10
                _digit = _mul % 10

                carry = _carry
                multiplication_result.append(_digit)

            if carry > 0:
                multiplication_result.append(carry)

            result = self.add(result, multiplication_result)

        while len(result) > 1 and result[-1] == 0:
            result.pop()

        result.reverse()
        return "".join([str(digit) for digit in result])

        # Complexity analysis
        # Time : O(M * (N + (N + M)))
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 43. Multiply Strings - https://leetcode.com/problems/multiply-strings/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["2", "3", "6"],
        ["123", "456", "56088"],
        ["123", "0", "0"],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.multiply(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 15 of September 2026

    p1()

    p2()

    p3()
