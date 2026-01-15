from typing import List


class Solution1:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        # Idea:
        # find the maximum possible square hole area
        # need the longest consecutive removed horizontal bars
        # and the longest consecutive removed vertical bars
        # finally return the area of square created by these bars

        maxH = maxV = 1
        cntH = cntV = 1

        hBars.sort()
        vBars.sort()

        hBarsLen = len(hBars)
        vBarsLen = len(vBars)

        for i in range(1, hBarsLen):
            if hBars[i] - hBars[i - 1] == 1:
                cntH += 1
                maxH = max(maxH, cntH)
            else:
                cntH = 1

        for i in range(1, vBarsLen):
            if vBars[i] - vBars[i - 1] == 1:
                cntV += 1
                maxV = max(maxV, cntV)
            else:
                cntV = 1

        side = min(maxH + 1, maxV + 1)
        return side * side

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2943. Maximize Area of Square Hole in Grid - https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/description/?envType=daily-question&envId=2026-01-15

    testcase = [
        [2, 1, [2, 3], [2], 4],
        [1, 1, [2], [2], 4],
        [2, 3, [2, 3], [2, 4], 4],
    ]

    for line in testcase:
        [n, m, hBars, vBars, expected] = line
        s1 = Solution1()
        result = s1.maximizeSquareHoleArea(n, m, hBars, vBars)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minCandy(self, arr):
        # Code here
        # use greedy approach here
        # first satisfy condition from left to right (only for left neighbor)
        # then satisfy for right neighbor
        # init candies[i] = 1
        # then in left to right
        # if arr[i] > arr[i - 1]: candies[i] = candies[i-1] + 1
        # then in right to left
        # if arr[i] > arr[i + 1]: candies[i] = max(candies[i], candies[i-1] + 1)

        N = len(arr)

        candies = [1] * N

        for i in range(1, N):
            if arr[i] > arr[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(N - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies, start=0)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Candy - https://www.geeksforgeeks.org/problems/candy/1

    testcase = [
        [[1, 0, 2], 5],
        [[1, 2, 2], 4],
        [[1, 3, 5, 3, 1], 9],
        [[1, 0, 2, 1, 3, 2, 1], 12],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.minCandy(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 15 of January 2026

    p1()

    p2()
