from math import gcd


class Solution1:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 1_000_000_007

        N = len(nums)

        max_element = max(nums)

        prev = [[0] * (max_element + 1) for _ in range(max_element + 1)]

        for first in range(max_element, -1, -1):
            for second in range(max_element, -1, -1):
                both_non_empty = first != 0 and second != 0
                gcd_match = first == second

                prev[first][second] = both_non_empty and gcd_match

        for i in range(N - 1, -1, -1):

            curr = [[0] * (max_element + 1) for _ in range(max_element + 1)]

            for first in range(max_element, -1, -1):
                for second in range(max_element, -1, -1):

                    skip = prev[first][second]

                    take_1 = prev[gcd(first, nums[i])][second]

                    take_2 = prev[first][gcd(second, nums[i])]

                    curr[first][second] = (skip + take_1 + take_2) % MOD

            prev = curr

        return prev[0][0]

        # Complexity analysis
        # Time : O(N * Max(nums) * Max(nums))
        # Space : O(Max(nums) * Max(nums))


def p1():
    # Problem 1 : POTD Leetcode 3336. Find the Number of Subsequences With Equal GCD - https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/description/?envType=daily-question&envId=2026-07-14

    testcase = [
        [[1, 2, 3, 4], 10],
        [[10, 20, 30], 2],
        [[1, 1, 1, 1], 50],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.subsequencePairCount(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def find(self, arr: list[int]) -> int:
        # code here
        need = 0

        for a in reversed(arr):
            need = (need + a + 1) // 2

        return max(1, need)

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Smallest Non-Zero Number - https://www.geeksforgeeks.org/problems/find-smallest-non-zero-number4510/1

    testcase = [
        [[3, 4, 3, 2, 4], 4],
        [[4, 4], 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.find(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 14 of July 2026

    p1()

    p2()
