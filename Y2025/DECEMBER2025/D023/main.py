from typing import List
from bisect import bisect_left, bisect_right


class Solution1:
    def upper_bound(self, events: List[List[int]], x: int, l: int, h: int) -> int:
        ans = h + 1

        while l <= h:
            mid = (l + h) // 2

            if events[mid][0] >= x:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1

        return ans

    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        N = len(events)

        print(events)

        suffix = [0] * N
        suffix[N - 1] = events[N - 1][2]
        for i in range(N - 2, -1, -1):
            suffix[i] = max(events[i][2], suffix[i + 1])

        maxi = 0
        for i in range(N):
            val = events[i][2]
            j = self.upper_bound(events, events[i][1] + 1, i + 1, N - 1)
            if j > i and j < N:
                val += suffix[j]

            maxi = max(maxi, val)

        return maxi

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2054. Two Best Non-Overlapping Events - https://leetcode.com/problems/two-best-non-overlapping-events/description/?envType=daily-question&envId=2025-12-23

    testcase = [
        [
            [
                [1, 3, 2],
                [4, 5, 2],
                [2, 4, 3],
            ],
            4,
        ],
        [
            [
                [1, 3, 2],
                [4, 5, 2],
                [1, 5, 5],
            ],
            5,
        ],
        [
            [
                [1, 5, 3],
                [1, 5, 1],
                [6, 6, 5],
            ],
            8,
        ],
        [
            [
                [66, 97, 90],
                [98, 98, 68],
                [38, 49, 63],
                [91, 100, 42],
                [92, 100, 22],
                [1, 77, 50],
                [64, 72, 97],
            ],
            165,
        ],
    ]

    for line in testcase:
        [events, expected] = line
        s1 = Solution1()
        result = s1.maxTwoEvents(events)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def cntInRange(self, arr, queries):
        # code here
        arr.sort()

        q = len(queries)
        count = [0] * q

        for qi in range(q):
            [a, b] = queries[qi]

            first_a_index = bisect_left(arr, a)
            last_b_index = bisect_right(arr, b)

            count[qi] = last_b_index - first_a_index

        return count

        # Complexity analysis
        # Time : O(N*Log(N)) + O(Q)
        # Space : O(Q)


def p2():
    # Problem 2 : POTD Geeksforgeeks Elements in range [a, b] - https://www.geeksforgeeks.org/problems/find-number-of-elements-in-range-a-b-for-each-query/1

    testcase = [
        [[1, 4, 2, 8, 5], [[1, 4], [3, 6], [0, 10]], [3, 2, 5]],
        [[10, 20, 30, 40, 50], [[5, 15], [25, 45], [10, 50]], [1, 2, 5]],
    ]

    for line in testcase:
        [arr, queries, expected] = line
        s2 = Solution2()
        result = s2.cntInRange(arr, queries)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 23 of December 2025

    p1()

    p2()
