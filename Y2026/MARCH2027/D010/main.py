from typing import List


class Solution1:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        table = [[[0] * 2 for _ in range(one + 1)] for _ in range(zero + 1)]

        for i in range(min(zero, limit) + 1):
            table[i][0][0] = 1

        for j in range(min(one, limit) + 1):
            table[0][j][1] = 1

        for i in range(zero + 1):
            for j in range(one + 1):
                if i == 0 or j == 0:
                    continue

                table[i][j][1] = (table[i][j - 1][0] + table[i][j - 1][1]) % MOD

                if j - 1 >= limit:
                    table[i][j][1] = (
                        table[i][j][1] - table[i][j - 1 - limit][0] + MOD
                    ) % MOD

                table[i][j][0] = (table[i - 1][j][0] + table[i - 1][j][1]) % MOD

                if i - 1 >= limit:
                    table[i][j][0] = (
                        table[i][j][0] - table[i - 1 - limit][j][1] + MOD
                    ) % MOD

        return (table[zero][one][0] + table[zero][one][1]) % MOD

        # Complexity analysis
        # Time : O(Z * O)
        # Space : O(Z * O * 2)


def p1():
    # Problem 1 : POTD Leetcode 3130. Find All Possible Stable Binary Arrays II - https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/description/?envType=daily-question&envId=2026-03-10

    testcase = [
        [1, 1, 2, 2],
        [1, 2, 1, 1],
        [3, 3, 2, 14],
        [20, 15, 75, 247943139],
    ]

    for line in testcase:
        [zero, one, limit, expected] = line
        s1 = Solution1()
        result = s1.numberOfStableArrays(zero, one, limit)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countSubarrays(self, arr: List[int]) -> int:
        # code here
        # first element must be the minimum in that subarray
        # find the first element to the right that is smaller than arr[i]
        # count_i​ = nextSmaller[i]−i
        # we need next smaller element to the right
        # use monotonic stack
        # traversing from right to left

        n = len(arr)
        stack = []
        ans = 0

        for i in range(n - 1, -1, -1):

            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                next_smaller = stack[-1]
            else:
                next_smaller = n

            ans += next_smaller - i
            stack.append(i)

        return ans

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Subarrays with First Element Minimum - https://www.geeksforgeeks.org/problems/subarrays-with-first-element-minimum/1

    testcase = [
        [[1, 2, 1], 5],
        [[1, 3, 5, 2], 8],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.countSubarrays(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 10 of March 2026

    p1()

    p2()
