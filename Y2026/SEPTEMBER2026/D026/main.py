class Solution1:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        N = len(s)

        mp = {key: value for key, value in knowledge}

        result = []
        i = 0

        while i < N:
            if s[i] == "(":
                j = s.find(")", i + 1)
                key = s[i + 1 : j]
                result.append(mp.get(key, "?"))
                i = j + 1
            else:
                result.append(s[i])
                i += 1

        return "".join(result)

        # Complexity analysis
        # Time : O(N)
        # Space : O(K)


def p1():
    # P1 POTD Leetcode 1807. Evaluate the Bracket Pairs of a String - https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/description/?envType=daily-question&envId=2026-09-26

    testcase = [
        [
            "(name)is(age)yearsold",
            [["name", "bob"], ["age", "two"]],
            "bobistwoyearsold",
        ],
        [
            "hi(name)",
            [["a", "b"]],
            "hi?",
        ],
        [
            "(a)(a)(a)aaa",
            [["a", "yes"]],
            "yesyesyesaaa",
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.evaluate(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minimumCost(
        self, x: int, s: int, m: int, l: int, cs: int, cm: int, cl: int
    ) -> int:
        # code here

        INF = 10**12
        T = x + l + 1

        dp = [INF] * (T)
        dp[0] = 0

        for i in range(T):
            if dp[i] == INF:
                continue

            if i + s < T:
                dp[i + s] = min(dp[i + s], dp[i] + cs)

            if i + m < T:
                dp[i + m] = min(dp[i + m], dp[i] + cm)

            if i + l < T:
                dp[i + l] = min(dp[i + l], dp[i] + cl)

        result = INF
        for i in range(x, T):
            result = min(result, dp[i])

        return result

        # Complexity analysis
        # Time : O(T)
        # Space : O(T)


def p2():
    # P2 POTD Geeksforgeeks Minimum Cost Pizza Selection - https://www.geeksforgeeks.org/problems/pizza-mania0155/1

    testcase = [
        [16, 3, 6, 9, 50, 150, 300, 300],
        [10, 1, 3, 10, 10, 20, 50, 50],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minimumCost(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def plusOne(self, digits: list[int]) -> list[int]:
        N = len(digits)

        result = []
        carry = 1

        for i in range(N - 1, -1, -1):
            _sum = digits[i] + carry

            digit = _sum % 10
            carry = _sum // 10

            result.append(digit)

        while carry > 0:
            _sum = carry

            digit = _sum % 10
            carry = _sum // 10

            result.append(digit)

        result.reverse()

        return result

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p3():
    # P3 NC150 Leetcode 66. Plus One - https://leetcode.com/problems/plus-one/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[1, 2, 3], [1, 2, 4]],
        [[4, 3, 2, 1], [4, 3, 2, 2]],
        [[9], [1, 0]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.plusOne(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 26 of September 2026

    p1()

    p2()

    p3()
