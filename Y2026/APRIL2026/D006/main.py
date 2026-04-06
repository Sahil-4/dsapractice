import heapq
from typing import List, Optional


class Solution1:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles_set = set(map(tuple, obstacles))

        max_dist = 0

        origin_x = 0
        origin_y = 0

        curr_dir_x = 0
        curr_dir_y = 1

        for command in commands:
            if command == -2:
                # 90 degrees left
                curr_dir_x, curr_dir_y = -curr_dir_y, curr_dir_x
            elif command == -1:
                # 90 degrees right
                curr_dir_x, curr_dir_y = curr_dir_y, -curr_dir_x
            else:
                # movement
                for _ in range(command):
                    new_x = origin_x + curr_dir_x
                    new_y = origin_y + curr_dir_y

                    if (new_x, new_y) in obstacles_set:
                        break

                    origin_x = new_x
                    origin_y = new_y

            max_dist = max(max_dist, origin_x * origin_x + origin_y * origin_y)

        return max_dist

        # Complexity analysis
        # Time : O(N + M * C)
        # Space : O(M)


def p1():
    # Problem 1 : POTD Leetcode 874. Walking Robot Simulation - https://leetcode.com/problems/walking-robot-simulation/?envType=daily-question&envId=2026-04-06

    testcase = [
        [[4, -1, 3], [], 25],
        [[4, -1, 4, -2, 4], [[2, 4]], 65],
        [[6, -1, -1, 6], [[0, 0]], 36],
    ]

    for line in testcase:
        [commands, obstacles, expected] = line
        s1 = Solution1()
        result = s1.robotSim(commands, obstacles)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Node:
    """
    Huffman Tree Node
    """

    def __init__(
        self,
        data: int,
        index: int,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
    ):
        # frequency
        self.data = data

        # smallest original index in subtree
        self.index = index

        self.left = left
        self.right = right


class Solution2:
    def preOrder(self, root: Optional[Node], ans: List[str], curr: str) -> None:
        """
        Traverse the Huffman tree in preorder and collect codes
        """
        if root is None:
            return

        # Leaf node → represents a character
        if root.left is None and root.right is None:
            # Edge case: only one character
            ans.append(curr if curr else "0")
            return

        self.preOrder(root.left, ans, curr + "0")
        self.preOrder(root.right, ans, curr + "1")

    def huffmanCodes(self, s: str, f: List[int]) -> List[str]:
        """
        Generate Huffman Codes for given characters and frequencies
        """
        n = len(s)

        # min heap: (frequency, index, Node)
        pq: List[tuple[int, int, Node]] = []

        for i in range(n):
            node = Node(f[i], i)
            heapq.heappush(pq, (node.data, node.index, node))

        # edge case: single character
        if n == 1:
            return ["0"]

        # Huffman tree build
        while len(pq) >= 2:
            f1, i1, left = heapq.heappop(pq)
            f2, i2, right = heapq.heappop(pq)

            merged = Node(
                data=left.data + right.data,
                index=min(left.index, right.index),
                left=left,
                right=right,
            )

            heapq.heappush(pq, (merged.data, merged.index, merged))

        root = pq[0][2]

        result: List[str] = []
        self.preOrder(root, result, "")

        return result

        # Complexity analysis
        # Time : O(N * log(N))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Huffman Encoding - https://www.geeksforgeeks.org/problems/huffman-encoding3345/1

    testcase = [
        ["abcdef", [5, 9, 12, 13, 16, 45], [0, 100, 101, 1100, 1101, 111]],
    ]

    for line in testcase:
        [s, f, expected] = line
        s2 = Solution2()
        result = s2.huffmanCodes(s, f)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 6 of April 2026

    p1()

    p2()
