class Solution1:
    def countOdds(self, low: int, high: int) -> int:
        count = (high - low) // 2

        if high & 1 or low & 1:
            count += 1

        return count

        # Complexity analysis
        # Time : O(1)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1523. Count Odd Numbers in an Interval Range - https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/?envType=daily-question&envId=2025-12-07

    testcase = [
        [3, 7, 3],
        [8, 10, 1],
        [1, 5, 3],
        [1, 4, 2],
        [2, 7, 3],
        [2, 8, 3],
        [2, 3, 1],
    ]

    for line in testcase:
        [low, high, expected] = line
        s1 = Solution1()
        result = s1.countOdds(low, high)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def distinctSubseq(self, s):
        # code here
        mod = 1000000007

        n = len(s)

        dp = [0] * (n + 1)

        dp[0] = 1

        last = [-1] * 26

        for i in range(1, n + 1, 1):
            dp[i] = (2 * dp[i - 1]) % mod

            if last[ord(s[i - 1]) - ord("a")] != -1:
                dp[i] = (dp[i] - dp[last[ord(s[i - 1]) - ord("a")]]) % mod

            last[ord(s[i - 1]) - ord("a")] = i - 1

        return dp[n] % mod

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Number of distinct subsequences - https://www.geeksforgeeks.org/problems/number-of-distinct-subsequences0909/1

    testcase = [
        ["gfg", 7],
        ["ggg", 4],
    ]

    for line in testcase:
        [s, expected] = line
        s2 = Solution2()
        result = s2.distinctSubseq(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 7 of December 2025

    p1()

    p2()
