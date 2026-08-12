class Solution1:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        N = len(nums)

        max_subarray_length = 0
        frequency = dict()

        l = 0
        for r in range(N):
            if nums[r] not in frequency:
                frequency[nums[r]] = 0

            frequency[nums[r]] += 1

            while frequency[nums[r]] > k:
                frequency[nums[l]] -= 1
                l += 1

            max_subarray_length = max(max_subarray_length, r - l + 1)

        return max_subarray_length

        # Complexity analysis
        # Time : O(2N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2958. Length of Longest Subarray With at Most K Frequency - https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/?envType=daily-question&envId=2026-08-12

    testcase = [
        [[1, 2, 3, 1, 2, 3, 1, 2], 2, 6],
        [[1, 2, 1, 2, 1, 2, 1, 2], 1, 2],
        [[5, 5, 5, 5, 5, 5, 5], 4, 4],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maxSubarrayLength(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findWays(self, grid: list[list[int]]) -> list[int]:

        MOD = 10**9 + 7
        n = len(grid)

        ways = [[0] * n for _ in range(n)]
        best = [[-1] * n for _ in range(n)]

        # exit
        ways[n - 1][n - 1] = 1
        best[n - 1][n - 1] = grid[n - 1][n - 1]

        # bottom-right -> top-left
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):

                if r == n - 1 and c == n - 1:
                    continue

                next_cells = []

                # right
                if grid[r][c] in (1, 3):
                    if c + 1 < n and best[r][c + 1] != -1:
                        next_cells.append((r, c + 1))

                # down
                if grid[r][c] in (2, 3):
                    if r + 1 < n and best[r + 1][c] != -1:
                        next_cells.append((r + 1, c))

                # no valid path from current cell
                if not next_cells:
                    continue

                # number of paths
                for nr, nc in next_cells:
                    ways[r][c] += ways[nr][nc]

                ways[r][c] %= MOD

                # maximum Adventure
                best[r][c] = grid[r][c] + max(best[nr][nc] for nr, nc in next_cells)

        if best[0][0] == -1:
            return [0, 0]

        return [ways[0][0], best[0][0]]

    # Complexity analysis
    # Time : O(N * N)
    # Space : O(N * N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Adventure in a Maze - https://www.geeksforgeeks.org/problems/adventure-in-a-maze2051/1

    testcase = [
        [
            [
                [3, 2],
                [1, 3],
            ],
            [2, 8],
        ],
        [
            [
                [1, 1, 3, 2, 1],
                [3, 2, 2, 1, 2],
                [1, 3, 3, 1, 3],
                [1, 2, 3, 1, 2],
                [1, 1, 1, 3, 1],
            ],
            [4, 18],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.findWays(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 12 of August 2026

    p1()

    p2()
