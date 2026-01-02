from typing import List


class Solution1:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # total elements = 2N
        # unique elements = N
        # special element frequency = N
        # to separate all special element we can at max have two distance
        # special = [1,1,1], unique = [2,3,4]
        # arrangement = [1,2,1,3,1,4]
        # hence if (nums[i] == nums[i + 1]) or (nums[i] == nums[i + 2])
        # then nums[i] is the special element
        # we may not find this true at some index but as special elements are always possible
        # we will be able to find this condition true at some index

        NN = len(nums)
        for i in range(NN - 2):
            if nums[i] == nums[i + 1] or nums[i] == nums[i + 2]:
                return nums[i]

        return nums[-1]  # defensive fallback, will never be used for valid inputs

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 961. N-Repeated Element in Size 2N Array - https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/?envType=daily-question&envId=2026-01-02

    testcase = [
        [[1, 2, 3, 3], 3],
        [[2, 1, 2, 5, 3, 2], 2],
        [[5, 1, 5, 2, 5, 3, 5, 4], 5],
        [[9, 5, 6, 9], 9],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.repeatedNTimes(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def sort012(self, arr):
        # code here
        # arr[] = [0, 1, 2, 0, 1, 2]
        # use three pointers
        # z = 0 for zero
        # o = 0 for one
        # t = N-1 for two
        # run while o <= t
        # check using j
        # if nums[j] is 1 move forward
        # else if nums[j] is 2 swap it t
        # and move only t
        # else if nums[j] is 0 swap it z
        # and move z and o

        N = len(arr)

        z = 0
        o = 0
        t = N - 1

        while o <= t:
            if arr[o] == 1:
                o += 1
            elif arr[o] == 2:
                arr[o], arr[t] = arr[t], arr[o]
                t -= 1
            else:
                arr[o], arr[z] = arr[z], arr[o]
                z += 1
                o += 1

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Sort 0s, 1s and 2s - https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

    testcase = [
        [
            [0, 1, 2, 0, 1, 2],
            [0, 0, 1, 1, 2, 2],
        ],
        [
            [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2],
        ],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        s2.sort012(arr)
        result = arr
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 2 of January 2026

    p1()

    p2()
