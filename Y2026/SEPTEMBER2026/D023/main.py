class Solution1:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        target = total - x

        # we need to keep a subarray whose sum is total - x
        if target < 0:
            return -1

        # if target == 0, remove every element
        if target == 0:
            return len(nums)

        left = 0
        window_sum = 0
        max_len = -1

        for right, num in enumerate(nums):
            window_sum += num

            # shrink window until its sum <= target
            while left <= right and window_sum > target:
                window_sum -= nums[left]
                left += 1

            # found a valid subarray
            if window_sum == target:
                max_len = max(max_len, right - left + 1)

        return -1 if max_len == -1 else len(nums) - max_len

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1658. Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/?envType=daily-question&envId=2026-09-23

    testcase = [
        [[1, 1, 4, 2, 3], 5, 2],
        [[5, 6, 7, 8, 9], 4, -1],
        [[3, 2, 20, 1, 1, 3], 10, 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minOperations(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def formPyramid(self, arr: list[int]) -> int:
        # code here

        N = len(arr)

        height_sum = sum(arr)

        if N <= 2:
            return height_sum - 1

        left_peak = [0] * N
        right_peak = [0] * N

        left_peak[0] = 1
        for i in range(1, N):
            left_peak[i] = min(arr[i], left_peak[i - 1] + 1)

        right_peak[N - 1] = 1
        for i in range(N - 2, -1, -1):
            right_peak[i] = min(arr[i], right_peak[i + 1] + 1)

        min_cost = 10**12
        for i in range(N):
            peak_height = min(left_peak[i], right_peak[i])
            pyramid_sum = peak_height * peak_height

            min_cost = min(min_cost, height_sum - pyramid_sum)

        return min_cost

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Pyramid Array with Reduce Operations - https://www.geeksforgeeks.org/problems/pyramid-form3044/1

    testcase = [
        [[1, 2, 3, 4, 2, 1], 4],
        [[1, 2, 1], 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.formPyramid(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        M = len(s1)
        N = len(s2)

        if M > N:
            return False

        s1_frequency = [0] * 26
        s2_frequency = [0] * 26

        def contains_same_characters() -> bool:
            for idx in range(26):
                if s1_frequency[idx] != s2_frequency[idx]:
                    return False

            return True

        for c in s1:
            idx = ord(c) - ord("a")
            s1_frequency[idx] += 1

        i = 0
        while i < M:
            idx = ord(s2[i]) - ord("a")
            s2_frequency[idx] += 1

            i += 1

        if contains_same_characters():
            return True

        while i < N:
            # add right character
            idx = ord(s2[i]) - ord("a")
            s2_frequency[idx] += 1

            # remove left character
            idx = ord(s2[i - M]) - ord("a")
            s2_frequency[idx] -= 1

            i += 1

            if contains_same_characters():
                return True

        return False

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 567. Permutation in String - https://leetcode.com/problems/permutation-in-string/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["ab", "eidbaooo", True],
        ["ab", "eidboaoo", False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.checkInclusion(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 23 of September 2026

    p1()

    p2()

    p3()
