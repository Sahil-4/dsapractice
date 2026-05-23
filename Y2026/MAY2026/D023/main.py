from typing import List, Optional, Optional


class Solution1:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        count = 0

        for i in range(1, N):
            if nums[i] < nums[i - 1]:
                count += 1

        if nums[N - 1] > nums[0]:
            count += 1

        return count <= 1

        # Complexity Analysis:
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1752. Check if Array Is Sorted and Rotated - https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/?envType=daily-question&envId=2026-05-23

    testcase = [
        [[3, 4, 5, 1, 2], True],
        [[2, 1, 3, 4], False],
        [[1, 2, 3], True],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.check(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


# Structure for Tree Node
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
    def toSumTree(self, root: Optional[Node]) -> Optional[Node]:
        # code here

        def _post_order_sum(node: Optional[Node]) -> int:
            """
            Returns the sum of all original values in the subtree rooted at `node`.
            Mutates each node's .data to equal left_sum + right_sum (original children sums).
            """
            if node is None:
                return 0

            left_sum = _post_order_sum(node.left)  # original sum of left subtree
            right_sum = _post_order_sum(node.right)  # original sum of right subtree

            original = node.data  # preserve before overwrite
            node.data = left_sum + right_sum  # leaf nodes → 0 + 0 = 0

            # propagate full subtree total upward
            return original + left_sum + right_sum

        _post_order_sum(root)

        return root

        # Complexity Analysis:
        # Time : O(N)
        # Space : O(H)


def p2():
    # Problem 2 : POTD Geeksforgeeks Transform to Sum Tree - https://www.geeksforgeeks.org/problems/transform-to-sum-tree/1

    testcase = [
        [[10, -2, 6, 8, -4, 7, 5], [20, 4, 12, 0, 0, 0, 0]],
        [[1, 2, 3, 4, 5, -6, 2], [10, 9, -4, 0, 0, 0, 0]],
        [[1], [0]],
    ]

    for line in testcase:
        [input_vals, expected] = line
        s2 = Solution2()
        root = Node.build(input_vals)
        result = s2.toSumTree(root)
        output = Node.to_list(result) if result else []
        assert output == expected, f"Test failed: expected {expected}, got {output}"
        print(f"Testcase passed (P2): result={output}")


if __name__ == "__main__":
    # Day 23 of May 2026

    p1()

    p2()
