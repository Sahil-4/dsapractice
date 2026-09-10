from collections import deque
from typing import Any, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_list(arr: list[Optional[int]]) -> Optional["TreeNode"]:
        if not arr or arr[0] is None:
            return None

        root = TreeNode(arr[0])
        q: deque[TreeNode] = deque([root])

        i = 1
        while q and i < len(arr):
            node = q.popleft()

            val = arr[i]
            if i < len(arr) and val is not None:
                node.left = TreeNode(val)
                q.append(node.left)
            i += 1

            val = arr[i]
            if i < len(arr) and val is not None:
                node.right = TreeNode(val)
                q.append(node.right)
            i += 1

        return root

    def to_list(self) -> list[Any]:
        result = []
        q: deque[Optional[TreeNode]] = deque([self])

        while q:
            node = q.popleft()

            if node:
                result.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                result.append(None)

        # remove trailing None values
        while result and result[-1] is None:
            result.pop()

        return result


class Solution1:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def helper(node: Optional[TreeNode]) -> tuple[int, int, int]:
            if not node:
                # avg_eq_nodes_count, nodes_count, nodes_sum
                return 0, 0, 0

            l_avg_eq_nodes_count, l_nodes_count, l_nodes_sum = helper(node.left)
            r_avg_eq_nodes_count, r_nodes_count, r_nodes_sum = helper(node.right)

            _avg_eq_nodes_count = l_avg_eq_nodes_count + r_avg_eq_nodes_count
            _nodes_count = l_nodes_count + r_nodes_count + 1
            _nodes_sum = l_nodes_sum + r_nodes_sum + node.val

            if node.val == _nodes_sum // _nodes_count:
                _avg_eq_nodes_count += 1

            return _avg_eq_nodes_count, _nodes_count, _nodes_sum

        avg_eq_nodes_count, _, __ = helper(root)

        return avg_eq_nodes_count

        # Complexity analysis
        # Time : O(N)
        # Space : O(H)


def p1():
    # Problem 1 : POTD Leetcode 2265. Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/?envType=daily-question&envId=2026-09-10

    testcase = [
        [
            TreeNode.from_list([4, 8, 5, 0, 1, None, 6]),
            5,
        ],
        [
            TreeNode.from_list([1]),
            1,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.averageOfSubtree(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def pairCount(self, x: int, y: int) -> int:
        """code here"""

        # gcd(a,b) = x
        # therefore:
        #     a = x*m
        #     b = x*n
        # since gcd(a,b) = x:
        #     gcd(m,n) = 1
        # since lcm(a,b) = y:
        #     x*m*n = y
        # therefore:
        #     m*n = y/x
        # if y % x != 0:
        #     no solution
        # factor k = y/x
        # every distinct prime factor of k must go entirely
        # into either m or n.
        # if k has r distinct prime factors:
        #     answer = 2^r (pairs)

        # GCD must divide LCM
        if y % x != 0:
            return 0

        k = y // x

        # count distinct prime factors of k
        r = 0
        p = 2

        while p * p <= k:
            if k % p == 0:
                r += 1

                # remove all copies of this prime
                while k % p == 0:
                    k //= p

            p += 1

        # if something > 1 remains,
        # it is a prime factor
        if k > 1:
            r += 1

        return 2**r

        # Complexity analysis
        # Time : O(sqrt(K))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Pairs with Given GCD and LCM - https://www.geeksforgeeks.org/problems/possible-pairs1550/1

    testcase = [
        [2, 12, 4],
        [6, 4, 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.pairCount(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def __to_list__(cls, head):
        return [head.val] + cls.__to_list__(head.next) if head else []

    @classmethod
    def __from_list__(cls, arr):
        if not arr:
            return None

        head = ListNode(arr[0])
        curr = head
        for x in arr[1:]:
            curr.next = ListNode(x)
            curr = curr.next
        return head

    def __eq__(self, other) -> bool:
        if not isinstance(other, ListNode):
            return False

        temp1 = self
        temp2 = other

        while temp1 or temp2:
            if not temp1 or not temp2:
                return False

            if temp1.val != temp2.val:
                return False

            temp1 = temp1.next
            temp2 = temp2.next

        return True

    def __lt__(self, other):
        return self.val < other.val

    def __repr__(self) -> str:
        return str(ListNode.__to_list__(self))

    def reverse(self):
        if not self:
            return self

        prev = None
        curr = self

        while curr:
            _next = curr.next

            curr.next = prev
            prev = curr

            curr = _next

        self = prev

        return self


class Solution3:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # kth node in the current group
            kth = group_prev

            for _ in range(k):
                kth = kth.next

                # fewer than k nodes remain
                if kth is None:
                    return dummy.next

            # first node of the group
            group_start = group_prev.next

            # node immediately after the group
            group_next = kth.next

            # reverse the group
            prev = group_next
            curr = group_start

            while curr != group_next:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            # `prev` is now the new head of the reversed group.
            group_prev.next = prev

            # `group_start` became the tail after reversal.
            group_prev = group_start

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 25. Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            ListNode.__from_list__([1, 2, 3, 4, 5]),
            2,
            ListNode.__from_list__([2, 1, 4, 3, 5]),
        ],
        [
            ListNode.__from_list__([1, 2, 3, 4, 5]),
            3,
            ListNode.__from_list__([3, 2, 1, 4, 5]),
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.reverseKGroup(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 10 of September 2026

    p1()

    p2()

    p3()
