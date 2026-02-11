from typing import List


class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.minBalance = [0] * (4 * n)
        self.maxBalance = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    # push lazy value down
    def _push(self, node: int, start: int, end: int):
        if self.lazy[node] != 0:
            val = self.lazy[node]

            self.minBalance[node] += val
            self.maxBalance[node] += val

            if start != end:
                self.lazy[node * 2] += val
                self.lazy[node * 2 + 1] += val

            self.lazy[node] = 0

    # range add
    def update(self, node: int, start: int, end: int, l: int, r: int, val: int):
        self._push(node, start, end)

        if start > r or end < l:
            return

        if l <= start and end <= r:
            self.lazy[node] += val
            self._push(node, start, end)
            return

        mid = (start + end) // 2

        self.update(node * 2, start, mid, l, r, val)
        self.update(node * 2 + 1, mid + 1, end, l, r, val)

        self.minBalance[node] = min(
            self.minBalance[node * 2], self.minBalance[node * 2 + 1]
        )
        self.maxBalance[node] = max(
            self.maxBalance[node * 2], self.maxBalance[node * 2 + 1]
        )

    # find leftmost index where balance == 0
    def getLeftMost(self, node: int, start: int, end: int) -> int:
        self._push(node, start, end)

        if self.minBalance[node] > 0 or self.maxBalance[node] < 0:
            return -1

        if start == end:
            return start if self.minBalance[node] == 0 else -1

        mid = (start + end) // 2

        left = self.getLeftMost(node * 2, start, mid)
        if left != -1:
            return left

        return self.getLeftMost(node * 2 + 1, mid + 1, end)


class Solution1:
    def longestBalanced(self, nums: List[int]) -> int:
        N = len(nums)

        prevIndex = {}
        st = SegmentTree(N)

        maxlen = 0

        for i, num in enumerate(nums):
            val = 1 if num % 2 == 0 else -1

            # remove old contribution
            if num in prevIndex:
                prev = prevIndex[num]
                st.update(1, 0, N - 1, 0, prev, -val)

            # add new contribution
            st.update(1, 0, N - 1, 0, i, val)

            prevIndex[num] = i

            left = st.getLeftMost(1, 0, N - 1)
            if left != -1 and left <= i:
                maxlen = max(maxlen, i - left + 1)

        return maxlen

        # Complexity analysis
        # Time  : O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3721. Longest Balanced Subarray II - https://leetcode.com/problems/longest-balanced-subarray-ii/description/?envType=daily-question&envId=2026-02-11

    testcase = [
        [[2, 5, 4, 3], 4],
        [[3, 2, 2, 5, 4], 5],
        [[1, 2, 3, 2], 3],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.longestBalanced(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minCost(self, heights: List[int], costs: List[int]) -> int:
        # convex cost function

        n = len(heights)

        def calculate_cost(th: int) -> int:
            total = 0
            for i in range(n):
                diff = abs(heights[i] - th)
                total += diff * costs[i]
            return total

        low = min(heights)
        high = max(heights)
        min_cost = -1

        while low <= high:
            mid = (low + high) // 2

            c0 = calculate_cost(mid - 1)
            c1 = calculate_cost(mid)
            c2 = calculate_cost(mid + 1)

            if c1 <= c0 and c1 <= c2:
                min_cost = c1
                break
            elif c0 >= c1 and c1 >= c2:
                low = mid + 1
            else:
                high = mid - 1

        return min_cost

        # Complexity analysis
        # Time : O(Log(max(heights)) * N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Equalize the Towers - https://www.geeksforgeeks.org/problems/equalize-the-towers2804/1

    testcase = [
        [[1, 2, 3], [10, 100, 1000], 120],
        [[7, 1, 5], [1, 1, 1], 6],
    ]

    for line in testcase:
        [heights, costs, expected] = line
        s2 = Solution2()
        result = s2.minCost(heights, costs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 11 of February 2026

    p1()

    p2()
