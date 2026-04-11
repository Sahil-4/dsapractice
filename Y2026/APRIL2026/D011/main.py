from typing import List


class Solution1:
    MAX_DIST = 10**9

    def minDistanceContiguous(self, arr: List[int]) -> int:
        N = len(arr)

        mdist = self.MAX_DIST

        for index in range(N - 2):
            i = arr[index + 0]
            j = arr[index + 1]
            k = arr[index + 2]

            dist = abs(i - j) + abs(j - k) + abs(k - i)
            mdist = min(mdist, dist)

        return mdist

    def minimumDistance(self, nums: List[int]) -> int:

        N = len(nums)

        mp = {}
        for i in range(N):
            if nums[i] not in mp:
                mp[nums[i]] = []
            mp[nums[i]].append(i)

        mdist = self.MAX_DIST
        for _, v in mp.items():
            if len(v) < 3:
                continue

            dist = self.minDistanceContiguous(v)
            mdist = min(mdist, dist)

        return mdist if mdist != self.MAX_DIST else -1

        # Complexity analysis:
        # Time : O(N + M)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3741. Minimum Distance Between Three Equal Elements II - https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/description/?envType=daily-question&envId=2026-04-11

    testcase = [
        [[1, 2, 1, 1, 3], 6],
        [[1, 1, 2, 3, 2, 1, 2], 8],
        [[1], -1],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.minimumDistance(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countIncreasing(self, arr):
        # code here.

        N = len(arr)

        count = 0
        length = 1

        for i in range(1, N):
            if arr[i] > arr[i - 1]:
                length += 1
            else:
                count += (length * (length - 1)) // 2
                length = 1

        count += (length * (length - 1)) // 2

        return count

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count increasing Subarrays - https://www.geeksforgeeks.org/problems/count-increasing-subarrays5301/1

    testcase = [
        [[1, 4, 5, 3, 7, 9], 6],
        [[1, 3, 3, 2, 3, 5], 4],
        [[2, 2, 2, 2], 0],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.countIncreasing(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 11 of April 2026

    p1()

    p2()
