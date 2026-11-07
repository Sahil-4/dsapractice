import heapq
from typing import Optional


class Solution1:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # idle servers ordered by (weight, index)
        free = [(weight, index) for index, weight in enumerate(servers)]
        heapq.heapify(free)

        # busy servers ordered by (time they become free, weight, index)
        busy: list[tuple[int, int, int]] = []

        result = []
        time = 0

        for i, duration in enumerate(tasks):
            # task i cannot start before second i
            time = max(time, i)

            # every server is busy : jump ahead to the moment the earliest one frees up
            if not free:
                time = max(time, busy[0][0])

            # release every server that has finished by now
            while busy and busy[0][0] <= time:
                _, weight, index = heapq.heappop(busy)
                heapq.heappush(free, (weight, index))

            # smallest weight, then smallest index
            weight, index = heapq.heappop(free)
            heapq.heappush(busy, (time + duration, weight, index))

            result.append(index)

        return result

        # Complexity analysis
        # Time : O((N + M) * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1882. Process Tasks Using Servers - https://leetcode.com/problems/process-tasks-using-servers/description/?envType=daily-question&envId=2026-11-07

    testcase = [
        [
            [3, 3, 2],
            [1, 2, 3, 2, 1, 2],
            [2, 2, 0, 2, 1, 2],
        ],
        [
            [5, 1, 4, 3, 2],
            [2, 1, 2, 4, 5, 2, 1],
            [1, 4, 1, 4, 1, 3, 2],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.assignTasks(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        # code here

        # upfront reserved
        reserved = set(arr)

        # names already assigned to users
        assigned = set()

        # next integer suffix to try for each base name
        suffix_tracker: dict[str, int] = {}

        result = []

        for name in arr:
            # first time this exact name appears -> retain unmodified
            if name not in assigned:
                assigned.add(name)
                result.append(name)

            else:
                # collision -> find the smallest positive integer suffix

                k = suffix_tracker.get(name, 1)
                candidate = f"{name}{k}"

                # suffix cannot be an original reserved name or an already assigned name
                while candidate in reserved or candidate in assigned:
                    k += 1
                    candidate = f"{name}{k}"

                # advance tracker for the next collision of this base name
                suffix_tracker[name] = k + 1
                assigned.add(candidate)
                result.append(candidate)

        return result

        # Complexity analysis
        # Time : O(N*L)
        # Space : O(N*L)


def p2():
    # Problem 2 : POTD Geeksforgeeks Generate Usernames - https://www.geeksforgeeks.org/problems/new-registration-system--150419/1

    testcase = [
        [
            ["aba", "ab", "aba", "aba", "ab"],
            ["aba", "ab", "aba1", "aba2", "ab1"],
        ],
        [
            ["a", "a", "a1", "a"],
            ["a", "a2", "a1", "a3"],
        ],
        [
            ["aba1", "aba", "aba"],
            ["aba1", "aba", "aba2"],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.generateUsernames(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def isHappy(self, n: int) -> bool:
        def next_number(x: int) -> int:
            total = 0
            while x > 0:
                x, digit = divmod(x, 10)
                total += digit * digit
            return total

        # the sequence either reaches 1 or enters a cycle, floyd's cycle detection
        slow = n
        fast = next_number(n)

        while fast != 1 and slow != fast:
            slow = next_number(slow)
            fast = next_number(next_number(fast))

        return fast == 1

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 202. Happy Number - https://leetcode.com/problems/happy-number/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [19, True],
        [2, False],
        [1, True],
        [7, True],
        [4, False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.isHappy(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


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


class Solution4:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            _next = curr.next

            # point the current node backwards
            curr.next = prev

            prev = curr
            curr = _next

        return prev

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p4():
    # Problem 4 : NC150 Leetcode 206. Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            ListNode.__from_list__([1, 2, 3, 4, 5]),
            ListNode.__from_list__([5, 4, 3, 2, 1]),
        ],
        [ListNode.__from_list__([1, 2]), ListNode.__from_list__([2, 1])],
        [ListNode.__from_list__([]), ListNode.__from_list__([])],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.reverseList(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 7 of November 2026

    p1()

    p2()

    p3()

    p4()
