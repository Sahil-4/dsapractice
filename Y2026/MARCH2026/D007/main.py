from typing import List


class Solution1:
    def minFlips(self, s: str) -> int:
        N = len(s)

        result = float("inf")

        flip1 = 0
        flip2 = 0

        i = 0
        j = 0

        while j < 2 * N:
            expected_char_s1 = "0" if j % 2 == 0 else "1"
            expected_char_s2 = "1" if j % 2 == 0 else "0"

            if s[j % N] != expected_char_s1:
                flip1 += 1

            if s[j % N] != expected_char_s2:
                flip2 += 1

            if j - i + 1 > N:
                expected_char_s1 = "0" if i % 2 == 0 else "1"
                expected_char_s2 = "1" if i % 2 == 0 else "0"

                if s[i % N] != expected_char_s1:
                    flip1 -= 1

                if s[i % N] != expected_char_s2:
                    flip2 -= 1

                i += 1

            if j - i + 1 == N:
                result = min(result, flip1, flip2)

            j += 1

        return int(result)

        # Complexity analysis
        # Time : O(2N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1888. Minimum Number of Flips to Make the Binary String Alternating - https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description/?envType=daily-question&envId=2026-03-07

    testcase = [
        ["111000", 2],
        ["010", 0],
        ["1110", 1],
    ]

    for line in testcase:
        [s, expected] = line
        s1 = Solution1()
        result = s1.minFlips(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def recursion(self, m: int, n: int, x: int, memo: List[List[int]]) -> int:
        if n == 0:
            return 1 if x == 0 else 0

        if memo[n][x] != -1:
            return memo[n][x]

        ways = 0

        for e in range(1, m + 1):
            if e <= x:
                ways += self.recursion(m, n - 1, x - e, memo)

        memo[n][x] = ways
        return memo[n][x]

        # Complexity analysis
        # Time : O(M*N*X)
        # Space : O(N*X)

    def noOfWays(self, m: int, n: int, x: int) -> int:
        # code here
        # simplify
        # We have `m` numbers from 1 to m to choose from
        # We have to pick any number e from 1 to m total n number of times
        # and achieve sum x

        memo = [[-1] * (x + 1) for _ in range(n + 1)]
        ways = self.recursion(m, n, x, memo)

        return ways


def p2():
    # Problem 2 : POTD Geeksforgeeks Dice throw - https://www.geeksforgeeks.org/problems/dice-throw5349/1

    testcase = [
        [6, 3, 12, 25],
        [2, 3, 6, 1],
    ]

    for line in testcase:
        [m, n, x, expected] = line
        s2 = Solution2()
        result = s2.noOfWays(m, n, x)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 7 of March 2026

    p1()

    p2()
