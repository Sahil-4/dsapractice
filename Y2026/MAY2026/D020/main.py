from typing import List


class Solution1:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        N = len(A)

        C = [0] * N

        set_a = set()
        set_b = set()

        for i in range(N):
            """
            # Naive approach : O(N^2)
            set_a.add(A[i])
            set_b.add(B[i])

            common_elements = set_a.intersection(set_b)
            C[i] = len(common_elements)
            """

            C[i] = C[i - 1] if i > 0 else 0

            if A[i] in set_b:
                C[i] += 1
            set_a.add(A[i])

            if B[i] in set_a:
                C[i] += 1
            set_b.add(B[i])

        return C

        # Complexity Analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2657. Find the Prefix Common Array of Two Arrays - https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/?envType=daily-question&envId=2026-05-20

    testcase = [
        [[1, 3, 2, 4], [3, 1, 2, 4], [0, 2, 3, 4]],
        [[2, 3, 1], [3, 1, 2], [0, 1, 3]],
    ]

    for line in testcase:
        [A, B, expected] = line
        s1 = Solution1()
        result = s1.findThePrefixCommonArray(A, B)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def isProduct(self, arr: list[int], target: int) -> bool:
        # code here
        arr_copy = arr.copy()
        arr_copy.sort()

        left, right = 0, len(arr_copy) - 1

        while left < right:
            product = arr_copy[left] * arr_copy[right]
            if product == target:
                return True
            elif product < target:
                left += 1
            else:
                right -= 1

        return False

        # Complexity Analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Product Pair - https://www.geeksforgeeks.org/problems/equal-to-product3836/1

    testcase = [
        [[10, 20, 9, 40], 400, True],
        [[-10, 20, 9, -40], 30, False],
        [[-10, 0, 9, -40], 0, True],
    ]

    for line in testcase:
        [arr, target, expected] = line
        s2 = Solution2()
        result = s2.isProduct(arr, target)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 20 of May 2026

    p1()

    p2()
