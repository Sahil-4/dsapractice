class Solution1:
    def solve(self, upper_bound: int) -> int:
        if upper_bound < 100:
            return 0

        digits = str(upper_bound)
        total_digits = len(digits)

        # State format:
        # (second_last_digit, last_digit, is_tight, leading_zero, ways, waviness_sum)
        active_states = [(10, 10, 1, 1, 1, 0)]

        for idx in range(total_digits):
            digit_limit = int(digits[idx])

            state_count = [
                [[[0] * 11 for _ in range(11)] for _ in range(2)] for _ in range(2)
            ]
            state_sum = [
                [[[0] * 11 for _ in range(11)] for _ in range(2)] for _ in range(2)
            ]

            for (
                prev_digit,
                curr_digit,
                is_tight,
                leading_zero,
                ways,
                accumulated_sum,
            ) in active_states:
                allowed_max = digit_limit if is_tight else 9

                for next_digit in range(allowed_max + 1):
                    still_leading = leading_zero and next_digit == 0

                    updated_prev = curr_digit
                    updated_curr = 10 if still_leading else next_digit
                    updated_tight = 1 if (is_tight and next_digit == allowed_max) else 0

                    waviness_increment = 0

                    if not still_leading and prev_digit != 10 and curr_digit != 10:
                        is_peak = prev_digit < curr_digit > next_digit
                        is_valley = prev_digit > curr_digit < next_digit

                        if is_peak or is_valley:
                            waviness_increment = ways

                    state_count[updated_tight][still_leading][updated_prev][
                        updated_curr
                    ] += ways
                    state_sum[updated_tight][still_leading][updated_prev][
                        updated_curr
                    ] += (accumulated_sum + waviness_increment)

            compressed_states = []

            for tight_flag in range(2):
                for lead_flag in range(2):
                    for prev_digit in range(11):
                        for curr_digit in range(11):
                            ways = state_count[tight_flag][lead_flag][prev_digit][
                                curr_digit
                            ]

                            if ways:
                                compressed_states.append(
                                    (
                                        prev_digit,
                                        curr_digit,
                                        tight_flag,
                                        lead_flag,
                                        ways,
                                        state_sum[tight_flag][lead_flag][prev_digit][
                                            curr_digit
                                        ],
                                    )
                                )

            active_states = compressed_states

        total_waviness = 0

        for *_, waviness_sum in active_states:
            total_waviness += waviness_sum

        return total_waviness

    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.solve(num2) - self.solve(num1 - 1)

        # Complexity Analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3753. Total Waviness of Numbers in Range II - https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/description/?envType=daily-question&envId=2026-06-05

    testcase = [
        [120, 130, 3],
        [198, 202, 3],
        [4848, 4848, 2],
    ]

    for line in testcase:
        [num1, num2, expected] = line
        s1 = Solution1()
        result = s1.totalWaviness(num1, num2)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def lexicographicallySmallest(self, s: str, k: int) -> str:
        # code here

        N = len(s)
        k = k * 2 if (N & (N - 1)) else k // 2

        if k >= N:
            return "-1"

        stack = []

        for i in range(N):
            while stack and k > 0 and stack[-1] > s[i]:
                stack.pop()
                k -= 1
            stack.append(s[i])

        while k > 0:
            stack.pop()
            k -= 1

        ans = []
        while stack:
            ans.append(stack.pop())

        ans.reverse()

        return "".join(ans)

        # Complexity Analysis
        # Time : O(N + K)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Lexicographically smallest after removing k - https://www.geeksforgeeks.org/problems/lexicographically-smallest-after-removing-k/1

    testcase = [
        ["fooland", 2, "and"],
        ["code", 4, "cd"],
    ]

    for line in testcase:
        [s, k, expected] = line
        s2 = Solution2()
        result = s2.lexicographicallySmallest(s, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 5 of June 2026

    p1()

    p2()
