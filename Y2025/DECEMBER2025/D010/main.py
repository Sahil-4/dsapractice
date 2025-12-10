from typing import List


class Solution1:
    def countPermutations(self, complexity: List[int]) -> int:
        N = len(complexity)
        MOD = 1000000007
        ans = 1

        for i in range(1, N):
            if complexity[i] <= complexity[0]:
                return 0

            ans = (ans * i) % MOD

        return ans

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3577. Count the Number of Computer Unlocking Permutations - https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/description/?envType=daily-question&envId=2025-12-10

    testcase = [
        [[1, 2, 3], 2],
        [[3, 3, 3, 4, 4, 4], 0],
    ]

    for line in testcase:
        [complexity, expected] = line
        s1 = Solution1()
        result = s1.countPermutations(complexity)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findTwoElement(self, arr):
        N = len(arr)
        F = N + 1

        # Mark frequencies
        for i in range(N):
            el = (arr[i] % F) - 1
            arr[el] += F

        twice = 0
        arr_sum = 0

        for i in range(N):
            arr_sum += arr[i] % F
            if arr[i] // F >= 2:
                twice = i + 1

        sum_of_n = N * (N + 1) // 2
        missing = sum_of_n - (arr_sum - twice)

        return [twice, missing]

        # Complexity analysis
        # Time : O(2N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Missing And Repeating - https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1

    testcase = [
        [[2, 2], [2, 1]],
        [[1, 3, 3], [3, 2]],
        [[4, 3, 6, 2, 1, 1], [1, 5]],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.findTwoElement(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 10 of December 2025

    p1()

    p2()
