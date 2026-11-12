from collections import deque
from typing import Any, Optional


class Solution1:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        if not nums:
            return 0

        max_len = 1
        inc = 1
        dec = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
            max_len = max(max_len, inc, dec)

        return max_len

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3105. Longest Strictly Increasing or Strictly Decreasing Subarray - https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/?envType=daily-question&envId=2026-11-12

    testcase = [
        [[1, 4, 3, 3, 2], 2],
        [[3, 3, 3, 3], 1],
        [[3, 2, 1], 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.longestMonotonicSubarray(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


# Structure of a Binary Search Tree node
class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @staticmethod
    def from_list(arr: list[Optional[int]]) -> Optional["Node"]:
        if not arr or arr[0] is None:
            return None

        root = Node(arr[0])
        q: deque[Node] = deque([root])

        i = 1
        while q and i < len(arr):
            node = q.popleft()

            if i < len(arr):
                data = arr[i]
                if data is not None:
                    node.left = Node(data)
                    q.append(node.left)
                i += 1

            if i < len(arr):
                data = arr[i]
                if data is not None:
                    node.right = Node(data)
                    q.append(node.right)
                i += 1

        return root

    def to_list(self) -> list[Any]:
        result = []
        q: deque[Optional[Node]] = deque([self])

        while q:
            node = q.popleft()

            if node:
                result.append(node.data)
                q.append(node.left)
                q.append(node.right)
            else:
                result.append(None)

        # remove trailing None values
        while result and result[-1] is None:
            result.pop()

        return result


class Solution2:
    def minDiff(self, root: "Node", k: int) -> int:
        # code here

        min_diff = float("inf")
        curr = root

        while curr:
            min_diff = min(min_diff, abs(curr.data - k))
            if k < curr.data:
                curr = curr.left
            elif k > curr.data:
                curr = curr.right
            else:
                return 0

        return int(min_diff)

        # Complexity analysis
        # Time : O(1)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Closest in BST - https://www.geeksforgeeks.org/problems/find-the-closest-element-in-bst/1

    testcase = [
        [
            Node.from_list([10, 2, 11, 1, 5, None, None, None, None, 3, 6, None, 4]),
            13,
            2,
        ],
        [
            Node.from_list([8, 1, 9, None, 4, None, 10, 3]),
            9,
            0,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minDiff(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Trie:
    def __init__(self):
        # every node is a dict : character -> child node, "$" marks the end of a word
        self.root: dict = {}

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]

        node["$"] = True

    def search(self, word: str) -> bool:
        node = self._find(word)

        return node is not None and "$" in node

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, text: str):
        node = self.root

        for ch in text:
            if ch not in node:
                return None
            node = node[ch]

        return node

    # Complexity analysis
    # Time : O(L)
    # Space : O(C)


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.word: Optional[str] = None


class Solution3:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()

        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w

        rows, cols = len(board), len(board[0])
        res: list[str] = []

        def dfs(r: int, c: int, parent: TrieNode) -> None:
            ch = board[r][c]
            curr_node = parent.children[ch]

            if curr_node.word is not None:
                res.append(curr_node.word)
                curr_node.word = None

            board[r][c] = "#"  # Mark visited
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and board[nr][nc] in curr_node.children
                ):
                    dfs(nr, nc, curr_node)
            board[r][c] = ch

            if not curr_node.children:
                parent.children.pop(ch)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return res

        # Complexity analysis
        # Time : O(M * N * 3^L)
        # Space : O(C + L)


def p3():
    # Problem 3 : NC150 Leetcode 212. Word Search II - https://leetcode.com/problems/word-search-ii/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
            ["oath", "eat"],
        ],
        [
            [
                ["a", "b"],
                ["c", "d"],
            ],
            ["abcb"],
            [],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.findWords(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 12 of November 2026

    p1()

    p2()

    p3()
