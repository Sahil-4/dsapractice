from collections import deque
from typing import List, Optional


class Fancy:

    MOD = 10**9 + 7

    def __init__(self):
        self.values = []
        self.increment = 0
        self.multiply = 1

    def power(self, a: int, b: int):
        if b == 0:
            return 1

        half = self.power(a, b // 2)
        result = (half * half) % self.MOD

        if b & 1:
            result = (result * a) % self.MOD

        return result

    def append(self, val: int) -> None:
        val = (
            ((val - self.increment) % self.MOD + self.MOD)
            * self.power(self.multiply, self.MOD - 2)
            % self.MOD
        )
        self.values.append(val)

    def addAll(self, inc: int) -> None:
        self.increment = (self.increment + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.multiply = (self.multiply * m) % self.MOD
        self.increment = (self.increment * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.values):
            return -1
        return (self.values[idx] * self.multiply + self.increment) % self.MOD


def p1():
    # Problem 1 : POTD Leetcode 1622. Fancy Sequence - https://leetcode.com/problems/fancy-sequence/description/?envType=daily-question&envId=2026-03-15

    testcase = [
        [
            [
                "Fancy",
                "append",
                "addAll",
                "append",
                "multAll",
                "getIndex",
                "addAll",
                "append",
                "multAll",
                "getIndex",
                "getIndex",
                "getIndex",
            ],
            [
                [],
                [2],
                [3],
                [7],
                [2],
                [0],
                [3],
                [10],
                [2],
                [0],
                [1],
                [2],
            ],
            [
                None,
                None,
                None,
                None,
                None,
                10,
                None,
                None,
                None,
                26,
                34,
                20,
            ],
        ]
    ]

    for line in testcase:
        [actions, inputs, expected] = line

        T = len(actions)

        obj = Fancy()
        result: List[Optional[int]] = [None]

        for i in range(1, T):
            action = actions[i]
            if action == "append":
                out = obj.append(inputs[i][0])
                result.append(out)
            elif action == "addAll":
                out = obj.addAll(inputs[i][0])
                result.append(out)
            elif action == "multAll":
                out = obj.multAll(inputs[i][0])
                result.append(out)
            elif action == "getIndex":
                out = obj.getIndex(inputs[i][0])
                result.append(out)

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
    def verticalOrder(self, root: Optional[Node]) -> List[List[int]]:
        # code here

        if not root:
            return []

        q = deque([(root, 0)])  # (node, horizontal_distance)
        hd_map = {}

        while q:
            node, hd = q.popleft()

            # store only the first node encountered at this HD
            if hd not in hd_map:
                hd_map[hd] = []

            hd_map[hd].append(node.data)

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
    # Problem 2 : POTD Geeksforgeeks Vertical Tree Traversal - https://www.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1

    testcase = [
        [
            [1, 2, 3, 4, 5, 6, 7, None, None, None, 8, None, 9, None, 10, 11, None],
            [[4], [2], [1, 5, 6, 11], [3, 8, 9], [7], [10]],
        ],
        [
            [1, 2, 3, 4, 5, None, 6],
            [[4], [2], [1, 5], [3], [6]],
        ],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        root = Node.from_list(arr)
        result = s2.verticalOrder(root)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 15 of March 2026

    p1()

    p2()
