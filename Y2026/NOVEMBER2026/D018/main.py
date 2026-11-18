class Solution1:
    def minChanges(self, s: str) -> int:
        N = len(s)

        # every substring of the partition has even length and a single repeated
        # character, so it can always be cut into pairs of equal characters.
        # Fix each adjacent pair (2i, 2i + 1) independently : one change per mismatching pair
        changes = 0

        for i in range(0, N, 2):
            if s[i] != s[i + 1]:
                changes += 1

        return changes

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2914. Minimum Number of Changes to Make Binary String Beautiful - https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/?envType=daily-question&envId=2026-11-18

    testcase = [
        ["1001", 2],
        ["10", 1],
        ["0000", 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minChanges(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findXOR(self, l: int, r: int) -> int:
        # code here

        # answer depends on how many times any bit
        # appeared in nums in range l,r
        # consider bits appeared odd times
        # bits appeared even times will cancel out each other
        # by XOR logic

        # prefix XOR : 0 ^ 1 ^ ... ^ n repeats with period 4
        def xor_till(n: int) -> int:
            remainder = n % 4

            if remainder == 0:
                return n
            if remainder == 1:
                return 1
            if remainder == 2:
                return n + 1

            return 0

        # numbers up to l - 1 cancel out in the XOR of the two prefixes
        return xor_till(r) ^ xor_till(l - 1)

        # Complexity analysis
        # Time : O(1)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks XOR of Number Range - https://www.geeksforgeeks.org/problems/find-xor-of-numbers-from-l-to-r/1

    testcase = [
        [4, 8, 8],
        [2, 4, 5],
        [5, 9, 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.findXOR(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        N = len(temperatures)

        answer = [0] * N
        stack = [N - 1]

        for i in range(N - 2, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                answer[i] = stack[-1] - i

            stack.append(i)

        return answer

        # Complexity analysis
        # Time : O(2N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 739. Daily Temperatures - https://leetcode.com/problems/daily-temperatures/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]],
        [[30, 40, 50, 60], [1, 1, 1, 0]],
        [[30, 60, 90], [1, 1, 0]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.dailyTemperatures(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 18 of November 2026

    p1()

    p2()

    p3()
