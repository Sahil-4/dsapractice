from typing import List


class Solution1:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        # do whatever is asked
        # we have to move to index i + (nums[i])
        # and use its value for result[i]

        N = len(nums)

        result = [0] * N

        for i in range(N):
            circular_index = (i + nums[i]) % N
            result[i] = nums[circular_index]

        return result

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3379. Transformed Array - https://leetcode.com/problems/transformed-array/description/?envType=daily-question&envId=2026-02-05

    testcase = [
        [[3, -2, 1, 1], [1, 1, 1, 3]],
        [[-1, 4, -1], [-1, -1, 4]],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.constructTransformedArray(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxOnes(self, arr, k):
        # code here
        # sliding window and two pointer

        l = 0
        zeros = 0
        max_len = 0

        for r in range(len(arr)):
            if arr[r] == 0:
                zeros += 1

            while zeros > k:
                if arr[l] == 0:
                    zeros -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len

        # Complexity analysis
        # Time : O(2N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Maximize Number of 1's - https://www.geeksforgeeks.org/problems/maximize-number-of-1s0905/1

    testcase = [
        [[1, 0, 1], 1, 3],
        [[1, 0, 0, 1, 0, 1, 0, 1], 2, 5],
        [[1, 1], 2, 2],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.maxOnes(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 5 of February 2026

    p1()

    p2()
