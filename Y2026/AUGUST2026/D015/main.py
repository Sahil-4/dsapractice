class Solution1:
    def longestSubsequence(self, nums: list[int]) -> int:
        xor = 0
        has_non_zero = False

        for num in nums:
            xor = xor ^ num
            has_non_zero = has_non_zero or num != 0

        l_sub_seq_len = 0
        if xor != 0:
            l_sub_seq_len = len(nums)
        elif has_non_zero:
            l_sub_seq_len = len(nums) - 1

        return l_sub_seq_len

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3702. Longest Subsequence With Non-Zero Bitwise XOR - https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/description/?envType=daily-question&envId=2026-08-15

    testcase = [
        [[1, 2, 3], 2],
        [[2, 3, 4], 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.longestSubsequence(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countWithout(self, n: int, d: int) -> int:
        # code here

        if n <= 0:
            return 0

        s = str(n)
        length = len(s)

        # count valid numbers with fewer digits than n
        count = 0

        for digits in range(1, length):
            if d == 0:
                # first digit: 1..9 => 9 choices
                # remaining digits: 1..9 => 9 choices
                count += 9**digits
            else:
                # first digit: 1..9 except d => 8 choices
                # remaining digits: 0..9 except d => 9 choices
                count += 8 * (9 ** (digits - 1))

        # count valid numbers having the same number of digits as n
        for i, ch in enumerate(s):
            current = int(ch)
            remaining = length - i - 1

            if d == 0:
                # first position, 0 is not allowed
                smaller = current - 1 if current > 0 else 0

                # d == 0, all non-zero smaller digits are valid
                if i == 0:
                    count += smaller * (9**remaining)
                else:
                    # later positions, 0 is excluded because d == 0
                    count += smaller * (9**remaining)
            else:
                # count valid digits smaller than current
                if i == 0:
                    # first digit: 1..current-1
                    smaller = current - 1

                    # exclude d if among those digits
                    if 1 <= d < current:
                        smaller -= 1
                else:
                    # later digits: 0..current-1
                    smaller = current

                    # exclude d if among those digits
                    if 0 <= d < current:
                        smaller -= 1

                count += smaller * (9**remaining)

            # current digit is d, n cannot be formed further
            if current == d:
                return count

        # n itself does not contain d
        return count + 1

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(Log(N))


def p2():
    # Problem 2 : POTD Geeksforgeeks Numbers Without d as Digit - https://www.geeksforgeeks.org/problems/count-numbers2004/1

    testcase = [
        [25, 3, 22],
        [5, 3, 4],
        [13, 3, 11],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.countWithout(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 15 of August 2026

    p1()

    p2()
