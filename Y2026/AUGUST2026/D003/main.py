class Solution1:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        N = len(stoneValue)
        alice, bob = 1, 0

        t = [[-1] * (N + 1) for _ in range(2)]

        def miniMax(player: int, i: int) -> int:
            if i >= N:
                return 0

            if t[player][i] != -1:
                return t[player][i]

            if player == alice:
                result = -(10**18)
                stones = 0
                for j in range(i, min(i + 3, N)):
                    stones += stoneValue[j]
                    result = max(result, stones + miniMax(bob, j + 1))
            else:
                result = 10**18
                stones = 0
                for j in range(i, min(i + 3, N)):
                    stones -= stoneValue[j]
                    result = min(result, stones + miniMax(alice, j + 1))

            t[player][i] = result
            return t[player][i]

        diff = miniMax(alice, 0)

        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        return "Tie"

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1406. Stone Game III - https://leetcode.com/problems/stone-game-iii/description/?envType=daily-question&envId=2026-08-03

    testcase = [
        [[1, 2, 3, 7], "Bob"],
        [[1, 2, 3, -9], "Alice"],
        [[1, 2, 3, 6], "Tie"],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.stoneGameIII(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        # code here

        first_window_sum = 0
        for i in range(k):
            first_window_sum += arr[i]

        j = 0
        last = 0

        max_sum = -1000000001
        max_sum = max(max_sum, first_window_sum)

        # remaining windows
        for i in range(k, len(arr)):

            # expand
            first_window_sum += arr[i]

            # update accumulated prefix
            last = last + arr[j]
            j += 1

            # update max_sum
            max_sum = max(max_sum, first_window_sum)

            # shrink
            if last < 0:
                first_window_sum -= last
                max_sum = max(max_sum, first_window_sum)
                last = 0

        return max_sum

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Sum Subarray of Size at least K - https://www.geeksforgeeks.org/problems/largest-first_window_sum-subarray-of-size-at-least-k3121/1

    testcase = [
        [[1, -2, 2, -3], 3, 1],
        [[1, 1, 1, 1, 1, 1], 2, 6],
        [[-4, -2, 1, -3], 2, -1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxSumWithK(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 3 of August 2026

    p1()

    p2()
