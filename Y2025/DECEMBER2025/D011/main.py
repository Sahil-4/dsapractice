import math
from collections import defaultdict
from typing import List


class Solution1:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        mp_x = defaultdict(list)
        mp_y = defaultdict(list)

        # Build lists
        for x, y in buildings:
            mp_x[x].append(y)
            mp_y[y].append(x)

        # Precompute min/max for each x and each y
        min_x = {x: min(vals) for x, vals in mp_x.items()}
        max_x = {x: max(vals) for x, vals in mp_x.items()}
        min_y = {y: min(vals) for y, vals in mp_y.items()}
        max_y = {y: max(vals) for y, vals in mp_y.items()}

        count = 0

        for x, y in buildings:
            # Same logic as C++
            if y == min_x[x] or x == min_y[y]:
                continue
            if y == max_x[x] or x == max_y[y]:
                continue

            count += 1

        return count

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3531. Count Covered Buildings - https://leetcode.com/problems/count-covered-buildings/description/?envType=daily-question&envId=2025-12-11

    testcase = [
        [3, [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]], 1],
        [3, [[1, 1], [1, 2], [2, 1], [2, 2]], 0],
        [5, [[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]], 1],
    ]

    for line in testcase:
        [n, buildings, expected] = line
        s1 = Solution1()
        result = s1.countCoveredBuildings(n, buildings)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def constructArr(self, arr):
        # code here
        # If pair array has only 1 element → original array has 2 elements
        if len(arr) == 1:
            return [1, arr[0] - 1]

        # Compute size of original array
        n = (1 + math.isqrt(1 + 8 * len(arr))) // 2

        res = [0] * n

        # Core formula:
        # a0 = (P0 + P1 - P(k)) / 2
        res[0] = (arr[0] + arr[1] - arr[n - 1]) // 2

        # Next elements: ai = P(i-1) - a0
        for i in range(1, n):
            res[i] = arr[i - 1] - res[0]

        return res

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Construct an array from its pair-sum array - https://www.geeksforgeeks.org/problems/construct-an-array-from-its-pair-sum-array/1

    testcase = [
        [[4, 5, 3], [3, 1, 2]],
        [[3], [1, 2]],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.constructArr(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 11 of December 2025

    p1()

    p2()
