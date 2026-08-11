class Solution1:
    def missingInteger(self, nums: list[int]) -> int:
        N = len(nums)

        longest_sequential_prefix_sum = nums[0]
        for j in range(1, N):
            if nums[j] - nums[j - 1] != 1:
                break
            longest_sequential_prefix_sum += nums[j]

        search_set = list(nums)
        search_set.sort()
        x = longest_sequential_prefix_sum

        for num in search_set:
            if x < num:
                return x

            if x == num:
                x += 1

        return x

        # Complexity analysis
        # Time : O(N) + O(N * Log(N)) + O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum - https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/description/?envType=daily-question&envId=2026-08-11

    testcase = [
        [[1, 2, 3, 2, 5], 6],
        [[3, 4, 5, 1, 12, 14, 13], 15],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.missingInteger(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def largestSquare(
        self, mat: list[list[int]], queries: list[list[int]], k: int
    ) -> list[int]:

        R = len(mat)
        C = len(mat[0])

        # 1. build 2D prefix sum
        # prefix[i + 1][j + 1] = number of 1s in
        # mat[0..i][0..j]

        prefix = [[0] * (C + 1) for _ in range(R + 1)]

        for i in range(R):
            row_sum = 0

            for j in range(C):
                row_sum += mat[i][j]

                prefix[i + 1][j + 1] = prefix[i][j + 1] + row_sum

        # helper: number of 1s in rectangle
        # (r1, c1) -> (r2, c2), inclusive
        def get_sum(r1: int, c1: int, r2: int, c2: int) -> int:
            return (
                prefix[r2 + 1][c2 + 1]
                - prefix[r1][c2 + 1]
                - prefix[r2 + 1][c1]
                + prefix[r1][c1]
            )

        ans = []

        # 2. Process every query
        for i, j in queries:

            # maximum possible radius before leaving matrix
            max_radius = min(i, j, R - 1 - i, C - 1 - j)

            left = 0
            right = max_radius

            best = -1

            # binary search on radius
            while left <= right:

                mid = (left + right) // 2

                r1 = i - mid
                r2 = i + mid
                c1 = j - mid
                c2 = j + mid

                ones = get_sum(r1, c1, r2, c2)

                if ones <= k:
                    # current square is valid
                    best = mid

                    # try a larger square
                    left = mid + 1
                else:
                    # too many 1s - try smaller square
                    right = mid - 1

            if best == -1:
                # No valid square exists
                ans.append(-1)
            else:
                # radius -> odd side length
                ans.append(2 * best + 1)

        return ans

        # Complexity analysis
        # Time : O(R*C + Q*Log(min(R, C)))
        # Space : O(R*C)


def p2():
    # Problem 2 : POTD Geeksforgeeks Largest Odd Squares with Limited 1s - https://www.geeksforgeeks.org/problems/largest-square-in-a-binary-matrix-with-at-most-k-1s-for-multiple-queries/1

    testcase = [
        [
            [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]],
            [[1, 2]],
            9,
            [3],
        ],
        [
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            [[1, 1], [2, 2]],
            9,
            [3, 1],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.largestSquare(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 11 of August 2026

    p1()

    p2()
