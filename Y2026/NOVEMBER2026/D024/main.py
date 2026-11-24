from collections import defaultdict
from math import gcd, lcm


class Solution1:
    def maxLength(self, nums: list[int]) -> int:
        N = len(nums)
        longest = 0

        # N <= 100 and nums[i] <= 10 : check every subarray with running product, gcd and lcm
        for i in range(N):
            product, g, l = 1, 0, 1

            for j in range(i, N):
                product *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])

                if product == g * l:
                    longest = max(longest, j - i + 1)

        return longest

        # Complexity analysis
        # Time : O(N^2)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3411. Maximum Subarray With Equal Products - https://leetcode.com/problems/maximum-subarray-with-equal-products/description/?envType=daily-question&envId=2026-11-24

    testcase = [
        [[1, 2, 1, 2, 1, 1, 1], 5],
        [[2, 3, 4, 5, 6], 3],
        [[1, 2, 3, 1, 4, 5, 1], 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maxLength(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findPairs(self, arr: list[int]) -> list[int]:
        N = len(arr)

        fallback = [-1, -1, -1, -1]

        # group every index pair (i, j), i < j, by its sum, pairs are generated in lexicographic order
        groups = defaultdict(list)
        for i in range(N):
            for j in range(i + 1, N):
                groups[arr[i] + arr[j]].append((i, j))

        best = None

        for pairs in groups.values():
            found = False

            # in every group the lexicographically smallest quadruplet is
            # the first pair that has a later pair with no shared index, and its first such partner
            for x in range(len(pairs)):
                a, b = pairs[x]

                for y in range(x + 1, len(pairs)):
                    c, d = pairs[y]

                    if c != a and c != b and d != a and d != b:
                        candidate = [a, b, c, d]

                        if best is None or candidate < best:
                            best = candidate

                        found = True
                        break

                if found:
                    break

        return best if best is not None else fallback

        # Complexity analysis
        # Time : O(N^2) pairs, plus the scan inside each group
        # Space : O(N^2)


def p2():
    # Problem 2 : POTD Geeksforgeeks Two Pairs with Same Sum - https://www.geeksforgeeks.org/problems/satisfy-the-equation5847/1

    testcase = [
        [[1, 5, 3, 7, 4, 2], [0, 1, 4, 5]],
        [[2, 2, 2, 2], [0, 1, 2, 3]],
        [[1, 2, 3], [-1, -1, -1, -1]],
        [[5, 1, 1, 1, 1], [1, 2, 3, 4]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.findPairs(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        N = len(nums)
        answer = [1] * N

        # answer[i] first holds the product of everything to the left of i
        prefix = 1
        for i in range(N):
            answer[i] = prefix
            prefix *= nums[i]

        # then multiply in the product of everything to the right of i
        suffix = 1
        for i in range(N - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

        # Complexity analysis
        # Time : O(N)
        # Space : O(1) extra, the output array is not counted


def p3():
    # Problem 3 : NC150 Leetcode 238. Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[1, 2, 3, 4], [24, 12, 8, 6]],
        [[-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]],
        [[2, 3], [3, 2]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.productExceptSelf(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 24 of November 2026

    p1()

    p2()

    p3()
