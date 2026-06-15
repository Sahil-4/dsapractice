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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # only one node
        if head is None or head.next is None:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            assert slow is not None
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow points to middle node
        assert prev is not None
        assert slow is not None
        prev.next = slow.next

        return head

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2095. Delete the Middle Node of a Linked List - https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=daily-question&envId=2026-06-15

    testcase = [
        [[1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6]],
        [[1, 2, 3, 4], [1, 2, 4]],
        [[2, 1], [2]],
    ]

    for line in testcase:
        [arr, expected] = line
        s1 = Solution1()
        head = ListNode.__from_list__(arr)
        result_list = s1.deleteMiddle(head)
        result = ListNode.__to_list__(result_list)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minimumCost(self, cost: List[int], w: int) -> int:
        INF = float("inf")

        dp = [INF] * (w + 1)
        dp[0] = 0

        for weight in range(1, w + 1):
            for i, c in enumerate(cost):
                packet_weight = i + 1

                if c == -1 or packet_weight > weight:
                    continue

                dp[weight] = min(dp[weight], dp[weight - packet_weight] + c)

        return int(dp[w] if dp[w] != INF else -1)

        # Complexity analysis
        # Time : O(N * W)
        # Space : O(W)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Cost to Fill Given Weight - https://www.geeksforgeeks.org/problems/minimum-cost-to-fill-given-weight-in-a-bag1956/1

    testcase = [
        [[20, 10, 4, 50, 100], 5, 14],
        [[-1, -1, 4, 3, -1], 5, -1],
    ]

    for line in testcase:
        [cost, w, expected] = line
        s2 = Solution2()
        result = s2.minimumCost(cost, w)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 15 of June 2026

    p1()

    p2()
