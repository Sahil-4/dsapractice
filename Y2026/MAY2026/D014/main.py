from typing import List


class Solution1:
    def isGood(self, nums: List[int]) -> bool:
        copy_nums = nums.copy()
        copy_nums.sort()

        N = len(copy_nums)

        if N < 2:
            return False

        for i in range(N - 1):
            if copy_nums[i] != i + 1:
                return False

        return copy_nums[N - 1] == copy_nums[N - 2]

        # Complexity analysis
        # Time : O(N * Log(N) + N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2784. Check if Array is Good - https://leetcode.com/problems/check-if-array-is-good/description/?envType=daily-question&envId=2026-05-14

    testcase = [
        [[2, 1, 3], False],
        [[1, 3, 3, 2], True],
        [[1, 1], True],
        [[3, 4, 4, 1, 2, 1], False],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.isGood(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def createLPS(self, pattern: list[int]) -> list[int]:
        m = len(pattern)
        lps = [0] * m

        length = 0
        i = 1

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def search(self, a: list[int], b: list[int]) -> list[int]:
        n, m = len(a), len(b)

        lps = self.createLPS(b)

        occurrences = []

        i = 0
        j = 0

        while i < n:
            if a[i] == b[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

            if j == m:
                occurrences.append(i - m)
                j = lps[j - 1]

        return occurrences

        # Complexity analysis
        # Time : O(N + M)
        # Space : O(M)


def p2():
    # Problem 2 : POTD Geeksforgeeks Search for Subarray - https://www.geeksforgeeks.org/problems/search-for-subarray/1

    testcase = [
        [[2, 4, 1, 0, 4, 1, 1], [4, 1], [1, 4]],
        [[2, 4, 1, 0, 0, 3], [0], [3, 4]],
        [[1, 3, 5, 3, 0], [1, 3, 0], []],
    ]

    for line in testcase:
        [a, b, expected] = line
        s2 = Solution2()
        result = s2.search(a, b)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 14 of May 2026

    p1()

    p2()
