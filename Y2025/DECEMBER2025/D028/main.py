from typing import List


class Solution1:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # start from top right
        # move either left or bottom
        # while counting number of element below current cell + current cell

        negatives_count = 0

        M = len(grid)
        N = len(grid[0])

        i = 0
        j = N - 1

        while i < M and j >= 0:
            if grid[i][j] >= 0:
                # move down
                i += 1
            else:
                # count this + bottom
                negatives_count += M - i
                j -= 1

        return negatives_count

        # Complexity analysis
        # Time : O(N+M)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1351. Count Negative Numbers in a Sorted Matrix - https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/?envType=daily-question&envId=2025-12-28

    testcase = [
        [[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]], 8],
        [[[3, 2], [1, 0]], 0],
        [[[5, 1, 0], [-5, -5, -5]], 3],
    ]

    for line in testcase:
        [grid, expected] = line
        s1 = Solution1()
        result = s1.countNegatives(grid)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minTime(self, ranks, n):
        def donuts_in_time(T):
            total = 0
            for r in ranks:
                time = 0
                k = 1
                while time + r * k <= T:
                    time += r * k
                    total += 1
                    k += 1
                if total >= n:
                    return True
            return False

        low, high = 0, min(ranks) * n * (n + 1) // 2
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if donuts_in_time(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

        # Complexity analysis
        # Time : O(N * Log(E))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum time to fulfil all orders - https://www.geeksforgeeks.org/problems/minimum-time-to-fulfil-all-orders/1

    testcase = [
        [10, [1, 2, 3, 4], 12],
        [8, [1, 1, 1, 1, 1, 1, 1, 1], 1],
    ]

    for line in testcase:
        [n, ranks, expected] = line
        s2 = Solution2()
        result = s2.minTime(ranks, n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 28 of December 2025

    p1()

    p2()
