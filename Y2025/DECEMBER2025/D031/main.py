from typing import List


class Solution1:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        self.ROW = row
        self.COL = col
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(grid, i, j):
            if i < 0 or i >= self.ROW or j < 0 or j >= self.COL or grid[i][j] == 1:
                return False

            if i == self.ROW - 1:
                return True

            grid[i][j] = 1  # mark visited

            for di, dj in self.directions:
                if dfs(grid, i + di, j + dj):
                    return True

            return False

        def canCross(day):
            grid = [[0] * self.COL for _ in range(self.ROW)]

            for i in range(day + 1):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1

            for j in range(self.COL):
                if grid[0][j] == 0 and dfs(grid, 0, j):
                    return True

            return False

        # Binary Search
        left, right = 0, len(cells) - 1
        last_day = 0

        while left <= right:
            mid = left + (right - left) // 2

            if canCross(mid):
                last_day = mid + 1
                left = mid + 1
            else:
                right = mid - 1

        return last_day

        # Complexity analysis
        # Time: O(Log(R*C) * R*C)
        # Space: O(R*C)


def p1():
    # Problem 1 : POTD Leetcode 1970. Last Day Where You Can Still Cross - https://leetcode.com/problems/last-day-where-you-can-still-cross/description/?envType=daily-question&envId=2025-12-31

    testcase = [
        [
            2,
            2,
            [[1, 1], [2, 1], [1, 2], [2, 2]],
            2,
        ],
        [
            2,
            2,
            [[1, 1], [1, 2], [2, 1], [2, 2]],
            1,
        ],
        [
            3,
            3,
            [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]],
            3,
        ],
    ]

    for line in testcase:
        [row, col, cells, expected] = line
        s1 = Solution1()
        result = s1.latestDayToCross(row, col, cells)
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
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        # find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # compare both halves
        left = head
        right = prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next

        return True

        # Complexity analysis
        # Time: O(N)
        # Space: O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Palindrome Linked List - https://www.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1

    testcase = [
        [[1, 2, 1, 1, 2, 1], True],
        [[1, 2, 3], False],
    ]

    for line in testcase:
        [arr, expected] = line
        head = Node.build_ll(arr)
        s2 = Solution2()
        result = s2.isPalindrome(head)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 31 of December 2025

    p1()

    p2()
