from bisect import bisect_left


class Solution1:
    def missingMultiple(self, nums: list[int], k: int) -> int:

        nums_copy = set(nums)

        for ki in range(k, max(nums_copy) + k + k, k):
            if ki not in nums_copy:
                return ki

        return -1

        # Complexity analysis
        # Time : O(N + M)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3718. Smallest Missing Multiple of K - https://leetcode.com/problems/smallest-missing-multiple-of-k/description/?envType=daily-question&envId=2026-08-25

    testcase = [
        [[8, 2, 3, 4, 6], 2, 10],
        [[1, 4, 7, 10, 15], 5, 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.missingMultiple(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minMoves(self, arr: list[int]) -> int:
        N = len(arr)

        # pos[value] = index of value in arr
        pos = [0] * (N + 1)

        for index, value in enumerate(arr):
            pos[value] = index

        # Find the longest consecutive sequence
        # whose values are already in increasing order.
        longest = 1
        current = 1

        for value in range(1, N):
            if pos[value] < pos[value + 1]:
                current += 1
                longest = max(longest, current)
            else:
                current = 1

        return N - longest

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Moves to Sort Permutation - https://www.geeksforgeeks.org/problems/morning-assembly3038/1

    testcase = [
        [[2, 1, 3], 1],
        [[4, 3, 1, 2], 2],
        [[1, 3, 2, 4], 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minMoves(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 25 of August 2026

    p1()

    p2()
