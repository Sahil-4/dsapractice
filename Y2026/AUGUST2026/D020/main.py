from typing import Optional


class Solution1:
    def resultArray(self, nums: list[int]) -> list[int]:
        N = len(nums)

        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, N):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3069. Distribute Elements Into Two Arrays I - https://leetcode.com/problems/distribute-elements-into-two-arrays-i/description/?envType=daily-question&envId=2026-08-20

    testcase = [
        [[2, 1, 3], [2, 3, 1]],
        [[5, 4, 3, 8], [5, 3, 4, 8]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.resultArray(*inputs)
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
    def maxDiff(self, root: Node) -> int:
        # code here

        def solve(node: Node) -> tuple[int, int]:
            min_node_value = node.data
            max_difference = -1000000007

            if node.left:
                min_node_value_left, max_difference_left = solve(node.left)
                min_node_value = min(min_node_value, min_node_value_left)
                max_difference = max(
                    max_difference, max_difference_left, node.data - min_node_value_left
                )

            if node.right:
                min_node_value_right, max_difference_right = solve(node.right)
                min_node_value = min(min_node_value, min_node_value_right)
                max_difference = max(
                    max_difference,
                    max_difference_right,
                    node.data - min_node_value_right,
                )

            return (min_node_value, max_difference)

        return solve(root)[1]

        # Complexity analysis
        # Time : O(N)
        # Space : O(H)


def p2():
    # Problem 2 : POTD Geeksforgeeks Node and Ancestor Max Diff - https://www.geeksforgeeks.org/problems/maximum-difference-between-node-and-its-ancestor/1

    testcase = [
        [Node.build([5, 2, 1]), 4],
        [Node.build([1, 2, 3, None, None, None, 7]), -1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxDiff(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 20 of August 2026

    p1()

    p2()
