from typing import List


class Solution1:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k

        # Complexity analysis
        # Time : O(N)
        # Time : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3512. Minimum Operations to Make Array Sum Divisible by K - https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/description/?envType=daily-question&envId=2025-11-29

    testcase = [
        [[3, 9, 7], 5, 4],
        [[4, 1, 3], 4, 0],
        [[3, 2], 6, 5],
    ]

    for line in testcase:
        [nums, k, expected] = line
        s1 = Solution1()
        result = s1.minOperations(nums, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countSetBits(self, n):
        total = 0
        i = 0

        # all bit positions until 2^i > n
        while (1 << i) <= n:
            block_size = 1 << (i + 1)
            half_block = 1 << i

            # contributed by complete blocks
            full_blocks = n // block_size
            total += full_blocks * half_block

            # remaining partial block
            remainder = n % block_size
            total += max(0, remainder - half_block + 1)

            i += 1

        return total

        # Complexity analysis
        # Time : O(Log(N))
        # Time : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count set bits - https://www.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1

    testcase = [
        [4, 5],
        [17, 35],
    ]

    for line in testcase:
        [n, expected] = line
        s2 = Solution2()
        result = s2.countSetBits(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 29 of November 2025

    p1()

    p2()
