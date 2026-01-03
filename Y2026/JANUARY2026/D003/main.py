class Solution1:
    def numOfWays(self, n: int) -> int:
        # number of ways = DP (or recursion)
        # each cell depends on left + top = need DP
        # if n == 1
        # total = 12
        # patterns:
        # 2-color pattern (ABA) = 6
        # 3-color pattern (ABC) = 6
        # IDEA:
        # treat each row as a pattern, not individual cells
        # define DP states:
        # A -> ways where current row is ABA pattern (2-color)
        # B -> ways where current row is ABC pattern (3-color)
        # base case (n = 1):
        # A = 6, B = 6
        # for n >= 2
        # next row depends only on upper row
        # vertical colors must be different
        # transitions:
        # newA = A*3 + B*2
        # newB = A*2 + B*2
        # repeat for all rows
        # final answer = A + B

        MOD = int((10**9) + 7)

        A, B = 6, 6

        for n in range(2, n + 1):
            newA = (A * 3 + B * 2) % MOD
            newB = (A * 2 + B * 2) % MOD
            A, B = newA, newB

        return (A + B) % MOD

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1411. Number of Ways to Paint N × 3 Grid - https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description/?envType=daily-question&envId=2026-01-03

    testcase = [
        [1, 12],
        [3, 246],
        [5, 5118],
        [21, 932697716],
        [5000, 30228214],
    ]

    for line in testcase:
        [n, expected] = line
        s1 = Solution1()
        result = s1.numOfWays(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None

    @classmethod
    def from_nested_list(cls, arr):
        """
        arr example:
        [
            [5, 7, 8],
            [10, 20],
            [19, 22, 50],
            [28, 35, 40, 45]
        ]
        """
        if not arr:
            return None

        head = Node(arr[0][0])
        curr = head

        # build first bottom list
        for x in arr[0][1:]:
            curr.bottom = Node(x)
            curr = curr.bottom

        prev_head = head

        # build remaining heads
        for sub in arr[1:]:
            head_node = Node(sub[0])
            prev_head.next = head_node
            prev_head = head_node

            curr = head_node
            for x in sub[1:]:
                curr.bottom = Node(x)
                curr = curr.bottom

        return head

    @staticmethod
    def bottom_to_list(head):
        res = []
        while head:
            res.append(head.data)
            head = head.bottom
        return res


class Solution2:
    def merge(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.data <= list2.data:
            list1.bottom = self.merge(list1.bottom, list2)
            return list1
        else:
            list2.bottom = self.merge(list1, list2.bottom)
            return list2

    def flatten(self, root):
        # code here
        # IDEA: merge sorted linked lists
        # each bottom sublist is already sorted
        # no need to sort all nodes again
        # flatten from right to left
        # given: L1 → L2 → L3 → L4 (each Li is sorted via bottom)
        # first flatten L2 → L3 → L4
        # then merge L1 with flattened list
        # merge of two sorted lists takes O(M1 + M2)
        # repeat merging for all N head nodes
        # final call: return merge(root, flatten(root.next))

        if root is None or root.next is None:
            return root

        root.next = self.flatten(root.next)
        return self.merge(root, root.next)

        # Complexity analysis
        # Time : O(N*M)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Flattening a Linked ListFlattening a Linked List - https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1

    testcase = [
        (
            [[5, 7, 8], [10, 20], [19, 22, 50], [28, 35, 40, 45]],
            [5, 7, 8, 10, 19, 20, 22, 28, 35, 40, 45, 50],
        ),
        (
            [[5, 7, 8, 30], [10, 20], [19, 22], [28, 50]],
            [5, 7, 8, 10, 19, 20, 22, 28, 30, 50],
        ),
        ([[1, 2, 3]], [1, 2, 3]),
    ]

    for line in testcase:
        [arr, expected] = line

        root = Node.from_nested_list(arr)
        s2 = Solution2()
        result = s2.flatten(root)
        result_list = Node.bottom_to_list(result)

        assert (
            result_list == expected
        ), f"Test failed: expected {expected}, got {result_list}"
        print(f"Testcase passed (P2): result={result_list}")


if __name__ == "__main__":
    # Day 3 of January 2026

    p1()

    p2()
