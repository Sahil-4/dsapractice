from bisect import bisect_left


class Solution1:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        max_num = max(nums)

        # frequency of x
        freq = [0] * (max_num + 1)
        for num in nums:
            freq[num] += 1

        # number of pairs whose gcd is exactly g
        exact = [0] * (max_num + 1)

        for g in range(max_num, 0, -1):

            # count numbers divisible by g
            cnt = 0
            for multiple in range(g, max_num + 1, g):
                cnt += freq[multiple]

            pairs = cnt * (cnt - 1) // 2

            # remove pairs already counted by multiples of g
            for multiple in range(g * 2, max_num + 1, g):
                pairs -= exact[multiple]

            exact[g] = pairs

        # prefix[i] = number of pairs with gcd <= i
        prefix = [0] * (max_num + 1)
        for g in range(1, max_num + 1):
            prefix[g] = prefix[g - 1] + exact[g]

        values = []
        for q in queries:
            # first gcd whose prefix count exceeds q
            values.append(bisect_left(prefix, q + 1))

        return values

        # Complexity analysis
        # Time : O(Max(nums) * log(Max(nums)) + Q * log(Max(nums)))
        # Space : O(Max(nums))


def p1():
    # Problem 1 : POTD Leetcode 3312. Sorted GCD Pair Queries - https://leetcode.com/problems/sorted-gcd-pair-queries/description/?envType=daily-question&envId=2026-07-17

    testcase = [
        [[2, 3, 4], [0, 2, 2], [1, 2, 2]],
        [[4, 4, 2, 1], [5, 3, 1, 0], [4, 2, 1, 1]],
        [[2, 2], [0, 0], [2, 2]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.gcdValues(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxDiffSubArrays(self, arr: list[int]) -> int:
        N = len(arr)

        max_left = [0] * N
        min_left = [0] * N
        max_right = [0] * N
        min_right = [0] * N

        # maximum subarray sum for every prefix
        curr = best = arr[0]
        max_left[0] = best
        for i in range(1, N):
            curr = max(arr[i], curr + arr[i])
            best = max(best, curr)
            max_left[i] = best

        # minimum subarray sum for every prefix
        curr = best = arr[0]
        min_left[0] = best
        for i in range(1, N):
            curr = min(arr[i], curr + arr[i])
            best = min(best, curr)
            min_left[i] = best

        # maximum subarray sum for every suffix
        curr = best = arr[-1]
        max_right[-1] = best
        for i in range(N - 2, -1, -1):
            curr = max(arr[i], curr + arr[i])
            best = max(best, curr)
            max_right[i] = best

        # minimum subarray sum for every suffix
        curr = best = arr[-1]
        min_right[-1] = best
        for i in range(N - 2, -1, -1):
            curr = min(arr[i], curr + arr[i])
            best = min(best, curr)
            min_right[i] = best

        ans = 0

        for i in range(N - 1):
            ans = max(
                ans,
                abs(max_left[i] - min_right[i + 1]),
                abs(min_left[i] - max_right[i + 1]),
            )

        return ans

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Absolute Diff of Two Subarrays - https://www.geeksforgeeks.org/problems/max-absolute-difference4114/1

    testcase = [
        [[-2, -3, 4, -1, -2, 1, 5, -3], 12],
        [[2, -1, -2, 1, -4, 2, 8], 16],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxDiffSubArrays(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 17 of July 2026

    p1()

    p2()
