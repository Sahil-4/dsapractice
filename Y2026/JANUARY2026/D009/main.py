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

    @classmethod
    def to_list(cls, root, FLAG=None):
        if not root:
            return []

        arr = []
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                arr.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                arr.append(FLAG)

        # remove trailing FLAGs
        while arr and arr[-1] == FLAG:
            arr.pop()

        return arr


class Solution1:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # use dfs traversal
        # at each step return
        # depth and potential answer node
        # if both subtrees returns same depth then answer will be root
        # else answer will node with greater depth

        def dfs(node):
            if not node:
                return (0, None)

            ld, ln = dfs(node.left)
            rd, rn = dfs(node.right)

            if ld > rd:
                return (ld + 1, ln)
            elif rd > ld:
                return (rd + 1, rn)
            else:
                return (ld + 1, node)

        return dfs(root)[1]

        # Complexity analysis
        # Time: O(N)
        # Space: O(H) (recursion stack)


def p1():
    # Problem 1 : POTD Leetcode 865. Smallest Subtree with all the Deepest Nodes - https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/?envType=daily-question&envId=2026-01-09

    testcase = [
        [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [2, 7, 4]],
        [[1], [1]],
        [[0, 1, 3, None, 2], [2]],
    ]

    for line in testcase:
        [arr, expected] = line
        s1 = Solution1()
        root = TreeNode.build(arr)
        subtree = s1.subtreeWithAllDeepest(root)
        result = TreeNode.to_list(subtree)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countAtMostK(self, arr, k):
        # Code here
        # arr[] = [1, 2, 1, 1, 3, 3, 4, 2, 1], k = 2
        # 1 + 2 + 3 + 4 + 3 + 4 + 3 + 2 + 2
        # use sliding window (two pointers left and right)
        # move right towards right
        # update element frequency
        # check if distinct count > k
        # shift left towards right while distinct count > k
        # increment the count by (right - left + 1) i.e. total subarray possible
        # use map to store elements frequency and counter variable to count distinct

        subarray_count = 0
        distinct_count = 0
        element_frequency = dict()

        N = len(arr)

        left = 0
        for right in range(N):
            if arr[right] not in element_frequency:
                distinct_count += 1
                element_frequency[arr[right]] = 0
            element_frequency[arr[right]] += 1

            while distinct_count > k:
                element_frequency[arr[left]] -= 1
                if element_frequency[arr[left]] == 0:
                    distinct_count -= 1
                    del element_frequency[arr[left]]
                left += 1

            subarray_count += right - left + 1

        return subarray_count

        # Complexity analysis
        # Time : O(N)
        # Space : O(K)


def p2():
    # Problem 2 : POTD Geeksforgeeks Subarrays With At Most K Distinct Integers - https://www.geeksforgeeks.org/problems/subarrays-with-at-most-k-distinct-integers/1

    testcase = [
        [[1, 2, 2, 3], 2, 9],
        [[1, 1, 1], 1, 6],
        [[1, 2, 1, 1, 3, 3, 4, 2, 1], 2, 24],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.countAtMostK(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 9 of January 2026

    p1()

    p2()
