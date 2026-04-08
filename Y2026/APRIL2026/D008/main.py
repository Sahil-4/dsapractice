from typing import List


class Solution1:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1000000007

        for query in queries:
            [li, ri, ki, vi] = query

            idx = li
            while idx <= ri:
                nums[idx] = (nums[idx] * vi) % MOD
                idx += ki

        nums_xor = 0
        for num in nums:
            nums_xor = nums_xor ^ num

        return nums_xor

        # Complexity analysis
        # Time : O(Q * N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3653. XOR After Range Multiplication Queries I - https://leetcode.com/problems/xor-after-range-multiplication-queries-i/description/?envType=daily-question&envId=2026-04-08

    testcase = [
        [
            [1, 1, 1],
            [[0, 2, 1, 4]],
            4,
        ],
        [
            [2, 3, 1, 5, 4],
            [[1, 4, 2, 3], [0, 2, 1, 2]],
            31,
        ],
    ]

    for line in testcase:
        [nums, queries, expected] = line
        s1 = Solution1()
        result = s1.xorAfterQueries(nums, queries)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def segregate0and1(self, arr):
        # code here

        N = len(arr)

        l = 0  # holds zero
        r = N - 1  # holds one

        # at any point if l does not hold 0 and
        # r does not hold 1 then
        # swap both

        while l < r:
            if arr[l] == 0:
                l += 1
            elif arr[r] == 1:
                r -= 1
            else:
                arr[l], arr[r] = arr[r], arr[l]

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Segregate 0s and 1s - https://www.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1

    testcase = [
        [
            [0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        ],
        [
            [1, 1],
            [1, 1],
        ],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        s2.segregate0and1(arr)
        result = arr
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 8 of April 2026

    p1()

    p2()
