class Solution1:
    def sumOfSquares(self, nums: list[int]) -> int:
        N = len(nums)

        total = 0

        # 1-indexed position i is special if i divides N
        for i in range(1, N + 1):
            if N % i == 0:
                total += nums[i - 1] * nums[i - 1]

        return total

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2778. Sum of Squares of Special Elements - https://leetcode.com/problems/sum-of-squares-of-special-elements/description/?envType=daily-question&envId=2026-10-11

    testcase = [
        [[1, 2, 3, 4], 21],
        [[2, 7, 1, 19, 18, 3], 63],
        [[5], 25],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.sumOfSquares(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def sortHalves(self, arr: list[int]) -> list[int]:
        # code here

        N = len(arr)

        # break point : first index where the order drops
        split = N
        for i in range(N - 1):
            if arr[i] > arr[i + 1]:
                split = i + 1
                break

        # already sorted
        if split == N:
            return arr

        # merge [0, split) and [split, N)
        merged = []
        i, j = 0, split

        while i < split and j < N:
            if arr[i] <= arr[j]:
                merged.append(arr[i])
                i += 1
            else:
                merged.append(arr[j])
                j += 1

        merged.extend(arr[i:split])
        merged.extend(arr[j:])

        arr[:] = merged
        return arr

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Sort Two Parts Sorted - https://www.geeksforgeeks.org/problems/sort-the-half-sorted2157/1

    testcase = [
        [[2, 3, 8, -1, 7, 10], [-1, 2, 3, 7, 8, 10]],
        [[-4, 6, 9, -1, 3], [-4, -1, 3, 6, 9]],
        [[10, 20, 30], [10, 20, 30]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.sortHalves(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def numDistinct(self, s: str, t: str) -> int:
        SN = len(s)
        TN = len(t)

        if TN > SN:
            return 0

        # dp[j] = number of distinct subsequences of s[:i] that equal t[:j]
        # empty t is a subsequence of any prefix exactly once
        dp = [0] * (TN + 1)
        dp[0] = 1

        for i in range(SN):
            # iterate j backwards so dp[j - 1] still holds the value of row i - 1
            for j in range(TN, 0, -1):
                if s[i] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[TN]

        # Complexity analysis
        # Time : O(SN * TN)
        # Space : O(TN)


def p3():
    # Problem 3 : NC150 Leetcode 115. Distinct Subsequences - https://leetcode.com/problems/distinct-subsequences/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["rabbbit", "rabbit", 3],
        ["babgbag", "bag", 5],
        ["a", "aa", 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.numDistinct(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 11 of October 2026

    p1()

    p2()

    p3()

