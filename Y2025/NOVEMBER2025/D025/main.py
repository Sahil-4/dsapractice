class Solution1:
    def smallestRepunitDivByK(self, k: int) -> int:
        # 1 = n % k
        # n contains only '1'

        rem = 0
        for nlen in range(1, k + 1, 1):
            rem = (rem * 10 + 1) % k
            if rem == 0:
                return nlen

        return -1

        # Complexity analysis
        # Time : O(K)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1015. Smallest Integer Divisible by K - https://leetcode.com/problems/smallest-integer-divisible-by-k/description/?envType=daily-question&envId=2025-11-25

    testcase = [
        [1, 1],
        [2, -1],
        [3, 3],
    ]

    for line in testcase:
        [k, expected] = line
        s1 = Solution1()
        result = s1.smallestRepunitDivByK(k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution2:
    def subarrayXor(self, arr):
        # code here
        # XOR = x ^ x = 0 (even case)
        # XOR = x ^ x ^ x = x (odd case)

        result = 0
        arr_len = len(arr)

        for i in range(arr_len):
            contribution_count = (i + 1) * (arr_len - i)

            if contribution_count & 1:
                result ^= arr[i]

        return result

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Game of XOR - https://www.geeksforgeeks.org/problems/game-of-xor1541/1

    testcase = [
        [[1, 2, 3], 2],
        [[1, 2], 0],
        [[1, 2, 3, 5, 4, 7], 0],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.subarrayXor(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 25 of November 2025

    p1()

    p2()
