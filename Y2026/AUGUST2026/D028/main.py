class Solution1:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        N = len(s)

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord("a")] += 1

        odd = [i for i in range(26) if freq[i] % 2 == 1]

        if len(odd) > 1:
            return ""

        center = chr(ord("a") + odd[0]) if N % 2 else ""
        half = [cnt // 2 for cnt in freq]
        M = N // 2

        def make_palindrome(left):
            if N % 2:
                return left + center + left[::-1]
            return left + left[::-1]

        best = None

        remaining = half[:]
        prefix = []

        for i in range(M):
            t = ord(target[i]) - ord("a")

            for c in range(t + 1, 26):
                if remaining[c] > 0:
                    remaining[c] -= 1

                    suffix = []
                    for x in range(26):
                        if remaining[x]:
                            suffix.append(chr(ord("a") + x) * remaining[x])

                    left = "".join(chr(ord("a") + x) for x in prefix)
                    left += chr(ord("a") + c)
                    left += "".join(suffix)

                    candidate = make_palindrome(left)

                    if candidate > target:
                        if best is None or candidate < best:
                            best = candidate

                    remaining[c] += 1
                    break

            if remaining[t] <= 0:
                break

            remaining[t] -= 1
            prefix.append(t)

        remaining = half[:]
        left_chars = []
        possible = True

        for i in range(M):
            c = ord(target[i]) - ord("a")

            if remaining[c] == 0:
                possible = False
                break

            remaining[c] -= 1
            left_chars.append(chr(ord("a") + c))

        if possible:
            left = "".join(left_chars)
            candidate = make_palindrome(left)

            if candidate > target:
                if best is None or candidate < best:
                    best = candidate

        return best if best is not None else ""

        # Complexity Analysis
        # Time : O(N * N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3734. Lexicographically Smallest Palindromic Permutation Greater Than Target - https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/description/?envType=daily-question&envId=2026-08-28

    testcase = [
        ["baba", "abba", "baab"],
        ["baba", "bbaa", ""],
        ["abc", "abb", ""],
        ["aac", "abb", "aca"],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.lexPalindromicPermutation(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minCost(self, mat: list[list[int]]) -> int:
        dp = mat[0][:]

        for index in range(1, len(mat)):
            new_dp = [
                mat[index][0] + min(dp[1], dp[2]),
                mat[index][1] + min(dp[0], dp[2]),
                mat[index][2] + min(dp[0], dp[1]),
            ]

            dp = new_dp

        return min(dp)

        # Complexity Analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Cost Selection - https://www.geeksforgeeks.org/problems/buying-vegetables0016/1

    testcase = [
        [[[1, 50, 50], [50, 50, 50], [1, 50, 50]], 52],
        [[[1, 4, 1], [3, 2, 2], [3, 2, 3]], 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minCost(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 28 of August 2026

    p1()

    p2()
