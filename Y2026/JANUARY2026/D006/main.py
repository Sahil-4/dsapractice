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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # use level order traversal
        # at each level calculate sum of all nodes
        # update maximum level sum and minimum level
        # at the end return minimum level

        T = -1000000

        maximum_sum = T
        min_level = 0
        level = 0

        dq = deque()
        dq.append(root)

        while dq:
            level += 1
            level_sum = 0

            LN = len(dq)

            for _ in range(LN):
                node = dq.popleft()

                level_sum += node.val

                if node.left:
                    dq.append(node.left)

                if node.right:
                    dq.append(node.right)

            if maximum_sum < level_sum:
                maximum_sum = level_sum
                min_level = level

        return min_level

        # Complexity analysis
        # Time : O(N)
        # Space : O(W)


def p1():
    # Problem 1 : POTD Leetcode 1161. Maximum Level Sum of a Binary Tree - https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=daily-question&envId=2026-01-06

    testcase = [
        [[1, 7, 0, 7, -8, None, None], 2],
        [[989, None, 10250, 98693, -89388, None, None, None, -32127], 2],
    ]

    for line in testcase:
        [arr, expected] = line
        s1 = Solution1()
        root = TreeNode.build(arr, None)
        result = s1.maxLevelSum(root)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxSubarrayXOR(self, arr, k):
        # code here
        # if we have computed xor = a XOR b XOR c
        # and we want to remove `a` we can do xor = xor XOR a
        # we can use sliding window technique
        # maintain a window of size k,
        # xor is precomputed - while creating or updating window
        # for all subarray of size k
        # find the max xor and return it

        N = len(arr)
        max_xor = 0

        xor = 0
        for i in range(N):
            xor = xor ^ arr[i]
            if i >= k:
                xor = xor ^ arr[i - k]

            if i >= k - 1:
                max_xor = max(max_xor, xor)

        return max_xor

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Xor Subarray of size K - https://www.geeksforgeeks.org/problems/max-xor-subarray-of-size-k/1

    testcase = [
        [[2, 5, 8, 1, 1, 3], 3, 15],
        [[1, 2, 4, 5, 6], 2, 6],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.maxSubarrayXOR(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 6 of January 2026

    p1()

    p2()
