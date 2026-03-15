from collections import deque
from typing import List, Optional


class Solution1:
    def getHappyString(self, n: int, k: int) -> str:

        result = ""
        count = 0
        curr = []

        def solve():
            nonlocal count, result

            if len(curr) == n:
                count += 1
                if count == k:
                    result = "".join(curr)
                return

            for ch in ["a", "b", "c"]:

                if curr and curr[-1] == ch:
                    continue

                curr.append(ch)

                solve()

                if result:
                    return

                curr.pop()

        solve()

        return result

        # Complexity analysis
        # Time : O(N * 2^N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1415. The k-th Lexicographical String of All Happy Strings of Length n - https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/?envType=daily-question&envId=2026-03-14

    testcase = [
        [1, 3, "c"],
        [1, 4, ""],
        [3, 9, "cab"],
    ]

    for line in testcase:
        [n, k, expected] = line
        s1 = Solution1()
        result = s1.getHappyString(n, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


# Definition for a binary tree node.
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
    def topView(self, root: Optional[Node]) -> List[int]:
        # code here
        # traverse in level order
        # root will be at 0
        # left of root will be at 0 - 1
        # left of left of root will be at 0 - 1 - 1
        # and so on
        # prepare a map while doing traversal
        # only add in map dont update
        # finally return the values

        if not root:
            return []

        q = deque([(root, 0)])  # (node, horizontal_distance)
        hd_map = {}

        while q:
            node, hd = q.popleft()

            # store only the first node encountered at this HD
            if hd not in hd_map:
                hd_map[hd] = node.data

            if node.left:
                q.append((node.left, hd - 1))

            if node.right:
                q.append((node.right, hd + 1))

        # return values sorted by horizontal distance
        return [hd_map[k] for k in sorted(hd_map)]

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Top View of Binary Tree - https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1

    testcase: List[List[List[Optional[int]]]] = [
        [[1, 2, 3], [2, 1, 3]],
        [[10, 20, 30, 40, 60, 90, 100], [40, 20, 10, 30, 100]],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        root = Node.from_list(arr)
        result = s2.topView(root)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 14 of March 2026

    p1()

    p2()
