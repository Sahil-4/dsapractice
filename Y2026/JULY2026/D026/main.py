class Solution1:
    def maximumProduct(self, nums: list[int]) -> int:
        # two possibilities for the maximum product of three numbers:
        # 1. product of the three largest numbers
        # 2. product of the two smallest numbers (which could be negative) and the largest number

        EDGE = 1000

        first_smallest = EDGE
        second_smallest = EDGE
        first_largest = -EDGE
        second_largest = -EDGE
        third_largest = -EDGE

        for num in nums:
            if num < first_smallest:
                second_smallest = first_smallest
                first_smallest = num
            elif num < second_smallest:
                second_smallest = num

            if num > first_largest:
                third_largest = second_largest
                second_largest = first_largest
                first_largest = num
            elif num > second_largest:
                third_largest = second_largest
                second_largest = num
            elif num > third_largest:
                third_largest = num

        product1 = first_largest * second_largest * third_largest
        product2 = first_smallest * second_smallest * first_largest

        return max(product1, product2)

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 628. Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/?envType=daily-question&envId=2026-07-26

    testcase = [
        [[1, 2, 3], 6],
        [[1, 2, 3, 4], 24],
        [[-1, -2, -3], -6],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maximumProduct(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def levelSort(self, arr: list[int]) -> list[list[int]]:
        # code here
        level_sorted = []

        N = len(arr)
        level = 1
        si = 0

        while si < N:
            ei = min(si + level, N)
            level_sorted.append(sorted(arr[si:ei]))
            si = ei
            level *= 2

        return level_sorted

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Complete Binary Tree Traversal with Array Input - https://www.geeksforgeeks.org/problems/print-binary-tree-levels-in-sorted-order3241/1

    testcase = [
        [[7, 6, 5, 4, 3, 2, 1], [[7], [5, 6], [1, 2, 3, 4]]],
        [[7, 16, 1, 4, 13], [[7], [1, 16], [4, 13]]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.levelSort(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 26 of July 2026

    p1()

    p2()
