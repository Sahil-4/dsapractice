from cmath import inf
from typing import List


class Solution1:
    def brute_force(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:

        n = len(landStartTime)
        m = len(waterStartTime)

        res = inf

        for i in range(n):
            for j in range(m):
                land = landStartTime[i] + landDuration[i]
                land_water = max(land, waterStartTime[j]) + waterDuration[j]
                res = min(res, land_water)

                water = waterStartTime[j] + waterDuration[j]
                water_land = max(water, landStartTime[i]) + landDuration[i]
                res = min(res, water_land)

        return res

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(1)

    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:

        def solve(
            start1: List[int],
            duration1: List[int],
            start2: List[int],
            duration2: List[int],
        ) -> int:
            finish1 = inf

            for i in range(len(start1)):
                finish1 = min(finish1, start1[i] + duration1[i])

            finish2 = inf

            for i in range(len(start2)):
                finish2 = min(finish2, max(start2[i], finish1) + duration2[i])

            return finish2

        land_water = solve(landStartTime, landDuration, waterStartTime, waterDuration)
        water_land = solve(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(land_water, water_land)

        # Complexity analysis
        # Time : O(N + M)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3633. Earliest Finish Time for Land and Water Rides I - https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/description/?envType=daily-question&envId=2026-06-02

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
    def sumDiffPairs(self, arr: List[int], k: int):
        # code here

        N = len(arr)

        copy_arr = list(arr)
        copy_arr.sort(reverse=True)

        pairs_sum = 0

        i = 0

        while i < N - 1:
            if copy_arr[i] - copy_arr[i + 1] < k:
                pairs_sum += copy_arr[i]
                pairs_sum += copy_arr[i + 1]
                i += 1

            i += 1

        return pairs_sum

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Pairs with certain difference - https://www.geeksforgeeks.org/problems/pairs-with-specific-difference1533/1

    testcase = [
        [[3, 5, 10, 15, 17, 12, 9], 4, 62],
        [[5, 15, 10, 300], 12, 25],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.sumDiffPairs(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 2 of June 2026

    p1()

    p2()
