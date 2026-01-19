from typing import List


class Solution1:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # use prefix sum (2D)
        # apply binary search on square size k
        # if found valid k size square
        # decrement search space to right
        # else decrement search space to left

        m, n = len(mat), len(mat[0])

        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j]

        def valid(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    total = ps[i][j] - ps[i - k][j] - ps[i][j - k] + ps[i - k][j - k]
                    if total <= threshold:
                        return True
            return False

        lo, hi, ans = 0, min(m, n), 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if valid(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans

        # Complexity analysis
        # Time : O(Log(min(N, M)) * N*M)
        # Space : O(N*M)


def p1():
    # Problem 1 : POTD Leetcode 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold - https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/description/?envType=daily-question&envId=2026-01-19

    testcase = [
        [
            [
                [1, 1, 3, 2, 4, 3, 2],
                [1, 1, 3, 2, 4, 3, 2],
                [1, 1, 3, 2, 4, 3, 2],
            ],
            4,
            2,
        ],
        [
            [
                [2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2],
            ],
            1,
            0,
        ],
    ]

    for line in testcase:
        [mat, threshold, expected] = line
        s1 = Solution1()
        result = s1.maxSideLength(mat, threshold)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def removeKdig(self, s, k):
        # code here
        # if removing ith digit
        # we get a smaller digit on ith index
        # then its benificial to delete ith digit
        # else we must try next index
        # edge:
        # there may be a case like this s = "123", k = some integer < slen
        # in this case at last we will see remaining k
        # for this we can remove last k digit in s
        # this will be solved using stack

        stack = []

        for ch in s:
            while stack and k > 0 and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        # If k digits still need to be removed, remove from the end
        if k > 0:
            stack = stack[:-k]

        # Remove leading zeros
        result = "".join(stack).lstrip("0")

        return result if result else "0"

        # Complexity analysis
        # Time : O(2N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Remove K Digits - https://www.geeksforgeeks.org/problems/remove-k-digits/1

    testcase = [
        ["4325043", 3, "2043"],
        ["765028321", 5, "221"],
    ]

    for line in testcase:
        [s, k, expected] = line
        s2 = Solution2()
        result = s2.removeKdig(s, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 19 of January 2026

    p1()

    p2()
