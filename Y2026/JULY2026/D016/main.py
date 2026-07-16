from functools import lru_cache
from math import gcd


class Solution1:
    def gcdSum(self, nums: list[int]) -> int:
        N = len(nums)

        prefix_gcd = []

        mx_i = nums[0]
        for num in nums:
            mx_i = max(mx_i, num)
            prefix_gcd.append(gcd(num, mx_i))

        prefix_gcd.sort()

        gcd_sum = 0
        for i in range(N):
            left = i
            right = N - 1 - i

            if right <= left:
                break

            _a = prefix_gcd[left]
            _b = prefix_gcd[right]

            gcd_sum += gcd(_a, _b)

        return gcd_sum

        # Complexity analysis
        # Time : O(N * log(E))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3867. Sum of GCD of Formed Pairs - https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/description/?envType=daily-question&envId=2026-07-16

    testcase = [
        [[2, 6, 4], 2],
        [[3, 6, 2, 8], 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.gcdSum(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countWays(self, n: int, _sum: int) -> int:
        # code here
        T = 9 * 81

        @lru_cache(maxsize=T)
        def recursion(digit_index: int, digit_sum: int) -> int:
            if digit_index == n:
                return int(digit_sum == 0)

            count = 0

            # 0 case
            if digit_index != 0:
                count += recursion(digit_index + 1, digit_sum - 0)

            # 1 to 9 case
            for dec in range(1, 10):
                if digit_sum - dec < 0:
                    break

                count += recursion(digit_index + 1, digit_sum - dec)

            return count

        t_count = recursion(0, _sum)

        return t_count if t_count != 0 else -1

        # Complexity analysis
        # Time : O(T)
        # Space : O(T)


def p2():
    # Problem 2 : POTD Geeksforgeeks Numbers with Given Digit Sum - https://www.geeksforgeeks.org/problems/count-of-n-digit-numbers-whose-sum-of-digits-equals-to-given-sum0733/1

    testcase = [
        [2, 2, 2],
        [1, 10, -1],
        [2, 10, 9],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.countWays(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 16 of July 2026

    p1()

    p2()
