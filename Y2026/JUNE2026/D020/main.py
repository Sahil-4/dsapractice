from typing import List


class Solution1:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions_copy = restrictions

        # restriction (1, 0)
        restrictions_copy.append([1, 0])
        restrictions_copy.sort()

        # restriction (n, n-1)
        if restrictions_copy[-1][0] != n:
            restrictions_copy.append([n, n - 1])

        m = len(restrictions_copy)

        # pass restrictions from left to right
        for i in range(1, m):
            restrictions_copy[i][1] = min(
                restrictions_copy[i][1],
                restrictions_copy[i - 1][1]
                + (restrictions_copy[i][0] - restrictions_copy[i - 1][0]),
            )

        # pass restrictions from right to left
        for i in range(m - 2, 0, -1):
            restrictions_copy[i][1] = min(
                restrictions_copy[i][1],
                restrictions_copy[i + 1][1]
                + (restrictions_copy[i + 1][0] - restrictions_copy[i][0]),
            )

        res = 0
        for i in range(m - 1):
            # maximum height of the buildings between [restrictions_copy[i][0], restrictions_copy[i][1]]
            m_height = (
                (restrictions_copy[i + 1][0] - restrictions_copy[i][0])
                + restrictions_copy[i][1]
                + restrictions_copy[i + 1][1]
            ) // 2

            res = max(res, m_height)

        return res

        # Complexity analysis
        # Time : O(M)
        # Space : O(M)


def p1():
    # Problem 1 : POTD Leetcode 1840. Maximum Building Height - https://leetcode.com/problems/maximum-building-height/description/?envType=daily-question&envId=2026-06-20

    testcase = [
        [5, [[2, 1], [4, 1]], 2],
        [6, [], 5],
        [10, [[5, 3], [2, 5], [7, 4], [10, 3]], 5],
    ]

    for line in testcase:
        [n, restrictions, expected] = line
        s1 = Solution1()
        result = s1.maxBuilding(n, restrictions)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def getLastDigit(self, a: str, b: str) -> int:
        # code here

        # a^0 = 1
        if b == "0":
            return 1

        # only the last digit of a matters
        base = int(a[-1])

        # Find b % 4
        mod = 0
        for digit in b:
            mod = (mod * 10 + int(digit)) % 4

        # cyclicity of last digits is 4
        if mod == 0:
            mod = 4

        return pow(base, mod, 10)

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Last Digit of a^b - https://www.geeksforgeeks.org/problems/find-last-digit-of-ab-for-large-numbers1936/1

    testcase = [
        ["3", "10", 9],
        ["6", "2", 6],
    ]

    for line in testcase:
        [a, b, expected] = line
        s2 = Solution2()
        result = s2.getLastDigit(a, b)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 20 of June 2026

    p1()

    p2()
