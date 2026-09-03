class Solution1:
    def uniformArray(self, nums1: list[int]) -> bool:
        N = len(nums1)

        # count of even, odd
        even_count, odd_count = 0, 0

        # smallest even, and smallest odd number in nums1
        smallest_even, smallest_odd = 1000000001, 1000000001

        for num in nums1:

            even_count += 1 if not (num & 1) else 0
            odd_count += 1 if (num & 1) else 0

            if num & 1:
                smallest_odd = min(smallest_odd, num)
            else:
                smallest_even = min(smallest_even, num)

        # either all even or all odds - return as it is nums2 = nums1
        if even_count == N or odd_count == N:
            return True

        # how to make all odds - subtract odd from all evens;
        # even - odd1 = odd2
        # even > odd1, and odd2 > 0 - (1)
        # find smallest even, and smallest odd
        # if (1) holds return True
        if smallest_even > smallest_odd:
            return True

        # how to make all even - subtract even from all odds; odd1 - odd2 = even
        # odd1 > odd2, and even > 0
        # not possible (circular dependency)
        # we will never be able to convert smallest odd number to even

        return False

        # Complexity analysis
        # Time: O(N)
        # Space: O(1)


def p1():
    # Problem 1 : POTD Leetcode 3876. Construct Uniform Parity Array II - https://leetcode.com/problems/construct-uniform-parity-array-ii/description/?envType=daily-question&envId=2026-09-03

    testcase = [
        [[1, 4, 7], True],
        [[2, 3], False],
        [[4, 6], True],
        [[22, 2, 13], False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.uniformArray(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxDiffSum(self, arr: list[int]) -> int:
        # code here

        N = len(arr)

        prev, prev_replace = 0, 0

        for i in range(1, N):

            curr = max(prev + abs(arr[i] - arr[i - 1]), prev_replace + abs(arr[i] - 1))
            curr_replace = max(prev + abs(1 - arr[i - 1]), prev_replace)

            prev = curr
            prev_replace = curr_replace

        return max(prev, prev_replace)

        # Complexity analysis
        # Time: O(N)
        # Space: O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks  Max Adjacent Diffs Sum with 1 Replacements - https://www.geeksforgeeks.org/problems/modify-array-to-maximize-sum-of-adjacent-differences1729/1

    testcase = [
        [[3, 2, 1, 4, 5], 8],
        [[1, 5], 4],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxDiffSum(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def change(self, amount: int, coins: list[int]) -> int:
        N = len(coins)

        dp_next = [0 for _ in range(amount + 1)]

        for coin_index in range(N, -1, -1):
            dp_curr = [0 for _ in range(amount + 1)]
            for remaining_amount in range(0, amount + 1, +1):
                if remaining_amount == 0:
                    dp_curr[remaining_amount] = 1

                elif coin_index >= N:
                    dp_curr[remaining_amount] = 0

                else:
                    dp_curr[remaining_amount] = 0

                    # pick coin_index coin
                    if remaining_amount >= coins[coin_index]:
                        dp_curr[remaining_amount] += dp_curr[
                            remaining_amount - coins[coin_index]
                        ]

                    # skip coin_index coin
                    dp_curr[remaining_amount] += dp_next[remaining_amount]

            dp_next = dp_curr

        return dp_next[amount]

        # Complexity analysis
        # Time: O(C * A)
        # Space: O(2A)


def p3():
    # Problem 3 : NC150 Leetcode 7. Reverse Integer - https://leetcode.com/problems/reverse-integer/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [5, [1, 2, 5], 4],
        [3, [2], 0],
        [10, [10], 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.change(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def reverse(self, x: int) -> int:
        min_cap, max_cap = -2147483648, 2147483647

        negative = bool(x < 0)

        x = abs(x)
        reverse_x = 0

        while x > 0:
            d = x % 10
            x //= 10

            reverse_x *= 10
            reverse_x += d

            if negative:
                if reverse_x * -1 < min_cap:
                    return 0
            else:
                if reverse_x > max_cap:
                    return 0

        return reverse_x * -1 if negative else reverse_x

        # Complexity analysis
        # Time: O(Log(N))
        # Space: O(1)


def p4():
    # Problem 4 : NC150 Leetcode 518. Coin Change II - https://leetcode.com/problems/coin-change-ii/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [123, 321],
        [-123, -321],
        [120, 21],
        [0, 0],
        [10, 1],
        [-2147483648, 0],
        [2147483647, 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.reverse(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 3 of September 2026

    p1()

    p2()

    p3()

    p4()
