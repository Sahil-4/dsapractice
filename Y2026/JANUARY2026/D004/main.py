from typing import List


class Solution1:
    def divisors_sum(self, ne: int) -> int:
        divisors = []

        i = 1
        while i * i <= ne:
            if ne % i == 0:
                divisors.append(i)
                if ne / i != i:
                    divisors.append(ne / i)

            i += 1

        return int(sum(divisors, 0)) if len(divisors) == 4 else 0

    def sumFourDivisors(self, nums: List[int]) -> int:
        sum = 0

        for num in nums:
            sum += self.divisors_sum(num)

        return sum

        # Complexity analysis
        # Time : O(N * sqrt(num))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1390. Four Divisors - https://leetcode.com/problems/four-divisors/description/?envType=daily-question&envId=2026-01-04

    testcase = [
        [[21, 4, 7], 32],
        [[21, 21], 64],
        [[1, 2, 3, 4, 5], 0],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.sumFourDivisors(nums)
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
    # Day 4 of January 2026

    p1()

    p2()
