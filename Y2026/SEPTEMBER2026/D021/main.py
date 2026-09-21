from collections import deque
from typing import Any, Optional


class Solution1:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        result = [0] * k
        dp = [0] * k

        for num in nums:

            # counts of subarrays ending at current index
            new_dp = [0] * k

            # case 1: subarray containing only num
            remainder = num % k
            new_dp[remainder] += 1

            # add single-element subarray to answer
            result[remainder] += 1

            # case 2: extend previous subarrays
            for remainder in range(k):
                count = dp[remainder]

                if count > 0:
                    new_r = (remainder * num) % k

                    new_dp[new_r] += count
                    result[new_r] += count

            dp = new_dp

        return result

        # Complexity analysis
        # Time : O(N * K)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3524. Find X Value of Array I - https://leetcode.com/problems/find-x-value-of-array-i/description/?envType=daily-question&envId=2026-09-21

    testcase = [
        [[1, 2, 3, 4, 5], 3, [9, 2, 4]],
        [[1, 2, 4, 8, 16, 32], 4, [18, 1, 2, 0]],
        [[1, 1, 2, 1, 1], 2, [9, 6]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.resultArray(*inputs)
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
    def areAnagrams(self, root1: Node, root2: Node) -> bool:
        """code here"""

        queue1 = deque([root1])
        queue2 = deque([root2])

        while queue1 or queue2:
            N = len(queue1)
            M = len(queue2)

            if N != M:
                return False

            val_frequency = dict()

            for _ in range(N):
                node = queue1.popleft()

                if node.data not in val_frequency.keys():
                    val_frequency[node.data] = 0

                val_frequency[node.data] += 1

                if node.left is not None:
                    queue1.append(node.left)

                if node.right is not None:
                    queue1.append(node.right)

            for _ in range(M):
                node = queue2.popleft()

                if (
                    node.data not in val_frequency.keys()
                    or val_frequency[node.data] == 0
                ):
                    return False

                val_frequency[node.data] -= 1

                if node.left is not None:
                    queue2.append(node.left)

                if node.right is not None:
                    queue2.append(node.right)

        return True

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Check Level Anagrams in Binary Trees - https://www.geeksforgeeks.org/problems/check-if-all-levels-of-two-trees-are-anagrams-or-not/1

    testcase = [
        [
            Node.from_list([1, 3, 2, None, None, 5, 4]),
            Node.from_list([1, 2, 3, 4, 5, None, None]),
            True,
        ],
        [
            Node.from_list([1, 2, 3, 5, 4]),
            Node.from_list([1, 2, 4, 5, 3]),
            False,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.areAnagrams(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        N = len(matrix)
        M = len(matrix[0])

        traversal = []

        rs, re = 0, N - 1
        cs, ce = 0, M - 1

        while rs <= re and cs <= ce:

            # top row
            for c in range(cs, ce + 1, +1):
                traversal.append(matrix[rs][c])

            rs += 1

            # right column
            for r in range(rs, re + 1, +1):
                traversal.append(matrix[r][ce])

            ce -= 1

            # avoid duplication/revisit
            if not (rs <= re and cs <= ce):
                break

            # bottom row
            for c in range(ce, cs - 1, -1):
                traversal.append(matrix[re][c])

            re -= 1

            # left column
            for r in range(re, rs - 1, -1):
                traversal.append(matrix[r][cs])

            cs += 1

        return traversal

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 54. Spiral Matrix - https://leetcode.com/problems/spiral-matrix/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        ],
        [
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.spiralOrder(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def canJump(self, nums: list[int]) -> bool:
        N = len(nums)

        if N == 1:
            return True

        max_reach = 0

        for i in range(N):
            reach = i + nums[i]
            max_reach = max(max_reach, reach)

            if max_reach <= i:
                return False

            if max_reach == N - 1:
                return True

        return True

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p4():
    # Problem 4 : NC150 Leetcode 55. Jump Game - https://leetcode.com/problems/jump-game/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[2, 3, 1, 1, 4], True],
        [[3, 2, 1, 0, 4], False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.canJump(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 21 of September 2026

    p1()

    p2()

    p3()

    p4()
