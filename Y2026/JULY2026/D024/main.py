from typing import Optional


class Solution1:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        N = len(nums)
        max_el = max(nums)

        T = 1
        while T <= max_el:
            T <<= 1

        xor_pairs = [False] * T
        xor_triplets = [False] * T

        for i in range(N):
            for j in range(i, N):
                xor_pairs[nums[i] ^ nums[j]] = True

        for x in range(T):
            if xor_pairs[x]:
                for num in nums:
                    xor_triplets[x ^ num] = True

        return sum(xor_triplets)

        # Complexity analysis
        # Time : O(N * N + N * maxElement)
        # Space: O(maxElement)


def p1():
    # Problem 1 : POTD Leetcode 3514. Number of Unique XOR Triplets II - https://leetcode.com/problems/number-of-unique-xor-triplets-ii/description/?envType=daily-question&envId=2026-07-24

    testcase = [
        [[1, 3], 2],
        [[6, 7, 8, 9], 4],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.uniqueXorTriplets(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


# Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    @staticmethod
    def build(values: list) -> Optional["Node"]:
        """Level-order construction from a list (None = missing node)."""
        if not values:
            return None
        root = Node(values[0])
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            if i < len(values) and values[i] is not None:
                node.left = Node(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = Node(values[i])
                queue.append(node.right)
            i += 1
        return root

    def to_list(self) -> list:
        """Level-order serialization for assertion comparison."""
        result, queue = [], [self]
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result


class Solution2:
    def longestConsecutive(self, root: Optional[Node]) -> int:
        longest = 0

        def dfs(node: Optional[Node], parent: Optional[Node], length: int):
            nonlocal longest

            if not node:
                return

            if parent and node.data == parent.data + 1:
                length += 1
            else:
                length = 1

            longest = max(longest, length)

            dfs(node.left, node, length)
            dfs(node.right, node, length)

        dfs(root, None, 0)

        return -1 if longest == 1 else longest

        # Complexity analysis
        # Time : O(N)
        # Space: O(H)


def p2():
    # Problem 2 : POTD Geeksforgeeks Longest Consecutive Path in Binary tree - https://www.geeksforgeeks.org/problems/longest-consecutive-sequence-in-binary-tree/1

    testcase = [
        [Node.build([1, 2, 3]), 2],
        [Node.build([10, 20, 30, 40, None, 60, 90]), -1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.longestConsecutive(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 24 of July 2026

    p1()

    p2()
