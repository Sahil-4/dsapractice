class Solution1:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        def kmp(pattern: str, word: str) -> bool:
            m = len(pattern)
            n = len(word)

            # prefix array of the pattern
            pi = [0] * m
            j = 0
            for i in range(1, m):
                while j and pattern[i] != pattern[j]:
                    j = pi[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                pi[i] = j

            # matching
            j = 0
            for i in range(n):
                while j and word[i] != pattern[j]:
                    j = pi[j - 1]
                if word[i] == pattern[j]:
                    j += 1
                if j == m:
                    return True

            return False

        count = 0
        for pattern in patterns:
            count += kmp(pattern, word)

        return count

        # Complexity analysis
        # Time : O(N*K + sum(m))
        # Space : O(max(m))


def p1():
    # Problem 1 : POTD Leetcode 1967. Number of Strings That Appear as Substrings in Word - https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/description/?envType=daily-question&envId=2026-06-29

    testcase = [
        [["a", "abc", "bc", "d"], "abc", 3],
        [["a", "b", "c"], "aaaaabbbbb", 2],
        [["a", "a", "a"], "ab", 3],
    ]

    for line in testcase:
        [patterns, word, expected] = line
        s1 = Solution1()
        result = s1.numOfStrings(patterns, word)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxDotProduct(self, a: list[int], b: list[int]) -> int:
        # code here

        M = len(a)
        N = len(b)

        dp = [int(-1e9)] * (N + 1)
        dp[0] = 0

        for i in range(1, M + 1):
            for j in range(N, 0, -1):
                dp[j] = max(dp[j], dp[j - 1] + (a[i - 1] * b[j - 1]))

        return dp[N]

        # Complexity analysis
        # Time : O(M * N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Dot Product with 0 Insertions - https://www.geeksforgeeks.org/problems/maximize-dot-product2649/1

    testcase = [
        [[2, 3, 1, 7, 8], [3, 6, 7], 107],
        [[1, 2, 3], [4], 12],
    ]

    for line in testcase:
        [a, b, expected] = line
        s2 = Solution2()
        result = s2.maxDotProduct(a, b)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 29 of June 2026

    p1()

    p2()
