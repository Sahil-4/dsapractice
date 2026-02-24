from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_list(arr: List[Optional[int]]) -> Optional["TreeNode"]:
        if not arr:
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


class Solution1:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        # use tree traversal
        # build a binary number
        # on leaf node we have to update sum

        tsum = 0

        def calculate_sum(root: TreeNode, num: int):
            nonlocal tsum

            num = (num << 1) | root.val

            if not root.left and not root.right:
                tsum += num
                return

            if root.left:
                calculate_sum(root.left, num)

            if root.right:
                calculate_sum(root.right, num)

        calculate_sum(root, 0)

        return tsum

        # Complexity analysis
        # Time : O(N)
        # Space : O(D)


def p1():
    # Problem 1 : POTD Leetcode 1022. Sum of Root To Leaf Binary Numbers - https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/?envType=daily-question&envId=2026-02-24

    testcase = [
        [[1, 0, 1, 0, 1, 0, 1], 22],
        [[0], 0],
    ]

    for line in testcase:
        [arr, expected] = line
        s1 = Solution1()
        root = TreeNode.from_list(arr)
        result = s1.sumRootToLeaf(root)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def equalSumSpan(self, a1, a2):
        # code here
        N = len(a1)

        mp = dict()

        mp[0] = -1  # 0 -> i

        psum = 0
        mlen = 0

        for i in range(N):
            psum += a1[i] - a2[i]

            if psum in mp:
                mlen = max(mlen, i - mp[psum])
            else:
                mp[psum] = i

        return mlen

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Longest Span in two Binary Arrays - https://www.geeksforgeeks.org/problems/longest-span-with-same-sum-in-two-binary-arrays5142/1

    testcase = [
        [[0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 1], 4],
        [[0, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1], 6],
        [[0, 0, 0], [1, 1, 1], 0],
    ]

    for line in testcase:
        [a1, a2, expected] = line
        s2 = Solution2()
        result = s2.equalSumSpan(a1, a2)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 24 of February 2026

    p1()

    p2()
