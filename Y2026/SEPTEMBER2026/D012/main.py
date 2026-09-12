from bisect import bisect_right
from typing import Optional


class Solution1:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        N = len(intervals)
        K = 4

        # keep original index: [left, right, weight, original_index]
        intervals_copy = [
            [left, right, weight, i]
            for i, (left, right, weight) in enumerate(intervals)
        ]

        # sort by left endpoint, then right endpoint, ...
        intervals_copy.sort()

        # starting positions for binary search
        starts = [interval[0] for interval in intervals_copy]

        # next_idx[i] = first interval whose left endpoint is > intervals_copy[i].right
        # strictly greater is required because touching endpoints are overlapping
        next_idx = [bisect_right(starts, intervals_copy[i][1]) for i in range(N)]

        # dp[i][k] = (maximum score, lexicographically smallest indices)
        # obtainable using intervals_copy[i:] with at most k intervals_copy
        dp = [[(0, ()) for _ in range(K + 1)] for _ in range(N + 1)]

        for i in range(N - 1, -1, -1):
            left, right, weight, original_idx = intervals_copy[i]
            j = next_idx[i]

            for k in range(1, K + 1):
                # option 1: skip current interval.
                skip_score, skip_indices = dp[i + 1][k]

                # option 2: take current interval.
                next_score, next_indices = dp[j][k - 1]
                take_score = weight + next_score
                take_indices = tuple(sorted(next_indices + (original_idx,)))

                # maximize score; on a tie, choose lexicographically
                # smaller list of original indices.
                if take_score > skip_score:
                    dp[i][k] = (take_score, take_indices)
                elif take_score < skip_score:
                    dp[i][k] = (skip_score, skip_indices)
                else:
                    dp[i][k] = (take_score, min(skip_indices, take_indices))

        return list(dp[0][K][1])

        # Complexity analysis
        # Time : O(N * Log(N) + N * K * Log(K))
        # Space : O(N * K)


def p1():
    # Problem 1 : POTD Leetcode 3414. Maximum Score of Non-overlapping Intervals - https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/description/?envType=daily-question&envId=2026-09-12

    testcase = [
        [[[1, 3, 2], [4, 5, 2], [1, 5, 5], [6, 9, 3], [6, 7, 1], [8, 9, 1]], [2, 3]],
        [
            [
                [5, 8, 1],
                [6, 7, 7],
                [4, 7, 3],
                [9, 10, 6],
                [7, 8, 2],
                [11, 14, 3],
                [3, 5, 5],
            ],
            [1, 3, 5, 6],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maximumWeight(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxProduct(self, arr: list[int], k: int) -> int:
        N = len(arr)

        # dp[j][0] -> maximum product using exactly j elements
        # dp[j][1] -> minimum product using exactly j elements
        dp: list[list[Optional[int]]] = [[None, None] for _ in range(k + 1)]

        # choosing 0 elements => product is 1
        dp[0] = [1, 1]

        for x in arr:

            # go backwards so x is used only once
            for j in range(min(k, N), 0, -1):

                if dp[j - 1][0] is None:
                    continue

                old_max = dp[j - 1][0]
                old_min = dp[j - 1][1]

                candidate1 = old_max * x
                candidate2 = old_min * x

                new_max = max(candidate1, candidate2)
                new_min = min(candidate1, candidate2)

                # existing state represents "skip x"
                if dp[j][0] is None:
                    dp[j][0] = new_max
                    dp[j][1] = new_min
                else:
                    dp[j][0] = max(dp[j][0], new_max)
                    dp[j][1] = min(dp[j][1], new_min)

        return dp[k][0]

        # Complexity analysis
        # Time : O(N * K)
        # Space : O(K)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Product Subsequence of Size K - https://www.geeksforgeeks.org/problems/maximum-product4633/1

    testcase = [
        [[1, 2, 0, 3], 2, 6],
        [[1, 2, -1, -3, -6, 4], 4, 144],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxProduct(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def search(self, nums: list[int], target: int) -> int:
        # binary search

        N = len(nums)

        low = 0
        high = N - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            elif nums[low] <= nums[mid]:
                # left part is sorted (not rotated); will use it
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # right part is sorted (not rotated); will use it
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 33. Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[4, 5, 6, 7, 0, 1, 2], 0, 4],
        [[4, 5, 6, 7, 0, 1, 2], 3, -1],
        [[1], 0, -1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.search(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        T = 9

        def check_cols(row: int) -> bool:
            seen = set()
            for col in range(T):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
            return True

        def check_rows(col: int) -> bool:
            seen = set()
            for row in range(T):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
            return True

        def check_sub_grid(row_index: int, col_index: int) -> bool:
            seen = set()

            for x in range(3):
                for y in range(3):
                    row = row_index + x
                    col = col_index + y

                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False

                    seen.add(board[row][col])

            return True

        for row in range(T):
            if not check_cols(row):
                return False

        for col in range(T):
            if not check_rows(col):
                return False

        for row_index in range(0, T, 3):
            for col_index in range(0, T, 3):
                if not check_sub_grid(row_index, col_index):
                    return False

        return True

        # Complexity analysis
        # Time : O(T * T)
        # Space : O(1)


def p4():
    # Problem 4 : NC150 Leetcode 36. Valid Sudoku - https://leetcode.com/problems/valid-sudoku/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            True,
        ],
        [
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            False,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.isValidSudoku(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 12 of September 2026

    p1()

    p2()

    p3()

    p4()
