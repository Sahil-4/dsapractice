class Solution1:
    def smallestNumber(self, n: int, t: int) -> int:

        def digit_product(x: int) -> int:
            product = 1

            while x > 0:
                digit = x % 10
                product *= digit
                x //= 10

            return product

        while True:
            if digit_product(n) % t == 0:
                return n

            n += 1

        # Complexity analysis
        # Time : O((O - N + 1) * Log(N))
        # Space: O(1)


def p1():
    # Problem 1 : POTD Leetcode 3345. Smallest Divisible Digit Product I - https://leetcode.com/problems/smallest-divisible-digit-product-i/description/?envType=daily-question&envId=2026-08-06

    testcase = [
        [10, 2, 10],
        [15, 3, 16],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.smallestNumber(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countMinOperations(self, arr: list[int]) -> int:
        nums = arr.copy()
        operations = 0

        while True:
            if all(val == 0 for val in nums):
                break

            # undo all increment operations - odds
            for i in range(len(nums)):
                if nums[i] % 2:
                    nums[i] -= 1
                    operations += 1

            # undo one doubling operation - even
            if any(val > 0 for val in nums):
                for i in range(len(nums)):
                    nums[i] //= 2
                operations += 1

        return operations

        # Complexity analysis
        # Time : O(N * Log(max(arr)))
        # Space: O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Increment or Double Operations to Convert - https://www.geeksforgeeks.org/problems/minimum-steps-to-get-desired-array5519/1

    testcase = [
        [[16, 16, 16], 7],
        [[2, 3], 4],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.countMinOperations(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 6 of August 2026

    p1()

    p2()
