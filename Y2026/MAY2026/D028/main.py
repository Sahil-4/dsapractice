from typing import List, Optional


class TrieNode:
    def __init__(self, index: int):
        self.index = index
        self.children = [None] * 26

    def insert(self, word: str, word_idx: int, wordsContainer: List[str]) -> None:
        node = self
        n = len(word)

        for i in range(n - 1, -1, -1):
            ch_idx = ord(word[i]) - ord("a")

            if node.children[ch_idx] is None:
                node.children[ch_idx] = TrieNode(word_idx)

            node = node.children[ch_idx]

            if len(wordsContainer[node.index]) > n:
                node.index = word_idx

    def search(self, word: str) -> int:
        node = self
        result_idx = node.index

        for i in range(len(word) - 1, -1, -1):
            ch_idx = ord(word[i]) - ord("a")

            node = node.children[ch_idx]

            if node is None:
                return result_idx

            result_idx = node.index

        return result_idx


class Solution1:
    def stringIndices(
        self, wordsContainer: List[str], wordsQuery: List[str]
    ) -> List[int]:
        root = TrieNode(0)

        for i, word in enumerate(wordsContainer):

            if len(wordsContainer[root.index]) > len(word):
                root.index = i

            root.insert(word, i, wordsContainer)

        result = []

        for word in wordsQuery:
            result.append(root.search(word))

        return result

        # Complexity analysis
        # Time : O(N * L + M * K)
        # Space : O(N * L)


def p1():
    # Problem 1 : POTD Leetcode 3093. Longest Common Suffix Queries - https://leetcode.com/problems/longest-common-suffix-queries/description/?envType=daily-question&envId=2026-05-28

    testcase = [
        [["abcd", "bcd", "xbcd"], ["cd", "bcd", "xyz"], [1, 1, 1]],
        [["abcdefgh", "poiuygh", "ghghgh"], ["gh", "acbfgh", "acbfegh"], [2, 0, 2]],
    ]

    for line in testcase:
        [wordsContainer, wordsQuery, expected] = line
        s1 = Solution1()
        result = s1.stringIndices(wordsContainer, wordsQuery)
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
    def map_index(self, node, index, index_mapping):
        if node is None:
            return

        if index not in index_mapping:
            index_mapping[index] = []

        index_mapping[index].append(node.data)

        self.map_index(node.left, index - 1, index_mapping)
        self.map_index(node.right, index + 1, index_mapping)

    def verticalSum(self, root):
        # code here
        # -1: [], 0: [], 1: [], ...
        index_mapping = {}

        self.map_index(root, 0, index_mapping)

        vsum = []

        min_index = min(index_mapping.keys())
        max_index = max(index_mapping.keys())

        for i in range(min_index, max_index + 1):
            vsum.append(sum(index_mapping[i]))

        return vsum

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Vertical Sum - https://www.geeksforgeeks.org/problems/vertical-sum/1

    testcase = [
        [[1, 2, 3, 4, 5, 6, 7], [4, 2, 12, 3, 7]],
        [[1, 2, None, 3, None, 4, None, 6, None, 7, None], [7, 6, 4, 3, 2, 1]],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        root = Node.build(arr)
        result = s2.verticalSum(root)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 28 of May 2026

    p1()

    p2()
