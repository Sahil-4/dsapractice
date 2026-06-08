from typing import List


class Solution1:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        N = len(nums)
        output = [-1] * N

        lt_count = sum(1 for x in nums if x < pivot)
        eq_count = sum(1 for x in nums if x == pivot)

        lt_idx = 0
        eq_idx = lt_count
        gt_idx = lt_count + eq_count

        for x in nums:
            if x < pivot:
                output[lt_idx] = x
                lt_idx += 1
            elif x == pivot:
                output[eq_idx] = x
                eq_idx += 1
            else:
                output[gt_idx] = x
                gt_idx += 1

        return output

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2161. Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/?envType=daily-question&envId=2026-06-08

    testcase = [
        [[9, 12, 5, 10, 14, 3, 10], 10, [9, 5, 3, 10, 10, 12, 14]],
        [[-3, 4, 3, 2], 2, [-3, 2, 4, 3]],
    ]

    for line in testcase:
        [nums, pivot, expected] = line
        s1 = Solution1()
        result = s1.pivotArray(nums, pivot)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


# Structure of linked list node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

    @staticmethod
    def from_list(arr):
        if not arr:
            return None

        head = Node(arr[0])
        cur = head

        for x in arr[1:]:
            cur.next = Node(x)
            cur = cur.next

        return head

    @staticmethod
    def to_list(head):
        result = []

        while head:
            result.append(head.data)
            head = head.next

        return result


class Solution2:
    def compute(self, head):
        # code here

        def reverse(node):
            prev, curr = None, node
            while curr:
                curr.next, prev, curr = prev, curr, curr.next

            return prev

        head = reverse(head)

        max_seen = head.data
        curr = head
        while curr.next:
            if curr.next.data >= max_seen:
                max_seen = curr.next.data
                curr = curr.next
            else:
                curr.next = curr.next.next

        head = reverse(head)
        return head

        # Complexity Analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Delete Nodes with Greater on Right - https://www.geeksforgeeks.org/problems/delete-nodes-having-greater-value-on-right/1

    testcase = [
        ([12, 15, 10, 11, 5, 6, 2, 3], [15, 11, 6, 3]),
        ([10, 20, 30, 40, 50, 60], [60]),
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        head = Node.from_list(arr)
        result = Node.to_list(s2.compute(head))
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 8 of June 2026

    p1()

    p2()
