from collections import deque
from typing import Any, List, Optional, cast


class Solution1:
    def maxK(self, nums: list[int]) -> int:
        # every misplaced element has to take part in at least one swap,
        # k has to be a sub-mask of each misplaced element, hence k <= AND of all of them;
        # and that AND itself is always achievable
        result = -1

        for i, num in enumerate(nums):
            if num != i:
                result = num if result == -1 else result & num

        # already sorted
        return 0 if result == -1 else result

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3644. Maximum K to Sort a Permutation - https://leetcode.com/problems/maximum-k-to-sort-a-permutation/description/?envType=daily-question&envId=2026-10-23

    testcase = [
        [[0, 3, 2, 1], 1],
        [[0, 1, 3, 2], 2],
        [[3, 2, 1, 0], 0],
        [[0, 1, 2], 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maxK(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


# Binary Tree Node Structure
class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @staticmethod
    def from_list(arr: List[Optional[int]]) -> Optional["Node"]:
        if not arr or arr[0] is None:
            return None

        root = Node(arr[0])
        q: deque[Node] = deque([root])

        i = 1
        while q and i < len(arr):
            node = q.popleft()

            val = arr[i]
            if val is not None:
                node.left = Node(val)
                q.append(node.left)
            i += 1

            val = arr[i]
            if val is not None:
                node.right = Node(val)
                q.append(node.right)
            i += 1

        return root

    def to_list(self) -> List[Any]:
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
    def pairsViolatingBST(self, root):
        # code here

        # in-order traversal of a valid BST is increasing;
        # every pair of nodes (x before y in in-order) with x > y violates a BST property:
        # either ancestor / descendant, or left subtree vs right subtree of a common node.
        # equal values are not counted as violations (judge expects 1 for [4, 1, N, 4])
        # iterative traversal, the tree can be a chain of 5 * 10^4 nodes
        inorder = []
        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            inorder.append(current.data)
            current = current.right

        # count pairs (i < j) with inorder[i] > inorder[j] using a fenwick tree over ranks
        ranks = {value: r for r, value in enumerate(sorted(set(inorder)), 1)}
        M = len(ranks)
        tree = [0] * (M + 1)

        count = 0
        for seen, value in enumerate(inorder):
            rank = ranks[value]

            # elements seen so far that are smaller than or equal to value
            not_greater = 0
            i = rank
            while i > 0:
                not_greater += tree[i]
                i -= i & -i

            count += seen - not_greater

            i = rank
            while i <= M:
                tree[i] += 1
                i += i & -i

        return count

        # Complexity analysis
        # Time : O(N log N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count Pairs Violating BST Property - https://www.geeksforgeeks.org/problems/pairs-violating-bst-property--212515/1

    testcase = [
        [Node.from_list([10, 50, 40, None, None, 20, 30]), 5],
        [Node.from_list([80, 40, 30, 70, None, 60, 70]), 8],
        [Node.from_list([4, 1, None, 4]), 1],
        [Node.from_list([2, 1, 3]), 0],
        [Node.from_list([5]), 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.pairsViolatingBST(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


# Definition for a Node with a random pointer.
class RandomListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

    @staticmethod
    def from_list(arr: List[List[Optional[int]]]) -> Optional["RandomListNode"]:
        # arr[i] = [val, random_index]
        if not arr:
            return None

        nodes = [RandomListNode(cast(int, val)) for val, _ in arr]

        for i, (_, random_index) in enumerate(arr):
            if i + 1 < len(nodes):
                nodes[i].next = nodes[i + 1]

            if random_index is not None:
                nodes[i].random = nodes[random_index]

        return nodes[0]

    @staticmethod
    def to_list(head: Optional["RandomListNode"]) -> List[List[Optional[int]]]:
        index_of = {}
        node = head
        while node:
            index_of[node] = len(index_of)
            node = node.next

        result = []
        node = head
        while node:
            result.append([node.val, index_of[node.random] if node.random else None])
            node = node.next

        return result

    @staticmethod
    def collect(head: Optional["RandomListNode"]) -> set["RandomListNode"]:
        nodes = set()
        node = head
        while node:
            nodes.add(node)
            node = node.next

        return nodes


class Solution3:
    def copyRandomList(
        self, head: Optional[RandomListNode]
    ) -> Optional[RandomListNode]:
        # original node -> its copy
        copies: dict[Optional[RandomListNode], Optional[RandomListNode]] = {None: None}

        node = head
        while node:
            copies[node] = RandomListNode(node.val)
            node = node.next

        node = head
        while node:
            copy = copies[node]
            if copy is not None:
                copy.next = copies[node.next]
                copy.random = copies[node.random]

            node = node.next

        return copies[head]

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 138. Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            RandomListNode.from_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]),
            [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        ],
        [RandomListNode.from_list([[1, 1], [2, 1]]), [[1, 1], [2, 1]]],
        [
            RandomListNode.from_list([[3, None], [3, 0], [3, None]]),
            [[3, None], [3, 0], [3, None]],
        ],
        [RandomListNode.from_list([]), []],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.copyRandomList(*inputs)
        assert (
            RandomListNode.to_list(result) == expected
        ), f"Test failed: expected {expected}, got {RandomListNode.to_list(result)}"
        # a deep copy must not share any node with the original list
        assert not (
            RandomListNode.collect(result) & RandomListNode.collect(*inputs)
        ), "Test failed: shared nodes"
        print(f"Testcase passed (P3): result={RandomListNode.to_list(result)}")


if __name__ == "__main__":
    # Day 23 of October 2026

    p1()

    p2()

    p3()
