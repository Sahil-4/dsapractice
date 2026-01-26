from typing import List


class Solution1:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # find minimum absolute difference between elemnent of pairs say min_diff
        # find all pairs with difference equal to min_diff
        # to find pairs efficiently we must sort the given list
        # since elements are distinct element wont pair like this
        # [a, b, c] => [a,b], [a,c] (X)
        # instead of applying two pass we can do this in one pass also
        # as once we get a min diff all previous pairs will be of no use

        arr.sort()

        N = len(arr)

        # find min_diff and all min_diff_pairs
        min_diff = float("inf")
        min_diff_pairs = []
        for i in range(1, N):
            if min_diff > arr[i] - arr[i - 1]:
                min_diff = arr[i] - arr[i - 1]
                min_diff_pairs.clear()

            if arr[i] - arr[i - 1] == min_diff:
                min_diff_pairs.append([arr[i - 1], arr[i]])

        return min_diff_pairs

        # Complexity analysis
        # Time : O(N * Log(N)) + O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1200. Minimum Absolute Difference - https://leetcode.com/problems/minimum-absolute-difference/description/?envType=daily-question&envId=2026-01-26

    testcase = [
        [[4, 2, 1, 3], [[1, 2], [2, 3], [3, 4]]],
        [[1, 3, 6, 10, 15], [[1, 3]]],
        [[3, 8, -10, 23, 19, -4, -14, 27], [[-14, -10], [19, 23], [23, 27]]],
    ]

    for line in testcase:
        [arr, expected] = line
        s1 = Solution1()
        result = s1.minimumAbsDifference(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def permuteDist(self, arr):
        # code here
        permutations = []

        N = len(arr)

        def backtrack(idx):
            if idx == N:
                permutations.append(arr[:])
                return

            for i in range(idx, N):
                arr[idx], arr[i] = arr[i], arr[idx]
                backtrack(idx + 1)
                arr[idx], arr[i] = arr[i], arr[idx]

        backtrack(0)

        return permutations

        # Complexity analysis
        # Time : O(N! * N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Generate Permutations of an array - https://www.geeksforgeeks.org/problems/generate-permutations-of-an-array/1

    testcase = [
        [
            [1, 2, 3],
            [
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1],
            ],
        ],
        [
            [1, 3],
            [
                [1, 3],
                [3, 1],
            ],
        ],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.permuteDist(arr)
        result.sort()
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 26 of January 2026

    p1()

    p2()
