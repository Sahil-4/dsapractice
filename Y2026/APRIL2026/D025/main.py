from bisect import bisect_left
from typing import List


class Solution1:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # Flatten square boundary into 1D
        arr = []

        for x, y in points:
            if x == 0:
                arr.append(y)
            elif y == side:
                arr.append(side + x)
            elif x == side:
                arr.append(3 * side - y)
            else:
                arr.append(4 * side - x)

        arr.sort()
        perimeter = 4 * side

        # feasibility check
        def can_place(dist: int) -> bool:
            n = len(arr)

            for i in range(n):
                count = 1
                last = arr[i]
                limit = arr[i] + perimeter - dist

                curr = last

                while count < k:
                    idx = bisect_left(arr, curr + dist)
                    if idx == n or arr[idx] > limit:
                        break

                    curr = arr[idx]
                    count += 1

                if count == k:
                    return True

            return False

        # binary search
        lo, hi = 1, side
        ans = 0

        while lo <= hi:
            mid = (lo + hi) // 2

            if can_place(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans

        # Complexity analysis
        # Time : O(N * log(N) * log(S))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3464. Maximize the Distance Between Points on a Square - https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/description/?envType=daily-question&envId=2026-04-25

    testcase = [
        [2, [[0, 2], [2, 0], [2, 2], [0, 0]], 4, 2],
        [2, [[0, 0], [1, 2], [2, 0], [2, 2], [2, 1]], 4, 1],
        [2, [[0, 0], [0, 1], [0, 2], [1, 2], [2, 0], [2, 2], [2, 1]], 5, 1],
    ]
    for line in testcase:
        side, points, k, expected = line
        s1 = Solution1()
        result = s1.maxDistance(side, points, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def reducePairs(self, arr: List[int]) -> List[int]:
        # code here

        def is_negative(a: int) -> bool:
            return a < 0

        final_arr = []

        for num in arr:
            # potential candidate to insert into final_arr
            candidate = num

            while final_arr and is_negative(final_arr[-1]) != is_negative(candidate):
                prev = final_arr.pop()
                if abs(prev) == abs(candidate):
                    candidate = None
                    break
                elif abs(prev) > abs(candidate):
                    candidate = prev
                else:
                    candidate = candidate

            if isinstance(candidate, int):
                final_arr.append(candidate)

        return final_arr

        # Complexity analysis
        # Time : O(2N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Opposite Sign Pair Reduction - https://www.geeksforgeeks.org/problems/asteroid-collision/1

    testcase = [
        [[10, -5, -8, 2, -5], [10]],
        [[5, -5, -2, -10], [-2, -10]],
        [[-20, 1, 20], []],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.reducePairs(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 25 of April 2026

    p1()

    p2()
