from typing import List


class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        # Process both strings from right to left
        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            total = digit_a + digit_b + carry

            result.append(str(total % 2))  # current bit
            carry = total // 2  # next carry

            i -= 1
            j -= 1

        # Reverse to get correct order
        return "".join(reversed(result))

        # Complexity analysis
        # Time : O(max(N, M))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 67. Add Binary - https://leetcode.com/problems/add-binary/?envType=daily-question&envId=2026-02-15

    testcase = [
        ["11", "1", "100"],
        ["1010", "1011", "10101"],
    ]

    for line in testcase:
        [a, b, expected] = line
        s1 = Solution1()
        result = s1.addBinary(a, b)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findMinDiff(self, arr: List[int], m: int) -> int:
        n = len(arr)

        if m == 0 or m > n:
            return 0

        arr.sort()

        min_diff = float("inf")

        for i in range(n - m + 1):
            diff = arr[i + m - 1] - arr[i]
            min_diff = min(min_diff, diff)

        return int(min_diff)

        # Complexity analysis
        # Time : O(N * Log(N)) + O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Chocolate Distribution Problem - https://www.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1

    testcase = [
        [[3, 4, 1, 9, 56, 7, 9, 12], 5, 6],
        [[7, 3, 2, 4, 9, 12, 56], 3, 2],
        [[3, 4, 1, 9, 56], 5, 55],
    ]

    for line in testcase:
        [arr, m, expected] = line
        s2 = Solution2()
        result = s2.findMinDiff(arr, m)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 15 of February 2026

    p1()

    p2()
