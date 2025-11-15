class Solution1:
    def one_dominant(self, ones_count: int, zero_count: int) -> bool:
        return ones_count >= (zero_count * zero_count)

    def solve1(self, s: str) -> int:
        slen = len(s)
        count: int = 0

        for i in range(slen):
            ones_count = 0
            zero_count = 0

            for j in range(i, slen):
                ones_count += 1 if s[j] == "1" else 0
                zero_count += 1 if s[j] == "0" else 0

                count += 1 if self.one_dominant(ones_count, zero_count) else 0

        return count

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(1)

    def solve2(self, s: str) -> int:
        n = len(s)
        pre = [-1] * (n + 1)
        for i in range(n):
            if i == 0 or s[i - 1] == "0":
                pre[i + 1] = i
            else:
                pre[i + 1] = pre[i]

        count = 0
        for i in range(1, n + 1):
            cnt0 = 1 if s[i - 1] == "0" else 0
            j = i
            while j > 0 and cnt0 * cnt0 <= n:
                cnt1 = (i - pre[j]) - cnt0
                if cnt0 * cnt0 <= cnt1:
                    count += min(j - pre[j], cnt1 - cnt0 * cnt0 + 1)
                j = pre[j]
                cnt0 += 1

        return count

        # Complexity analysis
        # Time : O(N*sqrt(N))
        # Space : O(N)

    def numberOfSubstrings(self, s: str) -> int:
        # return self.solve1(s)

        return self.solve2(s)


def p1():
    # Problem 1 : POTD Leetcode 3234. Count the Number of Substrings With Dominant Ones - https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/description/?envType=daily-question&envId=2025-11-15

    testcases = ["00011", "101101"]
    s1 = Solution1()

    for testcase in testcases:
        out = s1.numberOfSubstrings(testcase)
        print(out)


class Solution2:
    T = int(1e9)

    def recursion(self, s, e, cuts_set):
        if s >= e:
            return 0

        min_cost = self.T

        for ci in range(s + 1, e, 1):
            if ci in cuts_set:
                left = self.recursion(s, ci, cuts_set)
                right = self.recursion(ci, e, cuts_set)
                mid = e - s
                joined_cost = left + mid + right
                min_cost = min(min_cost, joined_cost)

        return 0 if min_cost == self.T else min_cost

    def memoize(self, s, e, cuts_set, memo):
        if s >= e:
            return 0

        if memo[s][e] != -1:
            return memo[s][e]

        min_cost = self.T

        for ci in range(s + 1, e, 1):
            if ci in cuts_set:
                left = self.memoize(s, ci, cuts_set, memo)
                right = self.memoize(ci, e, cuts_set, memo)
                mid = e - s
                joined_cost = left + mid + right
                min_cost = min(min_cost, joined_cost)

        memo[s][e] = 0 if min_cost == self.T else min_cost
        return memo[s][e]

        # Complexity analysis
        # Time : O(2 * N * N * M)
        # Space : O(N * N) + O(N)

    def tabulation(self, n, cuts):
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)

        dp = [[0.0] * m for _ in range(m)]

        for length in range(2, m):
            for i in range(0, m - length):
                j = i + length
                dp[i][j] = float("inf")

                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + (cuts[j] - cuts[i])
                    dp[i][j] = min(dp[i][j], cost)

        return dp[0][m - 1]

        # Complexity analysis
        # Time : O(M * M * N)
        # Space : O(M * M)

    def minCutCost(self, n, cuts):
        # code here
        # cuts_set = set(cuts)
        # return self.recursion(0, n, cuts_set)

        # memo = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        # return self.memoize(0, n, cuts_set, memo)

        return self.tabulation(n, cuts)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Cost to Cut a Stick of length N - https://www.geeksforgeeks.org/problems/minimum-cost-to-cut-a-stick-of-length-n/1

    testcases = [
        {"n": 8, "cuts": [1, 6, 3, 5]},
        {"n": 10, "cuts": [2, 4, 7]},
    ]
    for testcase in testcases:
        s2 = Solution2()
        out = s2.minCutCost(testcase.get("n"), testcase.get("cuts"))
        print(out)


if __name__ == "__main__":
    # Day 15 of November 2025

    p1()

    p2()
