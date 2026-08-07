from math import gcd


class Solution1:
    def free_slots_filler(self, required: int, length: int) -> str:
        # greedily consume the remaining prime factors using larger digits first
        # so the factor requirement fits within the available slots

        digits = []

        for digit in range(9, 1, -1):
            while required % digit == 0:
                digits.append(str(digit))
                required //= digit

        # pad remaining positions with '1' and reverse to get
        # lexicographically smallest valid suffix
        while len(digits) < length:
            digits.append("1")

        digits.reverse()
        return "".join(digits)

    def smallestNumber(self, num: str, t: int) -> str:
        # Intuition:
        # keep the longest possible prefix unchanged
        # starting from the right increase one digit
        # and greedily build the smallest valid suffix

        n = len(num)

        # If t contains a prime factor other than {2,3,5,7},
        # it is impossible to construct a valid zero-free number.
        temp = t
        for prime in (2, 3, 5, 7):
            while temp % prime == 0:
                temp //= prime

        if temp != 1:
            return "-1"

        # remaining_factor[i] = factor of t still needed after fixing
        # the first i digits of the answer
        remaining_factor = [t] * (n + 1)

        for i in range(n):
            digit = int(num[i])

            if digit == 0:
                break

            remaining_factor[i + 1] = remaining_factor[i] // gcd(
                remaining_factor[i], digit
            )

        # original number already satisfies the condition
        if remaining_factor[n] == 1:
            return num

        zero_pos = num.find("0")
        zero_index = n - 1 if zero_pos == -1 else zero_pos

        # traverse right to left so the first successful modification
        # yields the smallest number greater than or equal to num
        for i in range(zero_index, -1, -1):
            required = remaining_factor[i]
            free_slots = n - 1 - i

            start_digit = max(1, int(num[i]) + 1)

            for digit in range(start_digit, 10):
                further_required = required // gcd(required, digit)

                # after increasing the current digit, greedily construct
                # the smallest possible suffix satisfying the remaining factor.
                required_number = self.free_slots_filler(
                    further_required,
                    free_slots,
                )

                if len(required_number) == free_slots:
                    return num[:i] + str(digit) + required_number

        # no answer of the same length exists.
        return self.free_slots_filler(t, n + 1)

        # Complexity analysis
        # Time : O(N * Log(T))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3348. Smallest Divisible Digit Product II - https://leetcode.com/problems/smallest-divisible-digit-product-ii/?envType=daily-question&envId=2026-08-07

    testcase = [
        ["1234", 256, "1488"],
        ["12355", 50, "12355"],
        ["11111", 26, "-1"],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.smallestNumber(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countFriendsPairings(self, n: int) -> int:
        # code here
        MOD = 1000000007

        if n <= 2:
            return n

        prev2 = 1  # f(1)
        prev1 = 2  # f(2)

        for i in range(3, n + 1):
            curr = (prev1 + (i - 1) * prev2) % MOD
            prev2 = prev1
            prev1 = curr

        pairings = prev1

        return pairings

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Friends Pairing Problem - https://www.geeksforgeeks.org/problems/friends-pairing-problem5425/1

    testcase = [
        [3, 4],
        [2, 2],
        [1, 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.countFriendsPairings(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 7 of August 2026

    p1()

    p2()
