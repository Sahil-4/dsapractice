from typing import List


class Solution1:
    def maxDistance(self, colors: List[int]) -> int:
        # what if I just compare 0th house with N - 1, N - 2 ... house in sequence
        # and take the maximum distance
        # ie. first N-1, then N-2, and so on
        # and then I check N-1th house with 0, 1, ...
        # and do the same

        N = len(colors)

        mdist = 0

        candi1 = 0
        candi2 = N - 1

        for i in range(N):
            if colors[candi1] != colors[N - 1 - i]:
                mdist = max(mdist, N - 1 - i)

            if colors[candi2] != colors[i]:
                mdist = max(mdist, candi2 - i)

        return mdist

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2078. Two Furthest Houses With Different Colors - https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/?envType=daily-question&envId=2026-04-20

    testcase = [
        [[1, 1, 1, 6, 1, 1, 1], 3],
        [[1, 8, 3, 8, 3], 4],
        [[0, 1], 1],
    ]

    for line in testcase:
        [colors, expected] = line
        s1 = Solution1()
        result = s1.maxDistance(colors)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def recursion(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1

        return (n - 1) * (self.recursion(n - 1) + self.recursion(n - 2))

    def derangeCount(self, n: int) -> int:
        # code here
        # f(n) = (n-1) * (f(n-1)+f(n-2))
        # n = 1, output = 0
        # n = 2, output = 1
        # n = 3, output = 2

        # return self.recursion(n)

        if n == 1:
            return 0
        if n == 2:
            return 1

        prev2 = 0
        prev1 = 1

        for i in range(3, n + 1):
            curr = (i - 1) * (prev1 + prev2)
            prev2 = prev1
            prev1 = curr

        return prev1

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count Derangements - https://www.geeksforgeeks.org/problems/dearrangement-of-balls0918/1

    testcase = [
        [1, 0],
        [2, 1],
        [3, 2],
    ]

    for line in testcase:
        [n, expected] = line
        s2 = Solution2()
        result = s2.derangeCount(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 20 of April 2026

    p1()

    p2()
