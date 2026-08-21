from math import gcd


class Solution1:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        coins.sort()
        new_coins = []
        for x in coins:
            if all(x % y for y in new_coins):
                new_coins.append(x)
        coins = new_coins

        n = len(coins)
        m = 1 << n
        lcm = [1] * m

        left = k
        right = coins[0] * k + 1

        for mask in range(1, m):
            pre_mask = mask & (mask - 1)
            i = (mask & -mask).bit_length() - 1

            tmp = lcm[pre_mask] // gcd(lcm[pre_mask], coins[i])
            if tmp <= right // coins[i]:
                lcm[mask] = tmp * coins[i]
            else:
                lcm[mask] = right + 1

        def count(x: int) -> int:
            res = 0
            for mask in range(1, m):
                if lcm[mask] > x:
                    continue
                if bin(mask).count("1") & 1:
                    res += x // lcm[mask]
                else:
                    res -= x // lcm[mask]
            return res

        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left

        # Complexity analysis
        # Time : O(N*N + 2^N * (log(max(coins)) + log(k * min(coins))))
        # Space : O(2^N)


def p1():
    # Problem 1 : POTD Leetcode 3116. Kth Smallest Amount With Single Denomination Combination - https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/description/?envType=daily-question&envId=2026-08-21

    testcase = [
        [[3, 6, 9], 3, 9],
        [[5, 2], 7, 12],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.findKthSmallest(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def transform(self, s1: str, s2: str) -> int:
        # code here

        # lengths differ, transformation is impossible
        if len(s1) != len(s2):
            return -1

        # whether both strings contain the same characters
        # with the same frequencies
        if sorted(s1) != sorted(s2):
            return -1

        # traverse right to left.
        # characters match, both are part of the suffix
        # that does not need to be moved;
        # they don't match, skip the character in s1 because
        # it needs to be moved to the front;
        i = len(s1) - 1
        j = len(s2) - 1

        while i >= 0 and j >= 0:
            if s1[i] == s2[j]:
                i -= 1
                j -= 1
            else:
                i -= 1

        # j + 1 characters of s2 need to be moved to the front
        return j + 1

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Transform String - https://www.geeksforgeeks.org/problems/transform-string5648/1

    testcase = [
        ["abd", "bad", 1],
        ["GeeksForGeeks", "ForGeeksGeeks", 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.transform(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 21 of August 2026

    p1()

    p2()
