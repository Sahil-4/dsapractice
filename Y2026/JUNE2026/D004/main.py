class Solution1:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(n: int) -> int:
            s = str(n)

            w_count = 0
            for a, b, c in zip(s, s[1:], s[2:]):
                if (a < b > c) or (a > b < c):
                    w_count += 1

            return w_count

        total_waviness = 0
        for n in range(num1, num2 + 1):
            total_waviness += waviness(n)

        return total_waviness

        # Complexity Analysis
        # Time : O(N * Log(N))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3751. Total Waviness of Numbers in Range I - https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/description/?envType=daily-question&envId=2026-06-04

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
    def maxSubstring(self, s: str) -> int:
        # code here

        N = len(s)

        ans = -1

        psum = 0
        for i in range(N):
            psum += 1 if s[i] == "0" else -1

            if psum > ans:
                ans = psum

            if psum < 0:
                psum = 0

        return ans

        # Complexity Analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Substring with Max Zero-One Diff - https://www.geeksforgeeks.org/problems/maximum-difference-of-zeros-and-ones-in-binary-string4111/1

    testcase = [
        ["11000010001", 6],
        ["111", -1],
        ["000", 3],
        ["101010", 1],
        ["010101", 1],
    ]

    for line in testcase:
        [s, expected] = line
        s2 = Solution2()
        result = s2.maxSubstring(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 4 of June 2026

    p1()

    p2()
