class Solution1:
    def stoneGameIX(self, stones: list[int]) -> bool:

        remainder_zero_count = 0
        remainder_one_count = 0
        remainder_two_count = 0

        for stone in stones:
            remainder = stone % 3

            if remainder == 0:
                remainder_zero_count += 1
            elif remainder == 1:
                remainder_one_count += 1
            else:
                remainder_two_count += 1

        # even number of stones divisible by 3 does not
        # change the fundamental winning condition
        if remainder_zero_count % 2 == 0:
            return remainder_one_count > 0 and remainder_two_count > 0

        # With an odd number of stones divisible by 3
        # one remainder type must outnumber the other by at least 3
        return abs(remainder_one_count - remainder_two_count) > 2

        # Complexity Analysis
        # Time: O(N)
        # Space: O(1)


def p1():
    # Problem 1 : POTD Leetcode 2029. Stone Game IX - https://leetcode.com/problems/stone-game-ix/description/?envType=daily-question&envId=2026-08-16

    testcase = [
        [[2, 1], True],
        [[2], False],
        [[5, 1, 2, 4, 3], False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.stoneGameIX(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minProd(self, arr: list[int]) -> int:
        # code here

        # cases:
        # no negative elements
        #   - return the smallest positive element (including 0)
        #
        # odd number of negative elements
        #   - multiply all non-zero elements
        #   - the resulting product is negative, so it is the minimum
        #
        # even number of negative elements
        #   - exclude the negative number closest to zero
        #   - multiply all remaining non-zero elements
        #   - this leaves an odd number of negative elements

        negative_count = 0
        closest_to_zero_negative = -11
        product = 1

        for value in arr:
            if value < 0:
                negative_count += 1
                closest_to_zero_negative = max(
                    closest_to_zero_negative,
                    value,
                )

            if value != 0:
                product *= value

        # no negative numbers
        if negative_count == 0:
            return 0 if 0 in arr else min(arr)

        # odd number of negative numbers
        if negative_count % 2 == 1:
            return product

        # even number of negative numbers
        # exclude the negative closest to zero
        return product // closest_to_zero_negative

        # Complexity Analysis
        # Time: O(N)
        # Space: O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Min Product Subset - https://www.geeksforgeeks.org/problems/max-and-min-products3347/1

    testcase = [
        [[1, 2, 3], 1],
        [[4, -2, 5], -40],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minProd(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 16 of August 2026

    p1()

    p2()
