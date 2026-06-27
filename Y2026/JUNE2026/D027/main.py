from collections import Counter


class Solution1:
    def maximumLength(self, nums: list[int]) -> int:
        frequency = Counter(nums)

        frequency_one = frequency.get(1, 0)
        ans = frequency_one if frequency_one & 1 else frequency_one - 1

        frequency.pop(1, None)

        for num in frequency:

            res = 0
            x = num

            while x in frequency and frequency[x] > 1:
                res += 2
                x *= x

            ans = max(ans, res + (1 if x in frequency else -1))

        return ans

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3020. Find the Maximum Number of Elements in Subset - https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/description/?envType=daily-question&envId=2026-06-27

    testcase = [
        [[5, 4, 1, 2, 2], 3],
        [[1, 3, 2, 4], 1],
        [[1, 1], 1],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.maximumLength(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countWays(self, n: int, m: int) -> int:
        # Code here

        MOD = 1000000007

        dp = [0] * (n + 1)

        for i in range(n + 1):

            if i < m:
                dp[i] = 1
            elif i == m:
                dp[i] = 2
            else:
                dp[i] = (dp[i - 1] + dp[i - m]) % MOD

        return dp[n]

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Ways to Tile the Floor - https://www.geeksforgeeks.org/problems/count-the-number-of-ways-to-tile-the-floor-of-size-n-x-m-using-1-x-m-size-tiles0509/1

    testcase = [
        [4, 4, 2],
        [2, 3, 1],
    ]

    for line in testcase:
        [n, m, expected] = line
        s2 = Solution2()
        result = s2.countWays(n, m)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 27 of June 2026

    p1()

    p2()
