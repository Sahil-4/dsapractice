class Solution1:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []

        # open first row
        grid.append("." * n)

        for _ in range(1, m):
            # open last col
            grid.append(("#" * (n - 1)) + ".")

        return grid

        # Complexity Analysis
        # Time : O(M * N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3963. Create Grid With Exactly One Path - https://leetcode.com/problems/create-grid-with-exactly-one-path/?envType=daily-question&envId=2026-10-27

    testcase = [
        [2, 3, ["...", "##."]],
        [3, 3, ["...", "##.", "##."]],
        [1, 4, ["...."]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.createGrid(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def getMaxWeight(self, s: str) -> int:
        # code here

        N = len(s)

        dp = [0] * (N + 1)
        dp[N - 1] = 1

        for i in range(N - 2, -1, -1):

            a = 1 + dp[i + 1]
            b = dp[i + 2]

            if s[i] != s[i + 1]:
                b += 4
            else:
                b += 3

            dp[i] = max(a, b)

        return dp[0]

        # Complexity Analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Maximum Weight Transformation of String - https://www.geeksforgeeks.org/problems/maximum-weight-transformation-of-a-given-string3551/1

    testcase = [
        ["AA", 3],
        ["ABB", 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.getMaxWeight(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # token == "/"
                    # Python division truncates towards negative infinity, but we want truncation towards zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]

        # Complexity Analysis
        # Time : O(N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 150. Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [["2", "1", "+", "3", "*"], 9],
        [["4", "13", "5", "/", "+"], 6],
        [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.evalRPN(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def maxProduct(self, nums: list[int]) -> int:
        N = len(nums)

        m_product = nums[0]

        l_product = 1
        r_product = 1

        for i in range(N):
            l_product = 1 if l_product == 0 else l_product
            r_product = 1 if r_product == 0 else r_product

            l_product *= nums[i]
            r_product *= nums[N - 1 - i]

            m_product = max(m_product, l_product, r_product)

        return m_product

        # Complexity Analysis
        # Time : O(N)
        # Space : O(1)


def p4():
    # Problem 4 : NC150 Leetcode 152. Maximum Product Subarray - https://leetcode.com/problems/maximum-product-subarray/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[2, 3, -2, 4], 6],
        [[-2, 0, -1], 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.maxProduct(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 27 of October 2026

    p1()

    p2()

    p3()

    p4()
