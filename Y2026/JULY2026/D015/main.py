from math import gcd


class Solution1:
    def gcdOfOddEvenSums(self, n: int) -> int:
        _d = 2
        odd_a = 1
        even_a = 2

        sum_odd = int((n / 2) * ((2 * odd_a) + (n - 1) * _d))
        sum_even = int((n / 2) * ((2 * even_a) + (n - 1) * _d))

        return gcd(sum_odd, sum_even)

        # Complexity analysis
        # Time : O(Log(sum_odd, sum_even))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3658. GCD of Odd and Even Sums - https://leetcode.com/problems/gcd-of-odd-and-even-sums/description/?envType=daily-question&envId=2026-07-15

    testcase = [
        [4, 4],
        [5, 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.gcdOfOddEvenSums(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def bitonic(self, arr: list[int]) -> int:
        # code here

        N = len(arr)

        increasing_left_2_right = [1] * N
        for i in range(1, N, 1):
            increasing_left_2_right[i] = (
                increasing_left_2_right[i - 1] + 1 if arr[i] >= arr[i - 1] else 1
            )

        increasing_right_2_left = [1] * N
        for i in range(N - 2, -1, -1):
            increasing_right_2_left[i] = (
                increasing_right_2_left[i + 1] + 1 if arr[i] >= arr[i + 1] else 1
            )

        lbs = 1
        for i in range(N):
            sub_len = increasing_left_2_right[i] + increasing_right_2_left[i] - 1
            lbs = max(lbs, sub_len)

        return lbs

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Longest Bitonic Subarray - https://www.geeksforgeeks.org/problems/maximum-length-bitonic-subarray5730/1

    testcase = [
        [[12, 4, 78, 90, 45, 23], 5],
        [[10, 20, 30, 40], 4],
        [[10, 10, 10, 10], 4],
        [[10, 10], 2],
        [[5, 4, 3, 2, 1], 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.bitonic(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 15 of July 2026

    p1()

    p2()
