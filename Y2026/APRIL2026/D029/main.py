from typing import List


class Solution1:
    def maximumScore(self, grid: List[List[int]]) -> int:
        N = len(grid)

        if N == 1:
            return 0

        # prefix sums for each column
        pref = [[0] * (N + 1) for _ in range(N)]
        for c in range(N):
            for r in range(N):
                pref[c][r + 1] = pref[c][r] + grid[r][c]

        # dp[col][curr_height][prev_height]
        dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N)]

        # helper structures
        best_prefix = [[0] * (N + 1) for _ in range(N + 1)]
        best_suffix = [[0] * (N + 1) for _ in range(N + 1)]

        for col in range(1, N):
            for h_cur in range(N + 1):
                for h_prev in range(N + 1):

                    if h_cur <= h_prev:
                        gain = pref[col][h_prev] - pref[col][h_cur]
                        dp[col][h_cur][h_prev] = best_suffix[h_prev][0] + gain
                    else:
                        gain = pref[col - 1][h_cur] - pref[col - 1][h_prev]
                        dp[col][h_cur][h_prev] = max(
                            best_suffix[h_prev][h_cur],
                            best_prefix[h_prev][h_cur] + gain,
                        )

            # rebuild helper arrays
            for h_cur in range(N + 1):
                # prefix max
                running = float("-inf")
                for h_prev in range(N + 1):
                    penalty = 0
                    if h_prev > h_cur:
                        penalty = pref[col][h_prev] - pref[col][h_cur]

                    running = max(running, dp[col][h_cur][h_prev] - penalty)
                    best_prefix[h_cur][h_prev] = int(running)

                # suffix max
                running = float("-inf")
                for h_prev in range(N, -1, -1):
                    running = max(running, dp[col][h_cur][h_prev])
                    best_suffix[h_cur][h_prev] = int(running)

        # final answer
        res = 0
        for h in range(N + 1):
            res = max(res, dp[N - 1][0][h], dp[N - 1][N][h])

        return res

        # Complexity analysis
        # Time : O(N*N*N)
        # Space : O(N*N*N)


def p1():
    # Problem 1 : POTD Leetcode 3225. Maximum Score From Grid Operations - https://leetcode.com/problems/maximum-score-from-grid-operations/description/?envType=daily-question&envId=2026-04-29

    testcase = [
        [
            [
                [0, 0, 0, 0, 0],
                [0, 0, 3, 0, 0],
                [0, 1, 0, 0, 0],
                [5, 0, 0, 3, 0],
                [0, 0, 0, 0, 2],
            ],
            11,
        ],
        [
            [
                [10, 9, 0, 0, 15],
                [7, 1, 0, 8, 0],
                [5, 20, 0, 11, 0],
                [0, 0, 0, 1, 2],
                [8, 12, 1, 10, 3],
            ],
            94,
        ],
    ]

    for line in testcase:
        [grid, expected] = line
        s1 = Solution1()
        result = s1.maximumScore(grid)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:

    def minSwaps(self, arr: List[int]) -> int:
        # code here
        # minimum swaps = k - (max number of 1s in any window of size k)
        # k = total number of 1s

        N = len(arr)

        # count total 1s
        k = sum(arr)

        if k == 0:
            return -1

        # initial window
        curr_ones = sum(arr[:k])
        max_ones = curr_ones

        # sliding window
        for i in range(k, N):
            curr_ones += arr[i]  # include next
            curr_ones -= arr[i - k]  # remove left

            max_ones = max(max_ones, curr_ones)

        return k - max_ones

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Min Swaps to Group 1s - https://www.geeksforgeeks.org/problems/minimum-swaps-required-to-group-all-1s-together2451/1

    testcase = [
        [[1, 0, 1, 0, 1], 1],
        [[1, 0, 1, 0, 1, 1], 1],
        [[0, 0, 0], -1],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.minSwaps(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 29 of April 2026

    p1()

    p2()
