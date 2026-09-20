class Solution1:
    def reverseDegree(self, s: str) -> int:
        reverse_degree_sum = 0

        N = len(s)

        for index in range(1, N + 1):
            ch = s[index - 1]
            position = 26 - (ord(ch) - ord("a"))
            reverse_degree = position * index

            reverse_degree_sum += reverse_degree

        return reverse_degree_sum

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3498. Reverse Degree of a String - https://leetcode.com/problems/reverse-degree-of-a-string/description/?envType=daily-question&envId=2026-09-20

    testcase = [
        ["abc", 148],
        ["zaza", 160],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.reverseDegree(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def largestSubsquare(self, mat: list[list[str]]) -> int:
        N = len(mat)

        # right[i][j] = consecutive X's going right
        right = [[0] * N for _ in range(N)]

        # down[i][j] = consecutive X's going down
        down = [[0] * N for _ in range(N)]

        # Step 1: precompute right and down
        for i in range(N - 1, -1, -1):
            for j in range(N - 1, -1, -1):

                if mat[i][j] == "X":
                    right[i][j] = 1
                    down[i][j] = 1

                    right[i][j] = 1 if j == N - 1 else right[i][j + 1] + 1
                    down[i][j] = 1 if i == N - 1 else down[i + 1][j] + 1

        # Step 2: check all possible squares
        max_side_length = 0

        # for every top-left corner
        for i in range(N):
            for j in range(N):

                # Start with the largest possible square
                max_possible = min(right[i][j], down[i][j])

                # try possible side length -
                # only which can give better answer than current
                for k in range(max_possible, 0, -1):

                    # check all four boundaries
                    if right[i + k - 1][j] >= k and down[i][j + k - 1] >= k:
                        max_side_length = max(max_side_length, k)
                        break

        return max_side_length

        # Complexity analysis
        # Time : O(N^3)
        # Space : O(N^2)


def p2():
    # Problem 2 : POTD Geeksforgeeks Largest Subsquare Surrounded by X - https://www.geeksforgeeks.org/problems/largest-subsquare-surrounded-by-x0558/1

    testcase = [
        [
            [
                ["X", "X", "X", "O"],
                ["X", "O", "X", "X"],
                ["X", "X", "X", "O"],
                ["X", "O", "X", "X"],
            ],
            3,
        ],
        [
            [
                ["X", "X"],
                ["X", "X"],
            ],
            2,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.largestSubsquare(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def maxSubArray(self, nums: list[int]) -> int:
        N = len(nums)

        max_subarray_sum = -(10**8)
        _subarray_sum = 0

        for index in range(N - 1, -1, -1):

            subarray_sum = nums[index] + _subarray_sum
            max_subarray_sum = max(max_subarray_sum, subarray_sum)

            _subarray_sum = max([0, nums[index], subarray_sum])

        return max_subarray_sum

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 53. Maximum Subarray - https://leetcode.com/problems/maximum-subarray/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[-2, 1, -3, 4, -1, 2, 1, -5, 4], 6],
        [[1], 1],
        [[5, 4, -1, 7, 8], 23],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.maxSubArray(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 20 of September 2026

    p1()

    p2()

    p3()
