from typing import List


class Solution1:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        """
        ans[i] or (ans[i] + 1) == nums[i]
        nums[i] = ans[i] or (ans[i] + 1)
        by observation
        if x = (101001)
        (x+1) = (101010)
        x or (x+1) ie. 101001 or 101010
        101001 or 101010 = 101011
        update last zero bit to one
        reverse engineering
        on (101011) iterate from least significant bit
        find first zero bit and update bit before this to zero
        this will get us x
        now from x we can get (x+1)
        """

        result = []

        for num in nums:
            if num == 2:
                result.append(-1)
                continue

            found = False
            for j in range(1, 32):
                if (num & (1 << j)) > 0:
                    continue

                result.append(num ^ (1 << (j - 1)))
                found = True
                break

            if not found:
                result.append(-1)

        return result

        # Complexity analysis
        # Time : O(N * 32)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3315. Construct the Minimum Bitwise Array II - https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/description/?envType=daily-question&envId=2026-01-21

    testcase = [
        [[2, 3, 5, 7], [-1, 1, 4, 3]],
        [[11, 13, 31], [9, 12, 15]],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.minBitwiseArray(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def calculateSpan(self, arr):
        # code here
        # Stock Span = distance to previous greater element
        # use monotonic stack store index of prev greater element index
        # Once a higher price comes, all smaller prices before it can be discarded

        stack = []  # will store indices
        span = []

        for i in range(len(arr)):
            # remove all smaller or equal prices
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()

            if not stack:
                span.append(i + 1)
            else:
                span.append(i - stack[-1])

            stack.append(i)

        return span

        # Complexity analysis
        # Time : O(2N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Stock span problem - https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1

    testcase = [
        [[100, 80, 90, 120], [1, 1, 2, 4]],
        [[10, 4, 5, 90, 120, 80], [1, 1, 2, 4, 5, 1]],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.calculateSpan(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 21 of January 2026

    p1()

    p2()
