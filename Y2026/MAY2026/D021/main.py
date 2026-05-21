from typing import List


class Solution1:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # store all prefixes of arr1 elements
        prefix_set: set[str] = set()
        for num in arr1:
            s = str(num)
            for i in range(1, len(s) + 1):
                prefix_set.add(s[:i])  # at most 9 insertions per number

        max_len = 0
        for num in arr2:
            s = str(num)
            for i in range(1, len(s) + 1):
                if s[:i] in prefix_set:
                    max_len = max(max_len, i)

        return max_len

        # Complexity Analysis
        # Time: O((N + M) * L)
        # Space: O(N * L)


def p1():
    # Problem 1 : POTD Leetcode 3043. Find the Length of the Longest Common Prefix - https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/?envType=daily-question&envId=2026-05-21

    testcase = [
        [[1, 10, 100], [1000], 3],
        [[1, 2, 3], [4, 4, 4], 0],
    ]

    for line in testcase:
        [arr1, arr2, expected] = line
        s1 = Solution1()
        result = s1.longestCommonPrefix(arr1, arr2)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def isBitSet(self, n: int) -> bool:
        # code here
        if n == 0:
            return False
        return n & (n + 1) == 0

        # Complexity Analysis
        # Time : O(1)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Check if All Bits Set - https://www.geeksforgeeks.org/problems/check-set-bits5408/1

    testcase = [
        [7, True],
        [8, False],
        [0, False],
    ]

    for line in testcase:
        [n, expected] = line
        s2 = Solution2()
        result = s2.isBitSet(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 21 of May 2026

    p1()

    p2()
