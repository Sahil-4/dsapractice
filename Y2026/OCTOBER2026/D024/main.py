from typing import Optional


class Solution1:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:

        # days count in any month
        month_days = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }

        # overlap
        s = max(arriveAlice, arriveBob)
        e = min(leaveAlice, leaveBob)

        # for each month
        ms = int(s[:2])
        me = int(e[:2])

        # add days of each month
        d = 0
        for mi in range(ms, me + 1):
            d += month_days[mi]

        # day start, day end
        ds = int(s[3:])
        de = int(e[3:])

        # reduce extra days
        d -= ds - 1
        d -= month_days[me] - de

        # return overlapping days - OR 0 if negative
        return max(0, d)

        # Complexity analysis
        # Time : O(M)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2409. Count Days Spent Together - https://leetcode.com/problems/count-days-spent-together/description/?envType=daily-question&envId=2026-10-24

    testcase = [
        ["08-15", "08-18", "08-16", "08-19", 3],
        ["10-01", "10-31", "11-01", "12-31", 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.countDaysTogether(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def isPossible(self, n: int, m: int, s: str) -> bool:
        # code here
        maxR = 0
        minR = 0
        maxC = 0
        minC = 0

        r, c = 0, 0
        for d in s:
            match d:
                case "L":
                    c -= 1
                case "R":
                    c += 1
                case "D":
                    r += 1
                case "U":
                    r -= 1

            maxR = max(maxR, r)
            minR = min(minR, r)
            maxC = max(maxC, c)
            minC = min(minC, c)

        req_height = maxR - minR + 1
        req_width = maxC - minC + 1

        if req_height <= n and req_width <= m:
            return True

        return False

        # Complexity analysis
        # Time : O(S)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Trace Path - https://www.geeksforgeeks.org/problems/trace-path3840/1

    testcase = [
        [1, 1, "R", False],
        [2, 3, "LLRU", True],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.isPossible(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        N = len(s)

        dictionary = set(wordDict)

        dp = [False] * (N + 1)
        dp[N] = True

        for si in range(N - 1, -1, -1):
            result = False
            substr = []

            for i2 in range(si, N):
                substr.append(s[i2])
                substr_str = "".join(substr)

                if substr_str in dictionary:
                    result = dp[i2 + 1]

                if result:
                    break

            dp[si] = result

        return dp[0]

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 139. Word Break - https://leetcode.com/problems/word-break/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["leetcode", ["leet", "code"], True],
        ["applepenapple", ["apple", "pen"], True],
        ["catsandog", ["cats", "dog", "sand", "and", "cat"], False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.wordBreak(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


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

    @property
    def tail(self):
        tail = self
        curr = self

        while curr:
            tail = curr
            curr = curr.next

        return tail

    def set_cycle(self, pos: int):
        if pos < 0:
            return

        target_node = None
        curr = self
        idx = 0

        while curr:
            if idx == pos:
                target_node = curr
            if curr.next is None:
                curr.next = target_node
                break
            curr = curr.next
            idx += 1


class Solution4:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head
        tortoise = head

        while hare and tortoise and tortoise.next:
            hare = hare.next
            tortoise = tortoise.next.next

            if hare is tortoise:
                return True

        return False

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p4():
    # Problem 4 : NC150 Leetcode 141. Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[3, 2, 0, -4], 1, True],
        [[1, 2], 0, True],
        [[1], -1, False],
    ]

    for line in testcase:
        [arr, pos, expected] = line
        ll = ListNode.__from_list__(arr)
        if ll:
            ll.set_cycle(pos)

        s4 = Solution4()
        result = s4.hasCycle(ll)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 24 of October 2026

    p1()

    p2()

    p3()

    p4()
