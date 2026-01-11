from typing import List


class Solution1:
    def nextSmallRight(self, arr, n):
        out = [n - 1] * n
        stk = []

        for i in range(n - 1, -1, -1):
            while stk and arr[stk[-1]] >= arr[i]:
                stk.pop()
            if stk:
                out[i] = stk[-1] - 1
            stk.append(i)

        return out

    def nextSmallLeft(self, arr, n):
        out = [0] * n
        stk = []

        for i in range(n):
            while stk and arr[stk[-1]] >= arr[i]:
                stk.pop()
            if stk:
                out[i] = stk[-1] + 1
            stk.append(i)

        return out

    def largestHistogramRectangleArea(self, heights):
        n = len(heights)
        ns_l = self.nextSmallLeft(heights, n)
        ns_r = self.nextSmallRight(heights, n)

        area = 0
        for i in range(n):
            area = max(area, (ns_r[i] - ns_l[i] + 1) * heights[i])

        return area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        N, M = len(matrix), len(matrix[0])
        dp = [0] * M
        max_area = 0

        for i in range(N):
            for j in range(M):
                if matrix[i][j] == "1":
                    dp[j] += 1
                else:
                    dp[j] = 0

            max_area = max(max_area, self.largestHistogramRectangleArea(dp))

        return max_area

        # Complexity analysis
        # Time: O(N*M)
        # Space: O(M)


def p1():
    # Problem 1 : POTD Leetcode 85. Maximal Rectangle - https://leetcode.com/problems/maximal-rectangle/?envType=daily-question&envId=2026-01-11

    testcase = [
        [
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ],
            6,
        ],
        [
            [
                ["0"],
            ],
            0,
        ],
        [
            [
                ["1"],
            ],
            1,
        ],
    ]

    for line in testcase:
        [matrix, expected] = line
        s1 = Solution1()
        result = s1.maximalRectangle(matrix)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def get_possible_minimum_window(self, s1, s1i, s2, s2i):
        N = len(s1)
        M = len(s2)

        s1j = s1i
        s2j = s2i

        while s1j < N and s2j < M:
            if s1[s1j] == s2[s2j]:
                s2j += 1

            s1j += 1

        return s1[s1i:s1j] if s2j == M else None

    def minWindow_bruteforce(self, s1, s2):
        # Code here
        # find characters of s2 in subarray of s1 in order
        # to get subarray run a loop i from 0 to N
        # and check for valid subarray window for each subarray

        ans = None

        N = len(s1)
        for i in range(N):
            if s1[i] == s2[0]:
                possible_ans = self.get_possible_minimum_window(s1, i, s2, 0)
                if possible_ans and (ans == None or len(possible_ans) < len(ans)):
                    ans = possible_ans

        return ans if ans != None else ""

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(N)

    def minWindow(self, s1, s2):
        # two phase greedy expand then contract
        # first expand the window for valid subarray of s1
        # then contract the subarray from right to minimize the valid window size

        n, m = len(s1), len(s2)
        i = j = 0
        best = ""

        while i < n:
            # forward scan
            if s1[i] == s2[j]:
                j += 1
                if j == m:
                    end = i
                    j -= 1

                    # backward shrink
                    while j >= 0:
                        if s1[i] == s2[j]:
                            j -= 1
                        i -= 1

                    i += 1
                    window = s1[i : end + 1]

                    if not best or len(window) < len(best):
                        best = window

                    j = 0
            i += 1

        return best

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Window Subsequence - https://www.geeksforgeeks.org/problems/minimum-window-subsequence/1

    testcase = [
        ["geeksforgeeks", "eksrg", "eksforg"],
        ["abcdebdde", "bde", "bcde"],
        ["ad", "b", ""],
    ]

    for line in testcase:
        [s1, s2, expected] = line
        sol = Solution2()
        result = sol.minWindow(s1, s2)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 11 of January 2026

    p1()

    p2()
