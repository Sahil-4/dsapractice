from collections import deque
from typing import List


class Solution1:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M = len(nums2)

        i = 0
        j = 0

        while i < N and j < M:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return -1

        # Complexity analysis
        # Time : O(N + M)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2540. Minimum Common Value - https://leetcode.com/problems/minimum-common-value/description/?envType=daily-question&envId=2026-05-19

    testcase = [
        [[1, 2, 3], [2, 4], 2],
        [[1, 2, 3, 6], [2, 3, 4, 5], 2],
    ]

    for line in testcase:
        [nums1, nums2, expected] = line
        s1 = Solution1()
        result = s1.getCommon(nums1, nums2)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minSteps(self, arr: list[int], start: int, end: int) -> int:
        # code here

        T = 1000

        if start == end:
            return 0

        dist = [-1] * T
        dist[start] = 0

        queue = deque([start])

        while queue:
            curr = queue.popleft()

            for multiplier in arr:
                next_val = (curr * multiplier) % T

                if dist[next_val] == -1:  # not visited
                    dist[next_val] = dist[curr] + 1

                    if next_val == end:
                        return dist[next_val]

                    queue.append(next_val)

        return -1

        # Complexity analysis
        # Time : O(N)
        # Space : O(T)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Multiplications to reach End - https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1

    testcase = [
        [[2, 5, 7], 3, 30, 2],
        [[3, 4, 65], 7, 175, 4],
    ]

    for line in testcase:
        [arr, start, end, expected] = line
        s2 = Solution2()
        result = s2.minSteps(arr, start, end)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 19 of May 2026

    p1()

    p2()
