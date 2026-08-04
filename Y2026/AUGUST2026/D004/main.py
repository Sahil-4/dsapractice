from bisect import bisect_left


class Solution1:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        missing = []

        nums_set = set(nums)
        min_num = min(nums)
        max_num = max(nums)

        for num in range(min_num, max_num):
            if num not in nums_set:
                missing.append(num)

        return missing

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3731. Find Missing Elements - https://leetcode.com/problems/find-missing-elements/?envType=daily-question&envId=2026-08-04

    testcase = [
        [[1, 4, 2, 5], [3]],
        [[7, 8, 6, 9], []],
        [[5, 1], [2, 3, 4]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.findMissingElements(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countPairs(self, arr: list[int], k: int) -> int:
        # code here
        # arr[] = [1, 10, 4, 2], k = 3
        # arr[] = [1, 2, 4, 10], k = 3
        # [1-2], [2-4]

        pair_count = 0

        arr_copy = arr.copy()
        arr_copy.sort()
        N = len(arr_copy)

        for i in range(N):
            j = bisect_left(arr_copy, arr_copy[i] + k, i + 1, N)
            pair_count += j - i - 1

        return pair_count

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Pairs with Less Than K Diff - https://www.geeksforgeeks.org/problems/pairs-with-difference-less-than-k1348/1

    testcase = [
        [[1, 10, 4, 2], 3, 2],
        [[2, 3, 4], 5, 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.countPairs(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 4 of August 2026

    p1()

    p2()
