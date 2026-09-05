class Solution1:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        N = len(nums)

        min_right = nums[:]
        for i in range(N - 2, -1, -1):
            min_right[i] = min(min_right[i], min_right[i + 1])

        max_left_i = nums[0]
        for i in range(N):
            max_left_i = max(max_left_i, nums[i])
            instability_score = max_left_i - min_right[i]
            if instability_score <= k:
                return i

        return -1

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3904. Smallest Stable Index II - https://leetcode.com/problems/smallest-stable-index-ii/?envType=daily-question&envId=2026-09-05

    testcase = [
        [[5, 0, 1, 4], 3, 3],
        [[3, 2, 1], 1, -1],
        [[0], 0, 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.firstStableIndex(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def longestSubseq(self, arr: list[int]) -> int:
        # code here

        N = len(arr)

        longest_subsequence_length = [1] * N
        last_index_of = dict()

        last_index_of[arr[0]] = 0

        for i in range(1, N):
            val1 = arr[i] + 1
            val2 = arr[i] - 1

            if val1 in last_index_of:
                longest_subsequence_length[i] = max(
                    longest_subsequence_length[i],
                    1 + longest_subsequence_length[last_index_of[val1]],
                )

            if val2 in last_index_of:
                longest_subsequence_length[i] = max(
                    longest_subsequence_length[i],
                    1 + longest_subsequence_length[last_index_of[val2]],
                )

            last_index_of[arr[i]] = i

        return max(longest_subsequence_length)

        # Complexity analysis
        # Time : O(N)
        # Space : O(2N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Longest Subsequence with Adjacent Diff as 1 - https://www.geeksforgeeks.org/problems/longest-sub-sequence-such-that-difference-between-adjacents-is-one2558/1

    testcase = [
        [[10, 9, 4, 5, 4, 8, 6], 3],
        [[1, 2, 3, 2, 3, 7, 2, 1], 7],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.longestSubseq(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def maxArea(self, height: list[int]) -> int:

        N = len(height)

        max_area = 0

        ptr1 = 0
        ptr2 = N - 1

        while ptr1 < ptr2:

            area = min(height[ptr1], height[ptr2]) * (ptr2 - ptr1)
            max_area = max(max_area, area)

            if height[ptr1] <= height[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1

        return max_area

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 11. Container With Most Water - https://leetcode.com/problems/container-with-most-water/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[1, 8, 6, 2, 5, 4, 8, 3, 7], 49],
        [[1, 1], 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.maxArea(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 5 of September 2026

    p1()

    p2()

    p3()
