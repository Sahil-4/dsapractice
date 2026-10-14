class Solution1:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""

        nines_count = sum // 9
        remainder = sum % 9

        good_integer = ["9"] * nines_count
        if remainder > 0:
            good_integer.append(str(remainder))

        need_digits = num - nines_count - (1 if remainder > 0 else 0)
        good_integer.extend(["0"] * need_digits)

        return "".join(good_integer)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3723. Maximize Sum of Squares of Digits - https://leetcode.com/problems/maximize-sum-of-squares-of-digits/description/?envType=daily-question&envId=2026-10-14

    testcase = [
        [2, 3, "30"],
        [2, 17, "98"],
        [1, 10, ""],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maxSumOfSquares(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findRollOut(self, s, roll):
        # code here
        N = len(s)

        # increment = [0   0   0   0]
        # increment = [1  -1   0   0]
        # increment = [2  -1  -1   0]
        # increment = [3  -1  -1  -1]
        # increment = [3   2   1   0]
        # "bca" -> "b+3,c+2,a+1"
        # bca -> "eeb"

        increment = [0] * (N + 1)

        for r in roll:
            increment[0] += 1
            increment[r] -= 1

        for i in range(1, N + 1):
            increment[i] += increment[i - 1]

        updated_s = []
        for i in range(N):
            c = s[i]
            uc = chr(ord("a") + ((ord(c) - ord("a") + increment[i]) % 26))

            updated_s.append(uc)

        return "".join(updated_s)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Roll Characters of String - https://www.geeksforgeeks.org/problems/roll-the-characters-of-a-string2127/1

    testcase = [
        ["bca", [1, 2, 3], "eeb"],
        ["zcza", [1, 1, 3, 4], "debb"],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.findRollOut(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def isPalindrome(self, s: str) -> bool:
        # using two pointers

        N = len(s)

        l = 0
        r = N - 1

        while l < r:
            lc = s[l]
            rc = s[r]

            if lc >= "A" and lc <= "Z":
                lc = chr(ord("a") + (ord(lc) - ord("A")))

            if not (lc >= "a" and lc <= "z" or lc >= "0" and lc <= "9"):
                l += 1
                continue

            if rc >= "A" and rc <= "Z":
                rc = chr(ord("a") + (ord(rc) - ord("A")))

            if not (rc >= "a" and rc <= "z" or rc >= "0" and rc <= "9"):
                r -= 1
                continue

            if lc != rc:
                return False

            l += 1
            r -= 1

        return True

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 125. Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["A man, a plan, a canal: Panama", True],
        ["race a car", False],
        [" ", True],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.isPalindrome(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 14 of October 2026

    p1()

    p2()

    p3()
