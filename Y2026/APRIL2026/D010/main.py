from typing import List


class Solution1:
    def minimumDistance(self, nums: List[int]) -> int:
        MAX_LIMIT = 10000

        m_dist = MAX_LIMIT

        N = len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                if nums[i] != nums[j]:
                    continue
                for k in range(j + 1, N):
                    if nums[j] != nums[k]:
                        continue

                    dist = abs(i - j) + abs(j - k) + abs(k - i)
                    m_dist = min(m_dist, dist)

        return m_dist if m_dist != MAX_LIMIT else -1

        # Complexity analysis
        # Time : O(N^3)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3740. Minimum Distance Between Three Equal Elements I - https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/description/?envType=daily-question&envId=2026-04-10

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
    def find3Numbers(self, arr):
        # Code Here

        N = len(arr)

        left_min = [0] * N
        left_min[0] = arr[0]
        for i in range(1, N):
            left_min[i] = min(left_min[i - 1], arr[i])

        right_max = [N - 1] * N
        right_max[N - 1] = arr[N - 1]
        for i in range(N - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], arr[i])

        for i in range(1, N - 1):
            if left_min[i] < arr[i] and arr[i] < right_max[i]:
                return [left_min[i], arr[i], right_max[i]]

        return []

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Sorted subsequence of size 3 - https://www.geeksforgeeks.org/problems/sorted-subsequence-of-size-3/1

    testcase = [
        [[12, 11, 10, 5, 6, 2, 30], 1],
        [[1, 2, 3, 4], 1],
        [[4, 3, 2, 1], 0],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = None
        out = s2.find3Numbers(arr)
        if expected == 0:
            result = 0 if out == [] else -1
        if expected == 1:
            result = 1 if out != [] and out[0] <= out[1] and out[1] <= out[2] else -1
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 10 of April 2026

    p1()

    p2()
