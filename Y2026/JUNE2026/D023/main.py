from itertools import accumulate


class Solution1:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        M = r - l + 1

        dp_0 = [1] * M
        dp_1 = [1] * M

        for _ in range(n - 1):
            sum_0 = list(accumulate(dp_0, initial=0))
            sum_1 = list(accumulate(dp_1, initial=0))

            dp_0 = [x % MOD for x in sum_1[:-1]]

            s0_m = sum_0[-1]
            dp_1 = [(s0_m - x) % MOD for x in sum_0[1:]]

        return (sum(dp_0) + sum(dp_1)) % MOD

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(M)


def p1():
    # Problem 1 : POTD Leetcode 3699. Number of ZigZag Arrays I - https://leetcode.com/problems/number-of-zigzag-arrays-i/description/?envType=daily-question&envId=2026-06-23

    testcase = [
        [3, 4, 5, 2],
        [3, 1, 3, 10],
    ]

    for line in testcase:
        [n, l, r, expected] = line
        s1 = Solution1()
        result = s1.zigZagArrays(n, l, r)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


from math import sqrt


class Solution2:
    def maxPeopleDefeated(self, p: int) -> int:
        # code here
        count_defeated = 0
        power_remaining = p

        for i in range(1, int(sqrt(p)) + 1):
            i_sqr = i * i

            if power_remaining < i_sqr:
                break

            power_remaining -= i_sqr
            count_defeated += 1

        return count_defeated

        # Complexity analysis
        # Time : O(SQRT(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Maximum Number of People Defeated - https://www.geeksforgeeks.org/problems/killing-spree3020/1

    testcase = [
        [14, 3],
        [10, 2],
    ]

    for line in testcase:
        [p, expected] = line
        s2 = Solution2()
        result = s2.maxPeopleDefeated(p)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 23 of June 2026

    p1()

    p2()
