from collections import defaultdict
from typing import List


class Solution1:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        NN = len(nums)
        QN = len(queries)

        answer = [-1] * NN

        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)

        for v in pos:
            indices = pos[v]
            k = len(indices)

            if k == 1:
                continue

            for i in range(k):
                _curr = indices[i]
                _prev = indices[(i - 1) % k]
                _next = indices[(i + 1) % k]

                d1 = abs(_curr - _prev)
                d1 = min(d1, NN - d1)

                d2 = abs(_curr - _next)
                d2 = min(d2, NN - d2)

                answer[_curr] = min(d1, d2)

        return [answer[q] for q in queries]

        # Complexity analysis
        # Time : O(N + Q)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3488. Closest Equal Element Queries - https://leetcode.com/problems/closest-equal-element-queries/description/?envType=daily-question&envId=2026-04-16

    testcase = [
        [[1, 3, 1, 4, 1, 3, 2], [0, 3, 5], [2, -1, 3]],
        [[1, 2, 3, 4], [0, 1, 2, 3], [-1, -1, -1, -1]],
    ]

    for line in testcase:
        [nums, queries, expected] = line
        s1 = Solution1()
        result = s1.solveQueries(nums, queries)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def myAtoi(self, s: str) -> int:
        # code here

        MIN_LIMIT = -2147483648
        MAX_LIMIT = 2147483647

        num = 0
        sign = +1

        s = s.lstrip()

        for c in s:

            if c == "+":
                sign = +1
            elif c == "-":
                sign = -1
            elif c.isdigit():
                num = num * 10 + int(c)
            else:
                break

            if (num * sign) < MIN_LIMIT:
                return MIN_LIMIT

            if (num * sign) > MAX_LIMIT:
                return MAX_LIMIT

        return num * sign

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Implement Atoi - https://www.geeksforgeeks.org/problems/implement-atoi/1

    testcase = [
        ["-123", -123],
        [" -", 0],
        [" 1231231231311133", 2147483647],
        ["-999999999999", -2147483648],
        ["  -0012gfg4", -12],
    ]

    for line in testcase:
        [s, expected] = line
        s2 = Solution2()
        result = s2.myAtoi(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 16 of April 2026

    p1()

    p2()
