from typing import List


class Solution1:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # nums = [12,21,45,33,54]
        # nums_mirror = [21,12,54,33,45]
        # i = 0 to i < N - 1
        # j = i + 1 to j < N

        def get_mirror(num) -> int:
            return int(str(num)[::-1])

        N = len(nums)
        T = 10000000
        mdist = T

        seen = dict()
        seen[get_mirror(nums[0])] = 0

        for j in range(1, N):
            if nums[j] in seen:
                mdist = min(mdist, j - seen[nums[j]])

            seen[get_mirror(nums[j])] = j

        return mdist if mdist != T else -1

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3761. Minimum Absolute Distance Between Mirror Pairs - https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/?envType=daily-question&envId=2026-04-17

    testcase = [
        [[12, 21, 45, 33, 54], 1],
        [[120, 21], 1],
        [[21, 120], -1],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.minMirrorPairDistance(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def canFormPalindrome(self, s: str) -> bool:
        # code here
        # there should only be one character with odd frequency

        freq = dict()

        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1

        odds = 0
        for key in freq:
            if freq[key] & 1:
                odds += 1
                if odds > 1:
                    return False

        return True

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Anagram Palindrome - https://www.geeksforgeeks.org/problems/anagram-palindrome4720/1

    testcase = [
        ["baba", True],
        ["geeksogeeks", True],
        ["geeksforgeeks", False],
    ]

    for line in testcase:
        [s, expected] = line
        s2 = Solution2()
        result = s2.canFormPalindrome(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 17 of April 2026

    p1()

    p2()
