from math import gcd


class Solution1:
    SEQUENTIAL_DIGITS_NUMBERS = [
        12,
        23,
        34,
        45,
        56,
        67,
        78,
        89,
        123,
        234,
        345,
        456,
        567,
        678,
        789,
        1234,
        2345,
        3456,
        4567,
        5678,
        6789,
        12345,
        23456,
        34567,
        45678,
        56789,
        123456,
        234567,
        345678,
        456789,
        1234567,
        2345678,
        3456789,
        12345678,
        23456789,
        123456789,
    ]

    def sequentialDigits(self, low: int, high: int) -> list[int]:
        answer = []

        for number in self.SEQUENTIAL_DIGITS_NUMBERS:
            if low <= number <= high:
                answer.append(number)

        return answer

        # Complexity analysis
        # Time : O(1)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1291. Sequential Digits - https://leetcode.com/problems/sequential-digits/description/?envType=daily-question&envId=2026-07-13

    testcase = [
        [100, 300, [123, 234]],
        [1000, 13000, [1234, 2345, 3456, 4567, 5678, 6789, 12345]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.sequentialDigits(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minOperations(self, b: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(b)

        visited = [False] * n
        lcm = 1

        for i in range(n):

            if visited[i]:
                continue

            cycle_len = 0
            curr = i

            while not visited[curr]:
                visited[curr] = True
                curr = b[curr] - 1
                cycle_len += 1

            lcm = (lcm * cycle_len) // gcd(lcm, cycle_len)

        return lcm % MOD

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Rearrange the Array - https://www.geeksforgeeks.org/problems/rearrange-the-array-1639032648/1

    testcase = [
        [[1, 2, 3], 1],
        [[2, 3, 1, 5, 4], 6],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minOperations(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 13 of July 2026

    p1()

    p2()
