class Solution1:
    def minimizeSum(self, nums: list[int]) -> int:
        nums = sorted(nums)

        # changing two elements can always make the low score 0 (copy a value onto
        # another element), so only the high score = max - min matters.
        # Remove two elements from the extremes of the sorted array :
        # two smallest, one smallest + one largest, or two largest
        return min(
            nums[-1] - nums[2],
            nums[-2] - nums[1],
            nums[-3] - nums[0],
        )

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2567. Minimum Score by Changing Two Elements - https://leetcode.com/problems/minimum-score-by-changing-two-elements/description/?envType=daily-question&envId=2026-11-19

    testcase = [
        [[1, 4, 3], 0],
        [[1, 4, 7, 8, 5], 3],
        [[5, 5, 5], 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minimizeSum(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def sortIt(self, arr: list[int]) -> list[int]:
        # odd numbers first in descending order, then even numbers in ascending order
        # key : (is_even, -value for odd / value for even)
        arr.sort(key=lambda x: (x % 2 == 0, x if x % 2 == 0 else -x))

        return arr

        # Complexity analysis
        # Time : O(N Log(N))
        # Space : O(1) extra, in place


def p2():
    # Problem 2 : POTD Geeksforgeeks Sort in Specific Order - https://www.geeksforgeeks.org/problems/sort-in-specific-order2422/1

    testcase = [
        [[1, 2, 3, 5, 4, 7, 10], [7, 5, 3, 1, 2, 4, 10]],
        [[0, 4, 5, 3, 7, 2, 1], [7, 5, 3, 1, 0, 2, 4]],
        [[2, 2, 3, 3], [3, 3, 2, 2]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.sortIt(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)

        # dp[j] : LCS of text1[:i] and text2[:j], rolled over i
        dp = [0] * (M + 1)

        for i in range(1, N + 1):
            diagonal = 0  # dp[i - 1][j - 1]

            for j in range(1, M + 1):
                above = dp[j]  # dp[i - 1][j]

                if text1[i - 1] == text2[j - 1]:
                    dp[j] = diagonal + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])

                diagonal = above

        return dp[M]

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(M)


def p3():
    # Problem 3 : NC150 Leetcode 1143. Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["abcde", "ace", 3],
        ["abc", "abc", 3],
        ["abc", "def", 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.longestCommonSubsequence(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 19 of November 2026

    p1()

    p2()

    p3()
