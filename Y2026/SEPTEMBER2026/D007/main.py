from typing import Optional


class Solution1:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 1000000007

        N = len(s)

        total = 0
        end = [0] * 26

        for c in s:
            idx = ord(c) - ord("a")
            prev_total = total
            new_subseq_count = (prev_total + 1 - end[idx] + MOD) % MOD
            total = (total + new_subseq_count) % MOD
            end[idx] += new_subseq_count

        return total

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 940. Distinct Subsequences II - https://leetcode.com/problems/distinct-subsequences-ii/description/?envType=daily-question&envId=2026-09-07

    testcase = [
        ["abc", 7],
        ["aba", 6],
        ["aaa", 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.distinctSubseqII(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minCount(self, arr: list[int]) -> int:
        BASE = 102

        # inc = 0 means -infinity
        # dec = 101 means +infinity
        dp = {101: 0}  # 0 * 102 + 101

        for x in arr:
            ndp = dp.copy()

            for key, selected in dp.items():

                inc = key // BASE
                dec = key % BASE

                # increasing:
                # x > inc, where inc == 0 means -infinity
                if x > inc:
                    new_key = x * BASE + dec
                    new_value = selected + 1

                    old = ndp.get(new_key, -1)
                    if new_value > old:
                        ndp[new_key] = new_value

                # decreasing:
                # x < dec, where dec == 101 means +infinity
                if x < dec:
                    new_key = inc * BASE + x
                    new_value = selected + 1

                    old = ndp.get(new_key, -1)
                    if new_value > old:
                        ndp[new_key] = new_value

            dp = ndp

        return len(arr) - max(dp.values())

        # Complexity Analysis
        # Time : O(N * V * V)
        # Space : O(N * V * V)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Elements Outside Subsequences - https://www.geeksforgeeks.org/problems/minimum-number-of-elements-which-are-not-part-of-increasing-or-decreasing-subsequence2617/1

    testcase = [
        [[7, 8, 1, 2, 4, 6, 3, 5, 2, 1, 8, 7], 2],
        [[1, 4, 2, 3, 3, 2, 4], 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minCount(*inputs)
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        # count nodes
        temp = head
        while temp:
            N += 1
            temp = temp.next

        # remove nth node from end
        to_remove = N - n
        if to_remove == 0:
            if head:
                head = head.next
            return head

        # Find the node before the one to remove
        temp = head
        for _ in range(to_remove - 1):
            temp = temp.next if temp else None

        # Remove the nth node from end
        if temp and temp.next:
            temp.next = temp.next.next

        return head

        # Complexity Analysis
        # Time : O(N)
        # Time : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 19. Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            ListNode.__from_list__([1, 2, 3, 4, 5]),
            2,
            ListNode.__from_list__([1, 2, 3, 5]),
        ],
        [
            ListNode.__from_list__([1]),
            1,
            ListNode.__from_list__([]),
        ],
        [
            ListNode.__from_list__([1, 2]),
            1,
            ListNode.__from_list__([1]),
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.removeNthFromEnd(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or stack.pop() != mapping[char]:
                    return False

        return not stack

        # Complexity Analysis
        # Time : O(N)
        # Space : O(N)


def p4():
    # Problem 4 : NC150 Leetcode 20. Valid Parentheses - https://leetcode.com/problems/valid-parentheses/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["()", True],
        ["()[]{}", True],
        ["(]", False],
        ["([])", True],
        ["([)]", False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.isValid(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 7 of September 2026

    p1()

    p2()

    p3()

    p4()
