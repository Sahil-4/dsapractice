from typing import Optional


class Solution1:
    def countCommas(self, n: int) -> int:
        # 1-999; commas = 0
        # 1,000-999,999; commas = 1
        # 1,000,000-999,999,999; commas = 2

        count = 0

        # for i in range(1, n + 1):
        #     if i >= 1 and i <= 999:
        #         count += 0
        #     if i >= 1_000 and i <= 999_999:
        #         count += 1
        #     if i >= 1_000_000 and i <= 999_999_999:
        #         count += 2

        if n >= 1_000:
            count += n - 1_000 + 1
        if n >= 1_000_000:
            count += n - 1_000_000 + 1
        # if n >= 1_000_000_000: # no need
        #     count += n - 1_000_000_000 + 1

        return count

        # Complexity Analysis
        # Time : O(1)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3870. Count Commas in Range - https://leetcode.com/problems/count-commas-in-range/description/?envType=daily-question&envId=2026-09-08

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
    def searchWord(self, mat: list[list[str]], word: str) -> list[list[int]]:
        # code here
        _DR = ["U", "D", "L", "R", "UL", "UR", "DL", "DR"]

        N = len(mat)
        M = len(mat[0])
        K = len(word)

        def work_lookup(r: int, c: int, wi: int, dr: str) -> bool:
            if wi == K:
                return True

            if r < 0 or r >= N or c < 0 or c >= M:
                return False

            if mat[r][c] != word[wi]:
                return False

            if dr == "U":
                return work_lookup(r - 1, c, wi + 1, dr)
            elif dr == "D":
                return work_lookup(r + 1, c, wi + 1, dr)
            elif dr == "L":
                return work_lookup(r, c - 1, wi + 1, dr)
            elif dr == "R":
                return work_lookup(r, c + 1, wi + 1, dr)
            elif dr == "UL":
                return work_lookup(r - 1, c - 1, wi + 1, dr)
            elif dr == "UR":
                return work_lookup(r - 1, c + 1, wi + 1, dr)
            elif dr == "DL":
                return work_lookup(r + 1, c - 1, wi + 1, dr)
            elif dr == "DR":
                return work_lookup(r + 1, c + 1, wi + 1, dr)

            return False

        results = set()

        for r in range(N):
            for c in range(M):
                if mat[r][c] != word[0]:
                    continue

                for dr in _DR:
                    if work_lookup(r, c, 0, dr):
                        results.add((r, c))

        return sorted([list(x) for x in results])

        # Complexity Analysis
        # Time : O(N * M * K)
        # Space : O(K)


def p2():
    # Problem 2 : POTD Geeksforgeeks Word in Grid - All Occurrences - https://www.geeksforgeeks.org/problems/find-the-string-in-grid0111/1

    testcase = [
        [
            [
                ["a", "b", "a", "b"],
                ["a", "b", "e", "b"],
                ["e", "b", "e", "b"],
            ],
            "abe",
            [[0, 0], [0, 2], [1, 0]],
        ],
        [
            [
                ["G", "E", "E", "K", "S", "F", "O", "R", "G", "E", "E", "K", "S"],
                ["G", "E", "E", "K", "S", "Q", "U", "I", "Z", "G", "E", "E", "K"],
                ["I", "D", "E", "Q", "A", "P", "R", "A", "C", "T", "I", "C", "E"],
            ],
            "GEEKS",
            [[0, 0], [0, 8], [1, 0]],
        ],
        [
            [
                ["a", "b", "c", "d"],
                ["b", "c", "d", "e"],
                ["c", "d", "e", "f"],
            ],
            "a",
            [[0, 0]],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.searchWord(*inputs)
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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        merged_head = ListNode(0)
        curr = merged_head

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return merged_head.next

        # Complexity Analysis
        # Time : O(N + M)
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 22. Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            ListNode.__from_list__([1, 2, 4]),
            ListNode.__from_list__([1, 3, 4]),
            ListNode.__from_list__([1, 1, 2, 3, 4, 4]),
        ],
        [
            ListNode.__from_list__([]),
            ListNode.__from_list__([]),
            ListNode.__from_list__([]),
        ],
        [
            ListNode.__from_list__([]),
            ListNode.__from_list__([0]),
            ListNode.__from_list__([0]),
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.mergeTwoLists(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def generateParenthesis(self, n: int) -> list[str]:
        # open, close

        parentheses = []

        def backtrack(open_count: int, close_count: int, current: str):
            if len(current) == 2 * n:
                parentheses.append(current)
                return

            if open_count < n:
                backtrack(open_count + 1, close_count, current + "(")

            if close_count < open_count:
                backtrack(open_count, close_count + 1, current + ")")

        backtrack(0, 0, "")
        return parentheses

        # Complexity Analysis
        # Time : O(2^N)
        # Space : O(1)


def p4():
    # Problem 4 : NC150 Leetcode 21. Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [3, ["((()))", "(()())", "(())()", "()(())", "()()()"]],
        [1, ["()"]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.generateParenthesis(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 8 of September 2026

    p1()

    p2()

    p3()

    p4()
