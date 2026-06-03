import bisect
from collections import defaultdict
from typing import List


class Solution1:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        def solve(start1, dur1, start2, dur2):
            # earliest possible finish across all first-category rides
            earliest_finish = min(s + d for s, d in zip(start1, dur1))

            # board second ride immediately if open, else wait until it opens
            best = min(max(s, earliest_finish) + d for s, d in zip(start2, dur2))
            return best

        land_then_water = solve(
            landStartTime, landDuration, waterStartTime, waterDuration
        )
        water_then_land = solve(
            waterStartTime, waterDuration, landStartTime, landDuration
        )
        return min(land_then_water, water_then_land)

        # Complexity analysis
        # Time : O(N + M)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3635. Earliest Finish Time for Land and Water Rides II - https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/description/?envType=daily-question&envId=2026-06-03

    testcase = [
        [[2, 8], [4, 1], [6], [3], 9],
        [[5], [3], [1], [10], 14],
    ]

    for line in testcase:
        [landStartTime, landDuration, waterStartTime, waterDuration, expected] = line
        s1 = Solution1()
        result = s1.earliestFinishTime(
            landStartTime, landDuration, waterStartTime, waterDuration
        )
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def freqInRange(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # map each value to its sorted list of positions
        pos = defaultdict(list)
        for index, value in enumerate(arr):
            pos[value].append(index)

        ans = []
        for l, r, x in queries:
            if x not in pos:
                ans.append(0)
                continue

            positions = pos[x]
            # first position >= l
            lo = bisect.bisect_left(positions, l)
            # first position > r
            hi = bisect.bisect_right(positions, r)
            ans.append(hi - lo)

        return ans

        # Complexity analysis
        # Time : O(N + Q * log(K))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Subarray Frequency Count Queries - https://www.geeksforgeeks.org/problems/count-frequency-of-an-element-in-a-given-range/1

    testcase = [
        [
            [1, 2, 1, 3, 1, 2, 3],
            [[0, 4, 1], [2, 5, 2], [1, 6, 3], [0, 6, 5]],
            [3, 1, 2, 0],
        ],
        [[11, 21, 51, 101, 11, 51], [[0, 4, 11], [2, 5, 51]], [2, 2]],
    ]

    for line in testcase:
        [arr, queries, expected] = line
        s2 = Solution2()
        result = s2.freqInRange(arr, queries)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 3 of June 2026

    p1()

    p2()
