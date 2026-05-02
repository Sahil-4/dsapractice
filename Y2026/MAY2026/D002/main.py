import math


class Solution1:
    def rotatedDigits(self, n: int) -> int:
        table = [-1] * (n + 1)
        table[0] = 0

        count = 0

        for i in range(1, n + 1):
            remain = table[i // 10]

            if remain == 2:
                table[i] = 2
                continue

            d = i % 10

            if d in (0, 1, 8):
                digit_check = 0
            elif d in (2, 5, 6, 9):
                digit_check = 1
            else:
                table[i] = 2
                continue

            if remain == 0 and digit_check == 0:
                table[i] = 0
            else:
                table[i] = 1

            if table[i] == 1:
                count += 1

        return count

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 788. Rotated Digits - https://leetcode.com/problems/rotated-digits/description/?envType=daily-question&envId=2026-05-02

    testcase = [
        [10, 4],
        [1, 0],
        [2, 1],
    ]

    for line in testcase:
        [n, expected] = line
        s1 = Solution1()
        result = s1.rotatedDigits(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findPosition(self, n: int) -> int:
        # code here
        # n has only 1 bit
        # if n is a power of 2

        if n == 0 or n & (n - 1) != 0:
            return -1

        return int(math.log2(n)) + 1

        # Complexity analysis
        # Time : O(1)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Position of the Set Bit - https://www.geeksforgeeks.org/problems/find-position-of-set-bit3706/1

    testcase = [
        [2, 2],
        [5, -1],
    ]

    for line in testcase:
        [n, expected] = line
        s2 = Solution2()
        result = s2.findPosition(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 2 of May 2026

    p1()

    p2()
