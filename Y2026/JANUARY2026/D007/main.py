from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def build(cls, arr, FLAG=None):
        if not arr or arr[0] == FLAG:
            return None

        root = cls(arr[0])
        q = deque([root])
        i = 1

        while q and i < len(arr):
            node = q.popleft()

            # left child
            if i < len(arr) and arr[i] != FLAG:
                node.left = cls(arr[i])
                q.append(node.left)
            i += 1

            # right child
            if i < len(arr) and arr[i] != FLAG:
                node.right = cls(arr[i])
                q.append(node.right)
            i += 1

        return root


class Solution1:
    MOD = 1000000007
    tsum = 0
    answer = 0

    def tree_node_sum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        sum = root.val

        sum += self.tree_node_sum(root.left)
        sum += self.tree_node_sum(root.right)

        return sum

    def find_max_sum_product(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftsum = self.find_max_sum_product(root.left)
        rightsum = self.find_max_sum_product(root.right)

        subsum = root.val + leftsum + rightsum

        product = subsum * (self.tsum - subsum)
        self.answer = max(self.answer, product)

        return subsum

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # use dfs traversal
        # first calculate the sum of all nodes val, calling it tsum
        # init variable answer to track maximum product
        # traverse tree again
        # at each point
        # calculate sum of subtree, subsum
        # assume we are cutting the edge connecting current node
        # at this point product will be (subsum * (tsum - subsum))
        # update answer

        self.answer = 0
        self.tsum = self.tree_node_sum(root)
        self.find_max_sum_product(root)

        return self.answer % self.MOD

        # Complexity analysis
        # Time : O(2N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1339. Maximum Product of Splitted Binary Tree - https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/?envType=daily-question&envId=2026-01-07

    testcase = [
        [[1, 2, 3, 4, 5, 6], 110],
        [[1, None, 2, 3, 4, None, None, 5, 6], 90],
    ]

    for line in testcase:
        [arr, expected] = line
        s1 = Solution1()
        root = TreeNode.build(arr)
        result = s1.maxProduct(root)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countDistinct(self, arr, k):
        # Code here
        # use sliding window approach
        # use count variable to count unique elements
        # use a map to count and update frequency of elements when moving in right
        # if frequency becomes 1 from 0 increment unique count
        # while shrinking decrement frequency
        # if frequency becomes 0 from 1 decrement unique count

        N = len(arr)

        window_unique_count = []
        unique_count = 0
        frequency_map = dict()

        for i in range(N):
            # expand
            if arr[i] not in frequency_map or frequency_map[arr[i]] == 0:
                frequency_map[arr[i]] = 0
                unique_count += 1

            frequency_map[arr[i]] += 1

            # new window found
            if i - k + 1 >= 0:
                window_unique_count.append(unique_count)

                # shrink
                frequency_map[arr[i - k + 1]] -= 1
                if frequency_map[arr[i - k + 1]] == 0:
                    unique_count -= 1

        return window_unique_count

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count distinct elements in every window - https://www.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1

    testcase = [
        [[1, 2, 1, 3, 4, 2, 3], 4, [3, 4, 4, 3]],
        [[4, 1, 1], 2, [2, 1]],
        [[1, 1, 1, 1, 1], 3, [1, 1, 1]],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.countDistinct(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 7 of January 2026

    p1()

    p2()
