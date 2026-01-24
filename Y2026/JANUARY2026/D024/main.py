from typing import List


class Solution1:
    def minPairSum(self, nums: List[int]) -> int:
        # we have to make pair in such a way that
        # one element will be minimum and another will be maximum
        # this will give us minimum sum
        # to solve this
        # we just have to sort the array
        # use two pointers (one will also work)
        # take left element from beginning and (N - left - 1) element from end
        # calculate sum and update maximum pair sum

        N = len(nums)

        maximum_pair_sum = 0

        nums.sort()

        left = 0
        while left < N // 2:
            sum = nums[left] + nums[N - left - 1]
            maximum_pair_sum = max(maximum_pair_sum, sum)

            left += 1

        return maximum_pair_sum

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1877. Minimize Maximum Pair Sum in Array - https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/?envType=daily-question&envId=2026-01-24

    testcase = [
        [[3, 5, 2, 3], 7],
        [[3, 5, 4, 2, 4, 6], 8],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.minPairSum(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def josephus(self, n, k):
        # code here
        # n = 3, k = 3
        # 1 2 3
        # 1 2 [3]
        # [1] 2
        # 2
        # instead of simulating kills,
        # use a pattern
        # f(n) = survivor position when counting starts from 0 (0-based index)
        # f(1) = 0
        # f(n) = (f(n-1) + k) % n
        # after one person is killed, the circle “shrinks”
        # and survivor’s index shifts by k
        # to keep it circular we do %n

        res = 0  # f(1)
        for i in range(2, n + 1):
            res = (res + k) % i
        return res + 1  # convert to 1-based

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Josephus problem - https://www.geeksforgeeks.org/problems/josephus-problem/1

    testcase = [
        [5, 2, 3],
        [7, 3, 4],
    ]

    for line in testcase:
        [n, k, expected] = line
        s2 = Solution2()
        result = s2.josephus(n, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 24 of January 2026

    p1()

    p2()
