from typing import List


class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)

        low = 0
        high = N - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:  # left half is sorted
                if nums[low] <= target < nums[mid]:  # target is in the left half
                    high = mid - 1
                else:  # target is in the right half
                    low = mid + 1

            else:  # right half is sorted
                if nums[mid] < target <= nums[high]:  # target is in the right half
                    low = mid + 1
                else:  # target is in the left half
                    high = mid - 1

        return -1

        # Complexity Analysis:
        # Time : O(Log(N))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 33. Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=daily-question&envId=2026-05-22

    testcase = [
        [[4, 5, 6, 7, 0, 1, 2], 0, 4],
        [[4, 5, 6, 7, 0, 1, 2], 3, -1],
        [[1], 0, -1],
    ]

    for line in testcase:
        [nums, target, expected] = line
        s1 = Solution1()
        result = s1.search(nums, target)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def cntOnes(self, grid: List[List[int]]) -> int:
        # code here

        N = len(grid)
        M = len(grid[0])

        visited = [[False] * M for _ in range(N)]
        copy_grid = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                copy_grid[i][j] = grid[i][j]

        def is_boundary(x: int, y: int) -> bool:
            return x == 0 or x == N - 1 or y == 0 or y == M - 1

        def can_move(x: int, y: int) -> bool:
            check = True
            check = check and 0 <= x < N and 0 <= y < M
            check = check and not visited[x][y]
            check = check and copy_grid[x][y] == 1
            return check

        def dfs(x: int, y: int) -> None:
            visited[x][y] = True
            copy_grid[x][y] = 0

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if can_move(new_x, new_y):
                    dfs(new_x, new_y)

        for i in range(N):
            for j in range(M):
                if is_boundary(i, j) and copy_grid[i][j] == 1 and not visited[i][j]:
                    dfs(i, j)

        count = 0
        for i in range(N):
            for j in range(M):
                if copy_grid[i][j] == 1:
                    count += 1

        return count

        # Complexity Analysis:
        # Time : O(N*M)
        # Space : O(N*M)


def p2():
    # Problem 2 : POTD Geeksforgeeks 1s Surrounded by 0s - https://www.geeksforgeeks.org/problems/1s-surrounded-by-0s/1

    testcase = [
        [
            [
                [0, 0, 0, 0],
                [1, 0, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0],
            ],
            3,
        ],
        [
            [
                [1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 1, 0],
                [0, 0, 0, 1, 1, 0],
                [0, 0, 0, 1, 1, 0],
                [0, 1, 0, 1, 0, 0],
                [1, 1, 0, 0, 0, 1],
            ],
            6,
        ],
    ]

    for line in testcase:
        [grid, expected] = line
        s2 = Solution2()
        result = s2.cntOnes(grid)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 22 of May 2026

    p1()

    p2()
