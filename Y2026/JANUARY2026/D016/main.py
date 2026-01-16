import heapq
from typing import List


class Solution1:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        # If both side lengths are equal → a square is possible
        # We want the MAX such side length
        # Removing fences means:
        # choose two horizontal fences → gives a vertical side length
        # choose two vertical fences   → gives a horizontal side length

        MOD = 10**9 + 7

        # add boundary fences
        hFences = [1] + hFences + [m]
        vFences = [1] + vFences + [n]

        # all possible horizontal distances
        edges = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                edges.add(abs(hFences[i] - hFences[j]))

        max_area = -1

        # check vertical distances
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                side = abs(vFences[i] - vFences[j])
                if side in edges:
                    max_area = max(max_area, side * side)

        return max_area % MOD if max_area != -1 else -1

        # Complexity analysis
        # Time : O(H^2 * V^2)
        # Space : O(H^2)


def p1():
    # Problem 1 : POTD Leetcode 2975. Maximum Square Area by Removing Fences From a Field - https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/description/?envType=daily-question&envId=2026-01-16

    testcase = [
        [4, 3, [2, 3], [2], 4],
        [6, 7, [2], [4], -1],
    ]

    for line in testcase:
        [m, n, hFences, vFences, expected] = line
        s1 = Solution1()
        result = s1.maximizeSquareArea(m, n, hFences, vFences)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minMen(self, arr):
        # code here
        # walking from hour 0 → n-1
        # at each step:
        # look at all workers who can start covering <= current hour
        # from them,
        # pick the one whose right end is maximum
        # jump to that right end
        # worker += 1
        # repeat
        # Idea: At every step,
        # we choose the worker who extends coverage the farthest among all who can start now thus
        # this guarantees the minimum count

        n = len(arr)

        # build intervals
        intervals = []
        for i, r in enumerate(arr):
            if r != -1:
                left = max(0, i - r)
                right = min(n - 1, i + r)
                intervals.append((left, right))

        # sort by start time
        intervals.sort()

        max_heap = []
        i = 0
        curr = 0
        workers = 0

        while curr <= n - 1:
            # push all intervals that can start before or at curr
            while i < len(intervals) and intervals[i][0] <= curr:
                heapq.heappush(max_heap, -intervals[i][1])
                i += 1

            # no interval can cover current point
            if not max_heap:
                return -1

            # pick interval with farthest reach
            farthest = -heapq.heappop(max_heap)
            workers += 1
            curr = farthest + 1

        return workers

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Number of Workers - https://www.geeksforgeeks.org/problems/minimum-sprinklers/1

    testcase = [
        [[1, 2, 1, 0], 1],
        [[2, 3, 4, -1, 2, 0, 0, -1, 0], -1],
        [[0, 1, 0, -1], -1],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.minMen(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 16 of January 2026

    p1()

    p2()
