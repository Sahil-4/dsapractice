class Solution1:
    def minimumDeletions(self, s: str) -> int:

        n = len(s)

        left_b = [0] * n
        right_a = [0] * n

        # Count 'b's to the left of each index
        count_b = 0
        for i in range(n):
            left_b[i] = count_b
            if s[i] == "b":
                count_b += 1

        # Count 'a's to the right of each index
        count_a = 0
        for i in range(n - 1, -1, -1):
            right_a[i] = count_a
            if s[i] == "a":
                count_a += 1

        # Find minimum deletions
        ans = float("inf")
        for i in range(n):
            ans = min(ans, left_b[i] + right_a[i])

        return int(ans)

        # Complexity analysis
        # Time : O(3N)
        # Space : O(2N)


def p1():
    # Problem 1 : POTD Leetcode 1653. Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/?envType=daily-question&envId=2026-02-07

    testcase = [
        ["aababbab", 2],
        ["bbaaaaabb", 2],
    ]

    for line in testcase:
        [s, expected] = line
        s1 = Solution1()
        result = s1.minimumDeletions(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxSum(self, arr):
        # Code here
        n = len(arr)

        temp = 0
        total_sum = 0
        ans = 0

        # Compute initial sum of i * a[i] and array sum
        for i in range(n):
            temp += i * arr[i]
            total_sum += arr[i]

        ans = temp

        # Compute max value using rotation formula
        for i in range(1, n):
            temp = temp - total_sum + arr[i - 1] * n
            ans = max(ans, temp)

        return ans

        # Complexity analysis
        # Time : O(2N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max sum in the configuration - https://www.geeksforgeeks.org/problems/max-sum-in-the-configuration/1

    testcase = [
        [[3, 1, 2, 8], 29],
        [[1, 2, 3], 8],
        [[4, 13], 13],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.maxSum(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 7 of February 2026

    p1()

    p2()
