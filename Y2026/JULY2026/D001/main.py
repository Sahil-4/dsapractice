from collections import deque


class Solution1:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        grid_size = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # compute distance of every cell from the nearest thief
        distance_to_nearest_thief = [[-1] * grid_size for _ in range(grid_size)]
        visited = [[False] * grid_size for _ in range(grid_size)]
        queue = deque()

        for row in range(grid_size):
            for col in range(grid_size):
                if grid[row][col] == 1:
                    queue.append((row, col))
                    visited[row][col] = True

        distance = 0

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                current_row, current_col = queue.popleft()
                distance_to_nearest_thief[current_row][current_col] = distance

                for row_offset, col_offset in directions:
                    next_row = current_row + row_offset
                    next_col = current_col + col_offset

                    if (
                        next_row < 0
                        or next_row >= grid_size
                        or next_col < 0
                        or next_col >= grid_size
                        or visited[next_row][next_col]
                    ):
                        continue

                    visited[next_row][next_col] = True
                    queue.append((next_row, next_col))

            distance += 1

        # check if a path exists with minimum safeness >= target
        def can_reach_destination(required_safeness: int) -> bool:
            if distance_to_nearest_thief[0][0] < required_safeness:
                return False

            queue = deque([(0, 0)])
            visited = [[False] * grid_size for _ in range(grid_size)]
            visited[0][0] = True

            while queue:
                current_row, current_col = queue.popleft()

                if current_row == grid_size - 1 and current_col == grid_size - 1:
                    return True

                for row_offset, col_offset in directions:
                    next_row = current_row + row_offset
                    next_col = current_col + col_offset

                    if (
                        next_row < 0
                        or next_row >= grid_size
                        or next_col < 0
                        or next_col >= grid_size
                        or visited[next_row][next_col]
                    ):
                        continue

                    if (
                        distance_to_nearest_thief[next_row][next_col]
                        < required_safeness
                    ):
                        continue

                    visited[next_row][next_col] = True
                    queue.append((next_row, next_col))

            return False

        # binary search for the maximum possible safeness factor
        left = 0
        right = 400
        maximum_safeness = 0

        while left <= right:
            middle = left + (right - left) // 2

            if can_reach_destination(middle):
                maximum_safeness = middle
                left = middle + 1
            else:
                right = middle - 1

        return maximum_safeness

        # Complexity analysis
        # Time : O(N*N * Log(N))
        # Space : O(N*N)


def p1():
    # Problem 1 : POTD Leetcode 2812. Find the Safest Path in a Grid - https://leetcode.com/problems/find-the-safest-path-in-a-grid/description/?envType=daily-question&envId=2026-07-01

    testcase = [
        [[[1, 0, 0], [0, 0, 0], [0, 0, 1]], 0],
        [[[0, 0, 1], [0, 0, 0], [0, 0, 0]], 2],
        [[[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]], 2],
    ]

    for line in testcase:
        [grid, expected] = line
        s1 = Solution1()
        result = s1.maximumSafenessFactor(grid)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxSumSubarray(self, arr: list) -> int:
        # code here

        N = len(arr)

        # maximum subarray sum ending at index i (kadane left to right)
        prefix = [0] * N

        # maximum subarray sum starting at index i (kadane right to left)
        suffix = [0] * N

        prefix[0] = arr[0]
        for i in range(1, N):
            prefix[i] = max(arr[i], prefix[i - 1] + arr[i])

        suffix[N - 1] = arr[N - 1]
        for i in range(N - 2, -1, -1):
            suffix[i] = max(arr[i], suffix[i + 1] + arr[i])

        # maximum subarray sum without deletion
        ans = max(prefix)

        # try removing each element
        for i in range(1, N - 1):
            ans = max(ans, prefix[i - 1] + suffix[i + 1])

        return ans

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Subarray Sum by Removing At Most One - https://www.geeksforgeeks.org/problems/max-sum-subarray-by-removing-at-most-one-element/1

    testcase = [
        [[1, 2, 3, -4, 5], 11],
        [[-2, -3, 4, -1, -2, 1, 5, -3], 9],
        [[-1, -1, -1, -1], -1],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.maxSumSubarray(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 1 of July 2026

    p1()

    p2()
