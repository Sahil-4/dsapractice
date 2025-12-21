from typing import List
from bisect import bisect_left, bisect_right


class Solution1:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        sorted_pairs = [False] * (n - 1)
        deletions = 0

        for col in range(m):
            bad = False

            # check violation
            for row in range(n - 1):
                if not sorted_pairs[row] and strs[row][col] > strs[row + 1][col]:
                    bad = True
                    break

            if bad:
                deletions += 1
                continue

            # update sorted pairs
            for row in range(n - 1):
                if not sorted_pairs[row] and strs[row][col] < strs[row + 1][col]:
                    sorted_pairs[row] = True

        return deletions

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 955. Delete Columns to Make Sorted II - https://leetcode.com/problems/delete-columns-to-make-sorted-ii/description/?envType=daily-question&envId=2025-12-21

    testcase = [
        [["ca", "bb", "ac"], 1],
        [["xc", "yb", "za"], 0],
        [["zyx", "wvu", "tsr"], 3],
    ]

    for line in testcase:
        [strs, expected] = line
        s1 = Solution1()
        result = s1.minDeletionSize(strs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countXInRange(self, arr, queries):
        # code here
        # for each query q
        # in range [l,r] have to perform two operations for x
        # find first occurrence of x and
        # find last occurrence of x
        # count[qi] = last - first + 1
        # if x not found in range [l,r]
        # count[qi] = 0

        N = len(arr)
        QN = len(queries)
        count = []

        for i in range(QN):
            [l, r, x] = queries[i]

            left = bisect_left(arr, x, l, r + 1)
            right = bisect_right(arr, x, l, r + 1)
            count.append(right - left)

        return count

        # Complexity analysis
        # Time : O(Q * Log(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count X in Range of a Sorted Array - https://www.geeksforgeeks.org/problems/count-x-in-range-of-a-sorted-array/1

    testcase = [
        [[1, 2, 2, 4, 5, 5, 5, 8], [[0, 7, 5], [1, 2, 2], [0, 3, 7]], [3, 2, 0]],
        [[1, 3, 3, 3, 6, 7, 8], [[0, 3, 3], [4, 6, 3], [1, 5, 6]], [3, 0, 1]],
    ]

    for line in testcase:
        [arr, queries, expected] = line
        s2 = Solution2()
        result = s2.countXInRange(arr, queries)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 21 of December 2025

    p1()

    p2()
