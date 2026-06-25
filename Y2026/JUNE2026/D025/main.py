class Solution1:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        N = len(nums)
        subarray_count = 0

        for left in range(N):
            target_count = 0

            for right in range(left, N):
                if nums[right] == target:
                    target_count += 1

                length = right - left + 1

                if target_count * 2 > length:
                    subarray_count += 1

        return subarray_count

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3737. Count Subarrays With Majority Element I - https://leetcode.com/problems/count-subarrays-with-majority-element-i/?envType=daily-question&envId=2026-06-25

    testcase = [
        [[1, 2, 2, 3], 2, 5],
        [[1, 1, 1, 1], 1, 10],
        [[1, 2, 3], 4, 0],
    ]

    for line in testcase:
        [nums, target, expected] = line
        s1 = Solution1()
        result = s1.countMajoritySubarrays(nums, target)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def increasingNumbers(self, n: int) -> list:
        # code here
        nums = []

        if n >= 10:
            return nums

        if n == 1:
            nums.append(0)

        def solve(N: int, prev: int = 0, num: int = 0):
            if N == 0:
                nums.append(num)
                return

            for i in range(prev + 1, 10):
                num = (num * 10) + i
                solve(N - 1, i, num)
                num = num // 10

        solve(n)

        return nums

        # Complexity analysis
        # Time : O(C(9, n))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks N-Digit Numbers with Increasing Digits - https://www.geeksforgeeks.org/problems/n-digit-numbers-with-digits-in-increasing-order5903/1

    testcase = [
        [
            1,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        ],
        [
            2,
            [
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                34,
                35,
                36,
                37,
                38,
                39,
                45,
                46,
                47,
                48,
                49,
                56,
                57,
                58,
                59,
                67,
                68,
                69,
                78,
                79,
                89,
            ],
        ],
        [
            15,
            [],
        ],
    ]

    for line in testcase:
        [n, expected] = line
        s2 = Solution2()
        result = s2.increasingNumbers(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 25 of June 2026

    p1()

    p2()
