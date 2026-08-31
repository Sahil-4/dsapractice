from functools import lru_cache
from typing import Optional


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
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        # Need at least 3 nodes for a critical point
        if head is None or head.next is None or head.next.next is None:
            return [-1, -1]

        prev = head
        curr = head.next
        index = 1

        first_critical = -1
        prev_critical = -1
        min_distance = float("inf")
        max_distance = -1

        while curr.next:
            next_node = curr.next

            # Check if curr is a local maximum or minimum
            is_critical = (curr.val > prev.val and curr.val > next_node.val) or (
                curr.val < prev.val and curr.val < next_node.val
            )

            if is_critical:
                if first_critical == -1:
                    # First critical point
                    first_critical = index
                else:
                    # Distance from previous critical point
                    min_distance = min(min_distance, index - prev_critical)

                    # Distance from first critical point
                    max_distance = max(max_distance, index - first_critical)

                prev_critical = index

            prev = curr
            curr = next_node
            index += 1

        if first_critical == -1 or min_distance == float("inf"):
            return [-1, -1]

        return [int(min_distance), max_distance]

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points - https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/?envType=daily-question&envId=2026-08-31

    testcase = [
        [ListNode.__from_list__([3, 1]), [-1, -1]],
        [ListNode.__from_list__([5, 3, 1, 2, 5, 1, 2]), [1, 3]],
        [ListNode.__from_list__([1, 3, 2, 2, 3, 2, 2, 2, 7]), [3, 3]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.nodesBetweenCriticalPoints(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minCost(self, n: int, i: int, d: int, c: int) -> int:

        @lru_cache(None)
        def solve(x):
            if x == 0:
                return 0

            if x == 1:
                return i

            # worst/simple case: insert all characters
            ans = x * i

            if x % 2 == 0:
                # option 1: build x/2 and copy-paste
                ans = min(ans, solve(x // 2) + c)

            else:
                # option 2: build x-1 and insert
                ans = min(ans, solve(x - 1) + i)

                # option 3: build x+1, then delete
                ans = min(ans, solve(x + 1) + d)

            return ans

        return solve(n)

        # Complexity:
        # Time: O(Log(N))
        # Space: O(Log(N))


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Cost for n Characters - https://www.geeksforgeeks.org/problems/minimum-time1238/1

    testcase = [
        [9, 1, 2, 1, 5],
        [9, 10, 1, 1, 17],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minCost(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 31 of August 2026

    p1()

    p2()
