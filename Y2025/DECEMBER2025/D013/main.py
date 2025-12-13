from typing import List
import re


class Solution1:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        N = len(code)
        valid_business_lines = ["electronics", "grocery", "pharmacy", "restaurant"]

        def is_valid(index: int) -> bool:
            if not isActive[i]:
                return False
            if not businessLine[i] in valid_business_lines:
                return False
            return bool(re.fullmatch(r"[A-Za-z0-9_]+", code[i]))

        valid_coupons_dict = {
            business_line: [] for business_line in valid_business_lines
        }

        for i in range(N):
            if not is_valid(i):
                continue
            valid_coupons_dict[businessLine[i]].append(code[i])

        valid_coupons_list = []
        for business_line in valid_business_lines:
            valid_coupons_dict[business_line].sort()
            valid_coupons_list.extend(valid_coupons_dict[business_line])

        return valid_coupons_list

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3606. Coupon Code Validator - https://leetcode.com/problems/coupon-code-validator/description/?envType=daily-question&envId=2025-12-13

    testcase = [
        [
            ["SAVE20", "", "PHARMA5", "SAVE@20"],
            ["restaurant", "grocery", "pharmacy", "restaurant"],
            [True, True, True, True],
            ["PHARMA5", "SAVE20"],
        ],
        [
            ["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"],
            ["grocery", "electronics", "invalid"],
            [False, True, True],
            ["ELECTRONICS_50"],
        ],
        [
            ["mCSqZMoS", "402apYyk"],
            ["grocery", "restaurant"],
            [False, True],
            ["402apYyk"],
        ],
    ]

    for line in testcase:
        [code, businessLine, isActive, expected] = line
        s1 = Solution1()
        result = s1.validateCoupons(code, businessLine, isActive)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def swapDiagonal(self, mat):
        # code here
        # R = rows
        # run a loop from i = 0, i < R
        # at each iteration
        # swap mat[i][i], mat[i][N-1-i]

        N = len(mat)

        for i in range(N):
            [mat[i][i], mat[i][N - 1 - i]] = [mat[i][N - 1 - i], mat[i][i]]

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Swap diagonals - https://www.geeksforgeeks.org/problems/swap-major-and-minor-diagonals-of-a-square-matrix/1

    testcase = [
        [
            [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
            [[2, 1, 0], [3, 4, 5], [8, 7, 6]],
        ],
        [
            [[0, 1], [2, 3]],
            [[1, 0], [3, 2]],
        ],
        [
            [
                [0, 1, 2, 3, 4, 5],
                [7, 8, 9, 10, 11, 12],
                [1, 1, 1, 1, 1, 1],
                [2, 2, 2, 2, 2, 2],
                [2, 3, 2, 3, 4, 5],
                [7, 8, 9, 8, 7, 8],
            ],
            [
                [5, 1, 2, 3, 4, 0],
                [7, 11, 9, 10, 8, 12],
                [1, 1, 1, 1, 1, 1],
                [2, 2, 2, 2, 2, 2],
                [2, 4, 2, 3, 3, 5],
                [8, 8, 9, 8, 7, 7],
            ],
        ],
    ]

    for line in testcase:
        [mat, expected] = line
        s2 = Solution2()
        s2.swapDiagonal(mat)
        result = mat
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 13 of December 2025

    p1()

    p2()
