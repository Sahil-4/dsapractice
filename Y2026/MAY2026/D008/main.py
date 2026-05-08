from collections import deque
from typing import List


class Solution1:
    def build_sieve(self, n: int) -> List[bool]:
        sieve = [True] * (n + 1)

        if n >= 0:
            sieve[0] = False

        if n >= 1:
            sieve[1] = False

        for i in range(2, int(n**0.5) + 1):
            if not sieve[i]:
                continue

            for j in range(i * i, n + 1, i):
                sieve[j] = False

        return sieve

    def minJumps(self, nums: List[int]) -> int:

        N = len(nums)

        max_val = max(nums)
        prime = self.build_sieve(max_val)
        mp = {}
        for index, num in enumerate(nums):
            if num not in mp:
                mp[num] = []
            mp[num].append(index)

        seen = set()
        visited = [False] * N
        queue = deque([0])

        visited[0] = True

        steps = 0

        while queue:
            size = len(queue)

            for _ in range(size):
                i = queue.popleft()

                if i == N - 1:
                    return steps

                if i - 1 >= 0 and not visited[i - 1]:
                    visited[i - 1] = True
                    queue.append(i - 1)

                if i + 1 < N and not visited[i + 1]:
                    visited[i + 1] = True
                    queue.append(i + 1)

                if not prime[nums[i]] or nums[i] in seen:
                    continue

                for multiple in range(nums[i], max_val + 1, nums[i]):
                    if multiple not in mp:
                        continue

                    for j in mp[multiple]:
                        if not visited[j]:
                            visited[j] = True
                            queue.append(j)

                seen.add(nums[i])

            steps += 1

        return steps

        # Complexity analysis
        # Time : O(N + max_val * log(log(max_val)))
        # Space : O(N + max_val)


def p1():
    # Problem 1 : POTD Leetcode 3629. Minimum Jumps to Reach End via Prime Teleportation - https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/description/?envType=daily-question&envId=2026-05-08

    testcase = [
        [[1, 2, 4, 6], 2],
        [[2, 3, 4, 7, 9], 2],
        [[4, 6, 5, 8], 3],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.minJumps(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def validParenthesis(self, s: str) -> List[str]:
        # code here

        arr = list(s)
        N = len(arr)

        valid_strings = set()
        min_removals = N

        def solve(
            si: int, removal_count: int, balance: int, curr_state: List[str]
        ) -> None:
            nonlocal min_removals, valid_strings

            if si == N:
                if balance != 0:
                    return

                if removal_count < min_removals:
                    min_removals = removal_count
                    valid_strings.clear()
                if removal_count == min_removals:
                    valid_strings.add("".join(curr_state))

                return

            # not a parenthesis
            if arr[si] != ")" and arr[si] != "(":
                curr_state.append(arr[si])
                solve(si + 1, removal_count, balance, curr_state)
                curr_state.pop()
                return

            # opening paren - pick case
            if arr[si] == "(":
                curr_state.append(arr[si])
                solve(si + 1, removal_count, balance + 1, curr_state)
                curr_state.pop()

            # closing paren - pick case
            if arr[si] == ")" and balance > 0:
                curr_state.append(arr[si])
                solve(si + 1, removal_count, balance - 1, curr_state)
                curr_state.pop()

            # not pick case
            solve(si + 1, removal_count + 1, balance, curr_state)

        solve(0, 0, 0, [])

        return sorted(list(valid_strings))

        # Complexity analysis
        # Time : O(2^N)
        # Space : O(2^N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Remove Invalid Parentheses - https://www.geeksforgeeks.org/problems/remove-invalid-parentheses/1

    testcase = [
        ["()())()", ["(())()", "()()()"]],
        ["(a)())()", ["(a())()", "(a)()()"]],
        [")(", [""]],
    ]

    for line in testcase:
        [s, expected] = line
        s2 = Solution2()
        result = s2.validParenthesis(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 8 of May 2026

    p1()

    p2()
