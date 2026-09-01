from collections import deque
from typing import Optional


class Solution1:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # directions: right, down, left, up
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        # give every litter cell a bit index.
        litter_id = [[-1] * n for _ in range(m)]

        sx = sy = 0
        litter_count = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "S":
                    sx, sy = i, j

                elif classroom[i][j] == "L":
                    litter_id[i][j] = litter_count
                    litter_count += 1

        # example:
        # litter_count = 3
        # full_mask = 111 (binary)
        full_mask = (1 << litter_count) - 1

        # best_energy[x][y][mask] =
        # maximum energy with which we have reached
        # (x, y) after collecting exactly the litter in mask.
        best_energy = [[[-1] * (1 << litter_count) for _ in range(n)] for _ in range(m)]

        # BFS state:
        # (row, col, collected_mask, remaining_energy, moves)
        queue = deque()

        best_energy[sx][sy][0] = energy
        queue.append((sx, sy, 0, energy, 0))

        while queue:
            x, y, mask, e, moves = queue.popleft()

            # since BFS processes states by increasing moves,
            # the first state with all litter collected is optimal
            if mask == full_mask:
                return moves

            # no energy means we cannot make another move
            if e == 0:
                continue

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                # outside grid or obstacle
                if nx < 0 or nx >= m or ny < 0 or ny >= n or classroom[nx][ny] == "X":
                    continue

                # moving normally costs one energy
                new_energy = e - 1

                # entering R resets energy to maximum
                if classroom[nx][ny] == "R":
                    new_energy = energy

                # collect litter if this cell contains one
                new_mask = mask

                if classroom[nx][ny] == "L":
                    litter_bit = litter_id[nx][ny]
                    new_mask |= 1 << litter_bit

                # if we have already reached the same
                # (position, mask) with >= energy,
                # this state cannot give us anything new
                if new_energy <= best_energy[nx][ny][new_mask]:
                    continue

                best_energy[nx][ny][new_mask] = new_energy
                best_energy[nx][ny][new_mask] = new_energy
                best_energy[nx][ny][new_mask] = new_energy
                best_energy[nx][ny][new_mask] = new_energy

                queue.append((nx, ny, new_mask, new_energy, moves + 1))

        return -1

        # Complexity analysis
        # Time : O(N * N * 2^L)
        # Space : O(N * N * 2^L)


def p1():
    # Problem 1 : POTD Leetcode 3568. Minimum Moves to Clean the Classroom - https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/description/?envType=daily-question&envId=2026-09-01

    testcase = [
        [["S.", "XL"], 2, 2],
        [["LS", "RL"], 4, 3],
        [["L.S", "RXL"], 3, -1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minMoves(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def palindromicStrings(self, n: int, k: int) -> int:
        # code here
        MOD = 10**9 + 7

        # dp[i][j] = number of ways to arrange
        # j distinct characters from i characters
        dp = [[0] * (k + 1) for _ in range(k + 1)]

        # P(i, 0) = 1
        for i in range(k + 1):
            dp[i][0] = 1

        # calculate permutations
        for i in range(1, k + 1):
            for j in range(1, i + 1):
                dp[i][j] = (dp[i - 1][j] + j * dp[i - 1][j - 1]) % MOD

        ans = 0

        # P(k, i) counts one odd and one even length
        for i in range(1, n // 2 + 1):
            ans += 2 * dp[k][i]
            ans %= MOD

        # if n is odd, the largest odd length
        # has no corresponding even length <= n
        if n % 2 == 1:
            ans += dp[k][n // 2 + 1]
            ans %= MOD

        return ans

        # Complexity analysis
        # Time : O(K * K)
        # Space : O(K * K)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count Palindromic Strings with Constraints - https://www.geeksforgeeks.org/problems/number-of-palindromic-strings2706/1

    testcase = [
        [3, 2, 6],
        [4, 3, 18],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.palindromicStrings(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = dict()

        for index, num in enumerate(nums):
            need = target - num

            if seen.get(need, None) is not None:
                return [seen[need], index]

            seen[num] = index

        return [-1, -1]

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 1. Two Sum - https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[2, 7, 11, 15], 9, [0, 1]],
        [[3, 2, 4], 6, [1, 2]],
        [[3, 3], 6, [0, 1]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.twoSum(*inputs)
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


class Solution4:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        answer = ListNode(-1)
        temp = answer

        l1_temp = l1
        l2_temp = l2

        carry = 0

        while l1_temp and l2_temp:
            _sum = l1_temp.val + l2_temp.val + carry
            _digit = _sum % 10
            carry = _sum // 10

            temp.next = ListNode(_digit)
            temp = temp.next

            l1_temp = l1_temp.next
            l2_temp = l2_temp.next

        while l1_temp:
            _sum = l1_temp.val + carry
            _digit = _sum % 10
            carry = _sum // 10

            temp.next = ListNode(_digit)
            temp = temp.next

            l1_temp = l1_temp.next

        while l2_temp:
            _sum = l2_temp.val + carry
            _digit = _sum % 10
            carry = _sum // 10

            temp.next = ListNode(_digit)
            temp = temp.next

            l2_temp = l2_temp.next

        while carry:
            _sum = carry
            _digit = _sum % 10
            carry = _sum // 10

            temp.next = ListNode(_digit)
            temp = temp.next

        return answer.next

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p4():
    # Problem 4 : NC150 Leetcode 2. Add Two Numbers - https://leetcode.com/problems/add-two-numbers/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            ListNode.__from_list__([2, 4, 3]),
            ListNode.__from_list__([5, 6, 4]),
            ListNode.__from_list__([7, 0, 8]),
        ],
        [
            ListNode.__from_list__([0]),
            ListNode.__from_list__([0]),
            ListNode.__from_list__([0]),
        ],
        [
            ListNode.__from_list__([9, 9, 9, 9, 9, 9, 9]),
            ListNode.__from_list__([9, 9, 9, 9]),
            ListNode.__from_list__([8, 9, 9, 9, 0, 0, 0, 1]),
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.addTwoNumbers(*inputs)
        print(ListNode.__to_list__(result))
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 1 of September 2026

    p1()

    p2()

    p3()

    p4()
