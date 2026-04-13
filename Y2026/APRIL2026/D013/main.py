from typing import List


class Solution1:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        N = len(nums)

        diff = N

        for index, num in enumerate(nums):
            if num == target:
                diff = min(diff, abs(index - start))

        return diff

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1848. Minimum Distance to the Target Element - https://leetcode.com/problems/minimum-distance-to-the-target-element/description/?envType=daily-question&envId=2026-04-13

    testcase = [
        [[1, 2, 3, 4, 5], 5, 3, 1],
        [[1], 1, 0, 0],
        [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 0, 0],
    ]

    for line in testcase:
        [nums, target, start, expected] = line
        s1 = Solution1()
        result = s1.getMinDistance(nums, target, start)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def nextPalindrome(self, num: List[int]) -> List[int]:
        # code here
        # as per given constraints
        # smallest palindrome possible is [1, 1, ....., 1]
        # largest palindrome possible is [9, 9, ....., 9]

        N = len(num)

        # case 1: all digits are 9
        if all(d == 9 for d in num):
            return [1] + [0] * (N - 1) + [1]

        # case 2: mirrored num > original num
        res = num[:]
        i, j = 0, N - 1
        while i < j:
            res[j] = res[i]
            i += 1
            j -= 1

        if res > num:
            return res

        # case 3: increase mid
        carry = 1
        mid = N // 2

        if N % 2 == 1:
            res[mid] += 1
            carry = res[mid] // 10
            res[mid] %= 10
            i = mid - 1
            j = mid + 1
        else:
            i = mid - 1
            j = mid

        # propagate carry
        while i >= 0 and carry:
            res[i] += carry
            carry = res[i] // 10
            res[i] %= 10
            res[j] = res[i]
            i -= 1
            j += 1

        # mirror remaining
        while i >= 0:
            res[j] = res[i]
            i -= 1
            j += 1

        return res

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Next Smallest Palindrome - https://www.geeksforgeeks.org/problems/next-smallest-palindrome4740/1

    testcase = [
        [[9, 4, 1, 8, 7, 9, 7, 8, 3, 2, 2], [9, 4, 1, 8, 8, 0, 8, 8, 1, 4, 9]],
        [[2, 3, 5, 4, 5], [2, 3, 6, 3, 2]],
        [[2, 4, 5, 6], [2, 5, 5, 2]],
    ]

    for line in testcase:
        [num, expected] = line
        s2 = Solution2()
        result = s2.nextPalindrome(num)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 13 of April 2026

    p1()

    p2()
