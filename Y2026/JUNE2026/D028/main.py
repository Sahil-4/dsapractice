class Solution1:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        # sort the array
        # make 0th element 1
        # move forward i = 1 to i < N
        # if element arr[i] > (arr[i - 1] + 1)
        # make arr[i] = arr[i - 1] + 1
        # at last return arr[-1]

        copy = arr.copy()
        N = len(copy)

        copy.sort()

        copy[0] = 1

        for i in range(1, N):
            if copy[i] > copy[i - 1] + 1:
                copy[i] = copy[i - 1] + 1

        return copy[-1]

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1846. Maximum Element After Decreasing and Rearranging - https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/description/?envType=daily-question&envId=2026-06-28

    testcase = [
        [[2, 2, 1, 2, 1], 2],
        [[100, 1, 1000], 3],
        [[1, 2, 3, 4, 5], 5],
    ]

    for line in testcase:
        [arr, expected] = line
        s1 = Solution1()
        result = s1.maximumElementAfterDecrementingAndRearranging(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countStrings(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # impossible to have more than n-1 adjacent pairs
        if k > n - 1:
            return 0

        # dp0[i][j] -> length i, j adjacent pairs, ends with 0
        # dp1[i][j] -> length i, j adjacent pairs, ends with 1
        dp0 = [[0] * (k + 1) for _ in range(n + 1)]
        dp1 = [[0] * (k + 1) for _ in range(n + 1)]

        dp0[1][0] = 1
        dp1[1][0] = 1

        for length in range(2, n + 1):
            limit = min(k, length - 1)

            for pairs in range(limit + 1):

                # append 0: adjacent-pair count remains unchanged
                dp0[length][pairs] = (
                    dp0[length - 1][pairs] + dp1[length - 1][pairs]
                ) % MOD

                # append 1 after 0
                ways = dp0[length - 1][pairs]

                # append 1 after 1 -> creates one new adjacent pair
                if pairs > 0:
                    ways += dp1[length - 1][pairs - 1]

                dp1[length][pairs] = ways % MOD

        return (dp0[n][k] + dp1[n][k]) % MOD

        # Complexity analysis
        # Time : O(N * K)
        # Space : O(N * K)


def p2():
    # Problem 2 : POTD Geeksforgeeks k Times Appearing Adjacent Two 1's - https://www.geeksforgeeks.org/problems/count-binary-strings1944/1

    testcase = [
        [3, 2, 1],
        [5, 2, 6],
    ]

    for line in testcase:
        [n, k, expected] = line
        s2 = Solution2()
        result = s2.countStrings(n, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 28 of June 2026

    p1()

    p2()
