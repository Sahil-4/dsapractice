from typing import List
import math


class Solution1:
    def longestBalanced(self, nums: List[int]) -> int:
        llen = 0
        n = len(nums)

        for si in range(n):
            odds = set()
            evens = set()

            for i in range(si, n):
                if nums[i] % 2:
                    odds.add(nums[i])
                else:
                    evens.add(nums[i])

                if len(odds) == len(evens):
                    llen = max(llen, i - si + 1)

        return llen

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3719. Longest Balanced Subarray I - https://leetcode.com/problems/longest-balanced-subarray-i/description/?envType=daily-question&envId=2026-02-10

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
    def kokoEat(self, arr, k):
        # Code here

        def can_eat(s) -> bool:
            # can eat all piles in k hours with speed s bananas per hour

            hours = 0

            for pile in arr:
                hours += math.ceil(pile / s)

            return hours <= k

        low = 1
        high = max(arr)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            if can_eat(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

        # Complexity analysis
        # Time : O(N * Log(E))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Koko Eating Bananas - https://www.geeksforgeeks.org/problems/koko-eating-bananas/1

    testcase = [
        [[5, 10, 3], 4, 5],
        [[5, 10, 15, 20], 7, 10],
        [[3, 4], 10, 1],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.kokoEat(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 10 of February 2026

    p1()

    p2()
