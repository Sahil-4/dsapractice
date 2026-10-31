from bisect import bisect_left
import sys

sys.setrecursionlimit(200000)


class Solution1:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 1_000_000_007
        M, N = len(grid), len(grid[0])

        memo_moves = {}

        def get_dest(i: int, j: int, d: int) -> tuple[int, int] | None:
            if i >= M or j >= N:
                return None

            if grid[i][j] == 0:
                return (i, j)

            state = (i, j, d)
            if state in memo_moves:
                return memo_moves[state]

            if d == 0:
                res = get_dest(i + 1, j, 1)
            else:
                res = get_dest(i, j + 1, 0)

            memo_moves[state] = res
            return res

        memo_paths = [[0] * N for _ in range(M)]
        memo_paths[M - 1][N - 1] = 1

        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if i == M - 1 and j == N - 1:
                    continue
                if grid[i][j] == 1:
                    continue

                # move - right
                right = get_dest(i, j + 1, 0)
                if right:
                    ri, rj = right
                    memo_paths[i][j] = (memo_paths[i][j] + memo_paths[ri][rj]) % MOD

                # move - down
                down = get_dest(i + 1, j, 1)
                if down:
                    di, dj = down
                    memo_paths[i][j] = (memo_paths[i][j] + memo_paths[di][dj]) % MOD

        return memo_paths[0][0]

        # Complexity analysis
        # Time : O(M * N)
        # Space : O(M * N)


def p1():
    # Problem 1 : POTD Leetcode 3665. Twisted Mirror Path Count - https://leetcode.com/problems/twisted-mirror-path-count/description/?envType=daily-question&envId=2026-10-31

    testcase = [
        [[[0, 1, 0], [0, 0, 1], [1, 0, 0]], 5],
        [[[0, 0], [0, 0]], 2],
        [[[0, 1, 1], [1, 1, 0]], 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.uniquePaths(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        # code here
        N = len(arr)

        result = 0
        temp_sum = 0
        for i in range(N):
            temp_sum += arr[i]
            if i >= totalTime:
                temp_sum -= arr[i - totalTime]

            result = max(result, temp_sum)

        return result

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Maximum Packages within Time - https://www.geeksforgeeks.org/problems/bird-and-maximum-fruit-gathering0509/1

    testcase = [
        [[2, 1, 3, 5, 0, 1, 4], 3, 9],
        [[1, 6, 2, 5, 3, 4], 2, 8],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxPackages(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        N = len(numbers)

        for i in range(N):
            need = target - numbers[i]

            # find need in search space numbers[i + 1: ]
            # if found return [i, xi]

            xi = bisect_left(numbers, need, lo=i + 1, hi=N - 1)

            if xi < N and numbers[xi] == need:
                return [i + 1, xi + 1]

        return [-1, -1]

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 167. Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[2, 7, 11, 15], 9, [1, 2]],
        [[2, 3, 4], 6, [1, 3]],
        [[-1, 0], -1, [1, 2]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.twoSum(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 31 of October 2026

    p1()

    p2()

    p3()
