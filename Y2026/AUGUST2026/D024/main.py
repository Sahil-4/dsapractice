class Solution1:
    def stoneGameVIII(self, stones: list[int]) -> int:
        N = len(stones)

        # calculate prefix sums
        prefix_sum = 0
        prefix = [0] * N

        for i in range(N):
            prefix_sum += stones[i]
            prefix[i] = prefix_sum

        # base case: dp[N - 1]
        dp = prefix[N - 1]

        # calculate dp[i] from right to left
        for i in range(N - 2, 0, -1):
            take = prefix[i] - dp
            skip = dp

            dp = max(take, skip)

        return dp

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1872. Stone Game VIII - https://leetcode.com/problems/stone-game-viii/description/?envType=daily-question&envId=2026-08-24

    testcase = [
        [[-1, 2, -3, 4, -5], 5],
        [[7, -6, 5, 10, 5, -2, -6], 13],
        [[-10, -12], -22],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.stoneGameVIII(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def prefixStrings(self, n: int) -> int:
        # code here

        MOD = 10**9 + 7

        # calculate (2n)!
        fact = 1
        for i in range(1, 2 * n + 1):
            fact = (fact * i) % MOD

        # calculate n!
        fact_n = 1
        for i in range(1, n + 1):
            fact_n = (fact_n * i) % MOD

        # calculate (n + 1)!
        fact_n1 = (fact_n * (n + 1)) % MOD

        # modular inverse using `Fermat's Little Theorem`
        inv_fact_n = pow(fact_n, MOD - 2, MOD)
        inv_fact_n1 = pow(fact_n1, MOD - 2, MOD)

        # catalan number
        # (2n)! / (n! * (n+1)!)
        ans = fact
        ans = (ans * inv_fact_n) % MOD
        ans = (ans * inv_fact_n1) % MOD

        return ans

        # Complexity analysis
        # Time : O(2N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count Prefix-Balanced Binary Strings - https://www.geeksforgeeks.org/problems/geek-and-his-binary-strings1951/1

    testcase = [
        [2, 2],
        [3, 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.prefixStrings(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 24 of August 2026

    p1()

    p2()
