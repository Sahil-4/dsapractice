class Solution1:
    def closedIsland(self, grid: list[list[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        WATER = 1
        LAND = 0

        count = 0

        # dfs flood fill
        def dfs(r: int, c: int) -> None:
            # Base case: out of bounds or already water (1)
            if r < 0 or r >= N or c < 0 or c >= M or grid[r][c] == WATER:
                return

            # sink current land cell (0 -> 1) to mark as visited
            grid[r][c] = WATER

            # Flood-fill all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # step 1: sink all islands connected to the outer border
        for r in range(N):
            for c in range(M):
                if (r in (0, N - 1) or c in (0, M - 1)) and grid[r][c] == LAND:
                    dfs(r, c)

        # step 2: count and sink the remaining closed islands in the interior
        for r in range(1, N - 1):
            for c in range(1, M - 1):
                if grid[r][c] == LAND:
                    count += 1
                    dfs(r, c)

        return count

        # Complexity analysis
        # Time : O(N*M)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1254. Number of Closed Islands - https://leetcode.com/problems/number-of-closed-islands/description/?envType=daily-question&envId=2026-10-25

    testcase = [
        [
            [
                [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0],
            ],
            2,
        ],
        [[[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]], 1],
        [
            [
                [1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1],
            ],
            2,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.closedIsland(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def beautySum(self, s: str) -> int:
        # code here
        N = len(s)

        t_sum = 0

        for si in range(N):
            frequency = {}

            for ei in range(si, N):
                ch = s[ei]

                frequency[ch] = frequency.get(ch, 0) + 1

                max_freq = max(frequency.values())
                min_freq = min(frequency.values())

                t_sum += max_freq - min_freq

        return t_sum

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Sum of Beauty of All Substrings - https://www.geeksforgeeks.org/problems/sum-of-beauty-of-all-substrings-1662962118/1

    testcase = [
        ["aaac", 3],
        ["aabc", 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.beautySum(*inputs)
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


class Solution3:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        nodes: list[ListNode] = []

        curr = head
        while curr:
            next_node = curr.next
            curr.next = None

            nodes.append(curr)

            curr = next_node

        N = len(nodes)

        l = 0
        r = N - 1

        curr = ListNode(0)
        while l <= r:
            assert curr is not None

            curr.next = nodes[l]
            curr = curr.next
            l += 1

            if l < r:  # odd number of nodes, dont add the middle node twice
                curr.next = nodes[r]
                curr = curr.next
                r -= 1

        head = curr.next

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 143. Reorder List - https://leetcode.com/problems/reorder-list/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            ListNode.__from_list__([1, 2, 3, 4]),
            [1, 4, 2, 3],
        ],
        [
            ListNode.__from_list__([1, 2, 3, 4, 5]),
            [1, 5, 2, 4, 3],
        ],
        [
            ListNode.__from_list__([1]),
            [1],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        s3.reorderList(*inputs)
        result = ListNode.__to_list__(inputs[0])
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 25 of October 2026

    p1()

    p2()

    p3()
