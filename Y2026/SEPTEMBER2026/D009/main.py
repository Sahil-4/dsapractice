from typing import Optional
import heapq


class Solution1:
    def countCommas(self, n: int) -> int:
        # 1-999; commas = 0
        # 1,000-999,999; commas = 1
        # 1,000,000-999,999,999; commas = 2
        # 1_000_000_000_000_000

        count = 0

        if n >= 1_000:
            count += n - 1_000 + 1
        if n >= 1_000_000:
            count += n - 1_000_000 + 1
        if n >= 1_000_000_000:
            count += n - 1_000_000_000 + 1
        if n >= 1_000_000_000_000:
            count += n - 1_000_000_000_000 + 1
        if n >= 1_000_000_000_000_000:
            count += n - 1_000_000_000_000_000 + 1

        return count

        # Complexity Analysis
        # Time : O(1)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3871. Count Commas in Range II - https://leetcode.com/problems/count-commas-in-range-ii/description/?envType=daily-question&envId=2026-09-09

    testcase = [
        [1002, 3],
        [998, 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.countCommas(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findMax(self, n: int) -> int:
        s = str(n)

        # n itself is always a candidate
        best_candidate = n
        max_sum = sum(int(d) for d in s)

        # another best candidate:
        # decrease one non-zero digit by 1,
        # then make all following digits 9
        for i in range(len(s)):
            if s[i] == "0":
                continue

            candidate_str = s[:i] + str(int(s[i]) - 1) + "9" * (len(s) - i - 1)

            candidate = int(candidate_str)
            candidate_sum = sum(int(d) for d in candidate_str)

            if candidate_sum > max_sum:
                max_sum = candidate_sum
                best_candidate = candidate
            elif candidate_sum == max_sum:
                best_candidate = max(best_candidate, candidate)

        return best_candidate

        # Complexity analysis
        # Time : O(M)
        # Space : O(M)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Digit Sum Number in 1 to n - https://www.geeksforgeeks.org/problems/biggest-integer-having-maximum-digit-sum1704/1

    testcase = [
        [48, 48],
        [90, 89],
        [599641, 598999],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.findMax(*inputs)
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
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy_head_ptr = dummy_head

        # min heap powered
        pointers = []
        for l_list in lists or []:
            if l_list is not None:
                heapq.heappush(pointers, l_list)

        while pointers:
            min_node = heapq.heappop(pointers)
            dummy_head_ptr.next = min_node
            dummy_head_ptr = dummy_head_ptr.next

            if min_node.next is not None:
                heapq.heappush(pointers, min_node.next)

        return dummy_head.next

        # Complexity Analysis
        # Time : O(N * Log(K))
        # Space : O(K)


def p3():
    # Problem 3 : NC150 Leetcode 23. Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            [
                ListNode.__from_list__([1, 4, 5]),
                ListNode.__from_list__([1, 3, 4]),
                ListNode.__from_list__([2, 6]),
            ],
            ListNode.__from_list__([1, 1, 2, 3, 4, 4, 5, 6]),
        ],
        [
            ListNode.__from_list__([]),
            ListNode.__from_list__([]),
        ],
        [
            [
                ListNode.__from_list__([]),
            ],
            ListNode.__from_list__([]),
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.mergeKLists(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 9 of September 2026

    p1()

    p2()

    p3()
