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
    def list_length(self, head: Optional[ListNode]) -> int:
        length = 0

        temp = head
        while temp != None:
            temp = temp.next
            length += 1

        return length

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        N = self.list_length(head)
        if N <= 1:
            return head

        k = k % N
        if k == 0:
            return head

        temp = head
        for _ in range(N - k - 1):
            temp = temp.next

        new_head = temp.next
        temp.next = None

        temp = new_head
        while temp.next != None:
            temp = temp.next

        temp.next = head
        temp = None

        return new_head

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 61. Rotate List - https://leetcode.com/problems/rotate-list/description/?envType=daily-question&envId=2026-05-05

    testcase = [
        [[1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]],
        [[0, 1, 2], 4, [2, 0, 1]],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s1 = Solution1()
        head = ListNode.__from_list__(arr)
        result = s1.rotateRight(head, k)
        result = ListNode.__to_list__(result)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def sumXOR(self, arr: List[int]) -> int:
        # code here

        xor_sum = 0

        for i in range(32):
            zc = 0
            oc = 0

            for j in range(len(arr)):
                if arr[j] >> i & 1:
                    oc += 1
                else:
                    zc += 1

            xor_sum += (zc * oc) * (1 << i)

        return xor_sum

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Sum of XOR of all pairs - https://www.geeksforgeeks.org/problems/sum-of-xor-of-all-pairs0723/1

    testcase = [
        [[7, 3, 5], 12],
        [[5, 9, 7, 6], 47],
        [[10], 0],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.sumXOR(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 5 of May 2026

    p1()

    p2()
