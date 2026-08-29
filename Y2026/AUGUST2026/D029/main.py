class Solution1:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        N = len(nums)

        pairs = sorted((value, index) for index, value in enumerate(nums))

        i = 0
        while i < N:
            j = i

            while j + 1 < N and pairs[j + 1][0] - pairs[j][0] <= limit:
                j += 1

            values = sorted(pairs[k][0] for k in range(i, j + 1))
            indices = sorted(pairs[k][1] for k in range(i, j + 1))

            for index, value in zip(indices, values):
                nums[index] = value

            i = j + 1

        return nums

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2948. Make Lexicographically Smallest Array by Swapping Elements - https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/description/?envType=daily-question&envId=2026-08-29

    testcase = [
        [[1, 5, 3, 9, 8], 2, [1, 3, 5, 8, 9]],
        [[1, 7, 6, 18, 2, 1], 3, [1, 6, 7, 18, 1, 2]],
        [[1, 7, 28, 19, 10], 3, [1, 7, 28, 19, 10]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.lexicographicallySmallestArray(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countSubsequences(self, s: str, n: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * n

        for ch in s:
            digit = int(ch)
            curr = dp[:]

            curr[digit % n] = (curr[digit % n] + 1) % MOD

            for rem in range(n):
                new_rem = (rem * 10 + digit) % n
                curr[new_rem] = (curr[new_rem] + dp[rem]) % MOD

            dp = curr

        return dp[0]

        # Complexity analysis
        # Time : O(Len(S) × N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count Subsequences Divisible by n - https://www.geeksforgeeks.org/problems/number-of-subsequences-in-a-string-divisible-by-n5947/1

    testcase = [
        ["1234", 4, 4],
        ["330", 6, 4],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.countSubsequences(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 29 of August 2026

    p1()

    p2()
