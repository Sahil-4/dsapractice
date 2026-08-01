from functools import lru_cache


class Solution1:
    def predictTheWinner(self, nums: list[int]) -> bool:

        @lru_cache(maxsize=None)
        def solve(
            l: int, r: int, player: int, player1_points: int, player2_points: int
        ) -> bool:
            if l > r:
                return player1_points >= player2_points

            # player 1 turn
            if player == 0:
                return (
                    # leftmost number
                    solve(l + 1, r, 1, player1_points + nums[l], player2_points)
                    or
                    # rightmost number
                    solve(l, r - 1, 1, player1_points + nums[r], player2_points)
                )

            # player 2 turn
            return (
                # leftmost number
                solve(l + 1, r, 0, player1_points, player2_points + nums[l])
                and
                # rightmost number
                solve(l, r - 1, 0, player1_points, player2_points + nums[r])
            )

        return solve(0, len(nums) - 1, 0, 0, 0)

        # Complexity Analysis
        # Time : O(min(2^N, N^2 * S))
        # Space : O(min(2^N, N^2 * S)) + O(N)


def p1():
    # Problem 1 : POTD Leetcode 486. Predict the Winner - https://leetcode.com/problems/predict-the-winner/description/?envType=daily-question&envId=2026-08-01

    testcase = [
        [[1, 5, 2], False],
        [[1, 5, 233, 7], True],
        [[1, 5, 21, 5, 233, 7, 5, 233, 71, 5, 21], False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.predictTheWinner(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findMax(self, N: int, a: list[int], b: list[int], k: list[int]) -> int:
        # code here

        M = len(a)
        arr = [0] * N

        for i in range(M):
            s = a[i]
            e = b[i]
            inc = k[i]

            arr[s] += inc
            if e + 1 < N:
                arr[e + 1] -= inc

        for i in range(1, N):
            arr[i] += arr[i - 1]

        return max(arr)

        # Complexity Analysis
        # Time : O(M + N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max After m Range Increments - https://www.geeksforgeeks.org/problems/max-value-after-m-range-operation4300/1

    testcase = [
        [5, [0, 1, 2], [1, 4, 3], [100, 100, 100], 200],
        [4, [1, 0, 3], [2, 0, 3], [603, 286, 882], 882],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.findMax(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 1 of August 2026

    p1()

    p2()
