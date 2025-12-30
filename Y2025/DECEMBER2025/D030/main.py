from typing import List


class Solution1:
    def isMagicGrid(self, grid, r, c) -> bool:
        # check uniqueness
        st = set()
        for i in range(3):
            for j in range(3):
                num = grid[r + i][c + j]
                if num < 1 or num > 9 or num in st:
                    return False
                st.add(num)

        # check sum - row & col
        SUM = grid[r][c] + grid[r][c + 1] + grid[r][c + 2]
        for i in range(3):
            if grid[r + i][c + 0] + grid[r + i][c + 1] + grid[r + i][c + 2] != SUM:
                return False
            if grid[r + 0][c + i] + grid[r + 1][c + i] + grid[r + 2][c + i] != SUM:
                return False

        # check sum - diagonals
        if grid[r + 0][c + 0] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != SUM:
            return False
        if grid[r + 0][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c + 0] != SUM:
            return False

        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        magic_squares_count = 0

        for i in range(ROWS - 2):
            for j in range(COLS - 2):
                if self.isMagicGrid(grid, i, j):
                    magic_squares_count += 1

        return magic_squares_count

        # Complexity analysis
        # Time : O(N*M)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 840. Magic Squares In Grid - https://leetcode.com/problems/magic-squares-in-grid/?envType=daily-question&envId=2025-12-30

    testcase = [
        [[[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]], 1],
        [[[8]], 0],
    ]

    for line in testcase:
        [grid, expected] = line
        s1 = Solution1()
        result = s1.numMagicSquaresInside(grid)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    @classmethod
    def build_ll(cls, arr):
        head = Node(arr[0])
        curr = head
        for x in arr[1:]:
            curr.next = Node(x)
            curr = curr.next
        return head

    @classmethod
    def ll_to_list(cls, head):
        res = []
        while head:
            res.append(head.data)
            head = head.next
        return res


class Solution2:
    def trim(self, head):
        while head and head.data == 0:
            head = head.next
        return head

    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def addTwoLists(self, head1, head2):
        # trim lists - remove leading zeroes
        head1 = self.trim(head1)
        head2 = self.trim(head2)

        # reverse both lists
        head1 = self.reverse(head1)
        head2 = self.reverse(head2)

        carry = 0
        dummy = Node(0)
        curr = dummy

        p1, p2 = head1, head2

        while p1 or p2 or carry:
            s = carry
            if p1:
                s += p1.data
                p1 = p1.next
            if p2:
                s += p2.data
                p2 = p2.next

            carry = s // 10
            curr.next = Node(s % 10)
            curr = curr.next

        # reverse result list
        return self.reverse(dummy.next)

        # Complexity analysis
        # Time : O(max(head1, head2))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Add Number Linked Lists - https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1

    testcase = [
        ([4, 5], [3, 4], [7, 9]),
        ([9, 9], [1], [1, 0, 0]),
        ([1, 2, 3], [9, 9], [2, 2, 2]),
        ([9, 9, 9], [1], [1, 0, 0, 0]),
        ([0, 0, 1, 2], [0, 3], [1, 5]),
        ([5], [5], [1, 0]),
    ]

    for t in testcase:
        head1 = Node.build_ll(t[0])
        head2 = Node.build_ll(t[1])
        expected = t[2]

        s2 = Solution2()
        result = s2.addTwoLists(head1, head2)
        result_list = Node.ll_to_list(result)

        assert (
            result_list == expected
        ), f"Test failed: expected {expected}, got {result_list}"
        print(f"Testcase passed (P2): result={result_list}")


if __name__ == "__main__":
    # Day 30 of December 2025

    p1()

    p2()
