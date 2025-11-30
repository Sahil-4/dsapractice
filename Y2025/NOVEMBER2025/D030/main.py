from typing import List


class Solution1:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        M = total % p

        if M == 0:
            return 0

        pref = 0
        seen = {0: -1}
        ans = len(nums)

        for i, x in enumerate(nums):
            pref = (pref + x) % p
            target = (pref - M) % p

            if target in seen:
                ans = min(ans, i - seen[target])

            seen[pref] = i

        return ans if ans < len(nums) else -1

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1590. Make Sum Divisible by P - https://leetcode.com/problems/make-sum-divisible-by-p/description/?envType=daily-question&envId=2025-11-30

    testcase = [
        [[3, 1, 4, 2], 6, 1],
        [[6, 3, 5, 2], 9, 2],
        [[1, 2, 3], 3, 0],
    ]

    for line in testcase:
        [nums, p, expected] = line
        s1 = Solution1()
        result = s1.minSubarray(nums, p)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countSubs(self, s):
        # code here
        substrs = set()
        n = len(s)

        for i in range(n):
            for j in range(i, n):
                substrs.add(s[i : j + 1])

        return len(substrs)

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(N*N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count of distinct substrings - https://www.geeksforgeeks.org/problems/count-of-distinct-substrings/1

    testcase = [
        ["ababa", 9],
        ["aaa", 3],
    ]

    for line in testcase:
        [s, expected] = line
        s2 = Solution2()
        result = s2.countSubs(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 30 of November 2025

    p1()

    p2()
