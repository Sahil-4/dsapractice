from collections import deque
from typing import Any, Optional


class Solution1:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        N = len(s)

        # find the first and last occurrence of each character
        first = [N] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord("a")
            first[idx] = min(first[idx], i)
            last[idx] = i

        # find all valid minimal substrings
        intervals = []

        for i in range(N):
            idx = ord(s[i]) - ord("a")

            # only start from the first occurrence of a character
            if i != first[idx]:
                continue

            left = i
            right = last[idx]
            j = left
            valid = True

            while j <= right:
                char_idx = ord(s[j]) - ord("a")

                # this character occurs before the current interval
                if first[char_idx] < left:
                    valid = False
                    break

                # expand the interval to include all occurrences
                right = max(right, last[char_idx])
                j += 1

            if valid:
                intervals.append((left, right))

        # select non-overlapping intervals greedily
        # sort by ending position to maximize the number of substrings
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                result.append(s[left : right + 1])
                prev_end = right

        return result

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1520. Maximum Number of Non-Overlapping Substrings - https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/description/?envType=daily-question&envId=2026-09-18

    testcase = [
        ["adefaddaccc", ["e", "f", "ccc"]],
        ["abbaccd", ["d", "bb", "cc"]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maxNumOfSubstrings(*inputs)
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
    def absDiff(self, root: Node) -> int:
        # In-order traversal of a BST produces sorted values,
        # minimum absolute difference must be between
        # two consecutive values in sorted order

        min_diff = 10**8

        stack = []
        current = root
        prev = None

        while stack or current:
            # traverse left subtree
            while current:
                stack.append(current)
                current = current.left

            # Process the current node
            current = stack.pop()

            if prev is not None:
                min_diff = min(min_diff, current.data - prev)

            prev = current.data

            # traverse right subtree
            current = current.right

        return min_diff

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Absolute Difference In BST - https://www.geeksforgeeks.org/problems/minimum-absolute-difference-in-bst-1665139652/1

    testcase = [
        [[50, 30, 70, 20, None, 60, 80], 10],
        [[60, 30, 90, 10], 20],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.absDiff(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def myPow(self, x: float, n: int) -> float:
        # negative exponents
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0

        # binary exponentiation
        while n > 0:
            # odd exponent
            if n % 2 == 1:
                result *= x

            # square the base
            x *= x

            # halve the exponent
            n //= 2

        return result

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 50. Pow(x, N) - https://leetcode.com/problems/powx-N/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [2.00000, 10, 1024.00000],
        [2.10000, 3, 9.26100],
        [2.00000, -2, 0.25000],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.myPow(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 18 of September 2026

    p1()

    p2()

    p3()
