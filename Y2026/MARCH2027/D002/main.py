from typing import List


class Solution1:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # pre-compute numbers of trailing zeroes for all rows
        # for any row at index i we need zeroes = N - i - 1
        # for any row i pick first such row that satisfy this
        # if not found immediately return -1

        N = len(grid)

        row_zeroes_count = [0] * N
        for i in range(N):
            for j in range(N - 1, -1, -1):
                if grid[i][j] == 1:
                    break
                row_zeroes_count[i] += 1

        swaps = 0

        for i in range(N):
            need = N - i - 1
            j = i
            while j < N and row_zeroes_count[j] < need:
                j += 1

            if j == N:
                return -1

            swaps += j - i

            while j > i:
                [row_zeroes_count[j], row_zeroes_count[j - 1]] = [
                    row_zeroes_count[j - 1],
                    row_zeroes_count[j],
                ]
                j -= 1

        return swaps

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1536. Minimum Swaps to Arrange a Binary Grid - https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/description/?envType=daily-question&envId=2026-03-02

    testcase = [
        [
            [[0, 0, 1], [1, 1, 0], [1, 0, 0]],
            3,
        ],
        [
            [[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]],
            -1,
        ],
        [
            [[1, 0, 0], [1, 1, 0], [1, 1, 1]],
            0,
        ],
    ]

    for line in testcase:
        [grid, expected] = line
        s1 = Solution1()
        result = s1.minSwaps(grid)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxWater(self, arr: List[int]) -> int:
        # code here
        # water will get trapped above the block
        # if a block has support on left and right
        # else it cant store water
        # amount of water which can be trapped depends on left and right support
        # for any block b we have to find largest on left and right
        # among these whichever is low will be the amount of water we can store here

        n = len(arr)

        if n < 3:
            return 0

        # arrays to store largest on left and right
        left_max = [0] * n
        right_max = [0] * n

        # fill left_max
        left_max[0] = arr[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], arr[i])

        # fill right_max
        right_max[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], arr[i])

        water = 0

        # calculate trapped water
        for i in range(n):
            water += min(left_max[i], right_max[i]) - arr[i]

        return water

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Trapping Rain Water - https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1

    testcase = [
        [[3, 0, 1, 0, 4, 0, 2], 10],
        [[3, 0, 2, 0, 4], 7],
        [[1, 2, 3, 4], 0],
        [[2, 1, 5, 3, 1, 0, 4], 9],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.maxWater(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 2 of February 2026

    p1()

    p2()
