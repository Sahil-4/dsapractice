from typing import List, Optional


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
        head = ListNode(arr[0])
        curr = head
        for x in arr[1:]:
            curr.next = ListNode(x)
            curr = curr.next
        return head


class Solution1:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # find middle
        slow = head
        fast = head

        while fast and fast.next:
            assert slow is not None
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # compute maximum twin sum
        max_twin_sum = 0

        start1 = head
        start2 = prev

        while start2:
            assert start1 is not None
            max_twin_sum = max(max_twin_sum, start1.val + start2.val)
            start1 = start1.next
            start2 = start2.next

        return max_twin_sum

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2130. Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/?envType=daily-question&envId=2026-06-14

    testcase = [
        [[5, 4, 2, 1], 6],
        [[4, 2, 2, 3], 7],
        [[1, 100000], 100001],
    ]

    for line in testcase:
        [arr, expected] = line
        s1 = Solution1()
        head = ListNode.__from_list__(arr)
        result = s1.pairSum(head)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def exitPoint(self, mat: List[List[int]]) -> List[int]:
        # code here
        N = len(mat)
        M = len(mat[0])

        def within_boundary(i: int, j: int) -> bool:
            check = True
            check = check and i >= 0 and i < N
            check = check and j >= 0 and j < M
            return check

        D = 0  # 0 = right, 90 = down, 180 = left, 270 = up

        i = 0
        j = 0

        while True:
            # change direction
            if mat[i][j] == 1:
                mat[i][j] = 0
                D = (D + 90) % 360

            # advance
            ni = i
            nj = j
            if D == 0:
                nj = j + 1
            elif D == 90:
                ni = i + 1
            elif D == 180:
                nj = j - 1
            else:
                ni = i - 1

            if not within_boundary(ni, nj):
                break

            i = ni
            j = nj

        return [i, j]

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(N * M)


def p2():
    # Problem 2 : POTD Geeksforgeeks Exit Point in a Matrix - https://www.geeksforgeeks.org/problems/exit-point-in-a-matrix0905/1

    testcase = [
        [[[0, 1, 0], [0, 1, 1], [0, 0, 0]], [1, 0]],
        [[[0, 0]], [0, 1]],
        [
            [
                [0, 0, 0, 0, 0, 0, 1, 0, 1],
                [0, 1, 1, 1, 1, 1, 0, 0, 1],
                [1, 1, 1, 1, 0, 0, 0, 1, 1],
                [0, 0, 0, 1, 1, 0, 1, 0, 1],
                [0, 1, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 1, 0, 1],
                [0, 0, 0, 0, 1, 1, 0, 1, 0],
                [1, 1, 0, 0, 0, 1, 1, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 1, 1],
                [0, 0, 0, 1, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 1, 1, 1, 1, 0],
                [1, 1, 0, 0, 0, 1, 0, 1, 1],
                [1, 0, 0, 1, 1, 0, 1, 0, 0],
                [1, 1, 0, 0, 0, 1, 1, 0, 0],
                [1, 0, 0, 1, 0, 0, 0, 1, 1],
                [0, 1, 1, 0, 0, 1, 1, 1, 1],
                [1, 0, 0, 0, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 1, 0, 1],
            ],
            [0, 4],
        ],
    ]

    for line in testcase:
        [mat, expected] = line
        s2 = Solution2()
        result = s2.exitPoint(mat)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 14 of June 2026

    p1()

    p2()
