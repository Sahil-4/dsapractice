class Solution1:
    def processStr(self, s: str, k: int) -> str:
        L = 0

        # final L
        for ch in s:
            if ch == "*":
                if L > 0:
                    L -= 1
            elif ch == "#":
                L *= 2
            elif ch == "%":
                pass
            else:
                L += 1

        if k >= L:
            return "."

        # reverse simulation
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            if ch == "*":
                L += 1

            elif ch == "%":
                k = L - k - 1

            elif ch == "#":
                L //= 2
                if k >= L:
                    k -= L

            else:  # letter
                L -= 1
                if k == L:
                    return ch

        return "."

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3614. Process String with Special Operations II - https://leetcode.com/problems/process-string-with-special-operations-ii/description/?envType=daily-question&envId=2026-06-17

    testcase = [
        ["a#b%*", 1, "a"],
        ["cd%#*#", 3, "d"],
        ["z*#", 0, "."],
    ]

    for line in testcase:
        [s, k, expected] = line
        s1 = Solution1()
        result = s1.processStr(s, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxProduct(self, n: int) -> int:
        # code here

        if n == 2:
            return 1
        if n == 3:
            return 2

        product = 1

        while n > 4:
            product *= 3
            n -= 3

        return product * n

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Cut rope to maximise product - https://www.geeksforgeeks.org/problems/max-rope-cutting1312/1

    testcase = [
        [2, 1],
        [5, 6],
    ]

    for line in testcase:
        [n, expected] = line
        s2 = Solution2()
        result = s2.maxProduct(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 17 of June 2026

    p1()

    p2()
