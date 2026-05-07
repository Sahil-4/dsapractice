from collections import deque
from typing import List, Optional


class Solution1:
    def maxValue(self, nums: List[int]) -> List[int]:
        groups = []

        for idx, value in enumerate(nums):
            start = idx
            best = value

            while groups and groups[-1][0] > value:
                prev_best, left, _ = groups.pop()

                best = max(best, prev_best)
                start = left

            groups.append((best, start, idx))

        ans = [0] * len(nums)

        for highest, left, right in groups:
            for i in range(left, right + 1):
                ans[i] = highest

        return ans

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3660. Jump Game IX - https://leetcode.com/problems/jump-game-ix/description/?envType=daily-question&envId=2026-05-07

    testcase = [
        [[2, 1, 3], [2, 2, 3]],
        [[2, 3, 1], [3, 3, 3]],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.maxValue(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


# Definition for Node
class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @staticmethod
    def from_list(arr: List[Optional[int]]) -> Optional["Node"]:
        if not arr:
            return None

        root = Node(arr[0])
        q: deque[Node] = deque([root])

        i = 1
        while q and i < len(arr):
            node = q.popleft()

            if i < len(arr) and arr[i] is not None:
                node.left = Node(arr[i])
                q.append(node.left)
            i += 1

            if i < len(arr) and arr[i] is not None:
                node.right = Node(arr[i])
                q.append(node.right)
            i += 1

        return root


class Solution2:
    def pre_order(self, root: Optional["Node"]) -> List[str]:
        if not root:
            return []

        traversal = []

        traversal.append("(")
        traversal.append(str(root.data))
        traversal.extend(self.pre_order(root.left))
        traversal.extend(self.pre_order(root.right))
        traversal.append(")")

        return traversal

    def isSubTree(self, root1: Optional["Node"], root2: Optional["Node"]) -> bool:
        # code here
        # get pre-order traversal of both tree tr1, tr2
        # if tr2 is in tr1 return true else return false

        tr1_str = "".join(self.pre_order(root1))
        tr2_str = "".join(self.pre_order(root2))

        return tr2_str in tr1_str

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Check if subtree - https://www.geeksforgeeks.org/problems/check-if-subtree/1

    testcase = [
        [[1, 2, 3, None, None, 4], [3, 4], True],
        [[26, 10, None, 20, 30, 40, 60], [26, 10, None, 20, 30, 40, 60], True],
        [[1, 2, 3, 3, 12], [12, 3], False],
    ]

    for line in testcase:
        [arr1, arr2, expected] = line
        s2 = Solution2()
        root1 = Node.from_list(arr1)
        root2 = Node.from_list(arr2)
        result = s2.isSubTree(root1, root2)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 7 of May 2026

    p1()

    p2()
