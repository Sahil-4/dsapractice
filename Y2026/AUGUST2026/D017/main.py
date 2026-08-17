class Solution1:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        N = len(stoneValue)

        if N <= 1:
            return 0

        dp = [[0] * N for _ in range(N)]
        left_best = [[0] * N for _ in range(N)]
        right_best = [[0] * N for _ in range(N)]

        for start in range(N - 1, -1, -1):
            left_best[start][start] = stoneValue[start]
            right_best[start][start] = stoneValue[start]

            total = stoneValue[start]
            left_sum = 0
            split = start - 1

            for end in range(start + 1, N):
                total += stoneValue[end]

                while (
                    split + 1 < end and (left_sum + stoneValue[split + 1]) * 2 <= total
                ):
                    split += 1
                    left_sum += stoneValue[split]

                if start <= split:
                    dp[start][end] = max(dp[start][end], left_best[start][split])

                if split + 1 < end:
                    dp[start][end] = max(dp[start][end], right_best[split + 2][end])

                if left_sum * 2 == total:
                    dp[start][end] = max(dp[start][end], right_best[split + 1][end])

                left_best[start][end] = max(
                    left_best[start][end - 1], total + dp[start][end]
                )

                right_best[start][end] = max(
                    right_best[start + 1][end], total + dp[start][end]
                )

        return dp[0][N - 1]

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(N * N)


def p1():
    # Problem 1 : POTD Leetcode 1563. Stone Game V - https://leetcode.com/problems/stone-game-v/description/?envType=daily-question&envId=2026-08-17

    testcase = [
        [[6, 2, 3, 4, 5, 5], 18],
        [[7, 7, 7, 7, 7, 7, 7], 28],
        [[4], 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.stoneGameV(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minThrows(self, n: int, lad: list[int], sn: list[int]) -> int:

        destination = n * n

        jump = {}

        for i in range(0, len(lad), 2):
            jump[lad[i]] = lad[i + 1]

        for i in range(0, len(sn), 2):
            jump[sn[i]] = sn[i + 1]

        visited = bytearray(destination + 1)
        visited[1] = 1

        queue = [(1, 0)]
        front = 0

        while front < len(queue):

            curr, throws = queue[front]
            front += 1

            if curr == destination:
                return throws

            for dice in range(1, 7):
                next_cell = curr + dice

                if next_cell > destination:
                    break

                next_cell = jump.get(next_cell, next_cell)

                if not visited[next_cell]:
                    visited[next_cell] = 1
                    queue.append((next_cell, throws + 1))

        return -1

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(N*N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Snake and Ladder Problem - https://www.geeksforgeeks.org/problems/snake-and-ladder-problem4816/1

    testcase = [
        [6, [3, 22, 5, 8, 11, 35, 20, 32], [17, 4, 19, 7, 34, 1, 21, 9], 3],
        [3, [2, 8], [7, 3], 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minThrows(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 17 of August 2026

    p1()

    p2()
