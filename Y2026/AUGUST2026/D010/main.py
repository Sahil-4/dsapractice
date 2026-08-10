from math import isqrt


class Solution1:
    def winnerSquareGame(self, n: int) -> bool:

        dp = [False] * (n + 1)

        # dp[0] = False
        # No stones -> current player loses

        for i in range(1, n + 1):
            for j in range(1, isqrt(i) + 1):
                square = j * j

                # winning state
                if not dp[i - square]:
                    dp[i] = True
                    break

        return dp[n]

        # Complexity analysis
        # Time : O(N * sqrt(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1510. Stone Game IV - https://leetcode.com/problems/stone-game-iv/description/?envType=daily-question&envId=2026-08-10

    testcase = [
        [1, True],
        [2, False],
        [4, True],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.winnerSquareGame(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxTask(self, h: list[int], l: list[int]) -> int:
        # code here

        N = len(h)

        no_task = 0
        low = l[0]
        high = h[0]

        for i in range(1, N):
            prev_no_task = no_task
            prev_low = low
            prev_high = high

            best_prev = max(prev_no_task, prev_low, prev_high)

            # no task today
            no_task = best_prev

            # low-effort task today
            low = best_prev + l[i]

            # high-effort task requires no task yesterday
            high = prev_no_task + h[i]

        return max(no_task, low, high)

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks High Effort vs Low Effort - https://www.geeksforgeeks.org/problems/high-effort-vs-low-effort0213/1

    testcase = [
        [[2, 8, 1], [1, 2, 1], 9],
        [[3, 6, 8, 7, 6], [1, 5, 4, 5, 3], 20],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxTask(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 10 of August 2026

    p1()

    p2()
