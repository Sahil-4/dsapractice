from typing import List
import math


class Solution1:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # process per k
        # using sqrt decomposition + difference array

        MOD = 1000000007
        n = len(nums)

        B = int(math.sqrt(n)) + 1

        # group queries by k
        groups = [[] for _ in range(B)]

        # process queries
        for li, ri, ki, vi in queries:
            if ki < B:
                groups[ki].append((li, ri, vi))
            else:
                idx = li
                while idx <= ri:
                    nums[idx] = (nums[idx] * vi) % MOD
                    idx += ki

        # helper: modular inverse using Fermat's theorem
        def mod_inv(x):
            return pow(x, MOD - 2, MOD)

        # process small k using difference array
        dif = [1] * (n + B)

        for k in range(1, B):
            if not groups[k]:
                continue

            # reset difference array
            for i in range(n + B):
                dif[i] = 1

            # apply queries
            for li, ri, vi in groups[k]:
                dif[li] = (dif[li] * vi) % MOD

                # compute R (first index after last valid)
                R = ((ri - li) // k + 1) * k + li
                dif[R] = (dif[R] * mod_inv(vi)) % MOD

            # propagate using step k
            for i in range(k, n):
                dif[i] = (dif[i] * dif[i - k]) % MOD

            # apply to nums
            for i in range(n):
                nums[i] = (nums[i] * dif[i]) % MOD

        # compute XOR
        nums_xor = 0
        for num in nums:
            nums_xor ^= num

        return nums_xor

        # Complexity analysis
        # Time : O((Q + N) * sqrt(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3655. XOR After Range Multiplication Queries II - https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/description/?envType=daily-question&envId=2026-04-09

    testcase = [
        [[1, 1, 1], [[0, 2, 1, 4]], 4],
        [[2, 3, 1, 5, 4], [[1, 4, 2, 3], [0, 2, 1, 2]], 31],
    ]

    for line in testcase:
        [nums, queries, expected] = line
        s1 = Solution1()
        result = s1.xorAfterQueries(nums, queries)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def intersection(self, a, b):
        # code here

        N = len(a)
        M = len(b)

        intersection_arr = []

        p1 = 0
        p2 = 0

        while p1 < N and p2 < M:

            if a[p1] < b[p2]:
                p1 += 1
            elif a[p1] > b[p2]:
                p2 += 1
            else:
                if not intersection_arr or intersection_arr[-1] != a[p1]:
                    intersection_arr.append(a[p1])
                p1 += 1
                p2 += 1

        return intersection_arr

        # Complexity analysis
        # Time : O(N + M)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Intersection of Two Sorted Arrays - https://www.geeksforgeeks.org/problems/intersection-of-two-sorted-arrays-with-duplicate-elements/1

    testcase = [
        [[1, 1, 2, 2, 2, 4], [2, 2, 4, 4], [2, 4]],
        [[1, 2], [3, 4], []],
        [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
    ]

    for line in testcase:
        [a, b, expected] = line
        s2 = Solution2()
        result = s2.intersection(a, b)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 9 of April 2026

    p1()

    p2()
