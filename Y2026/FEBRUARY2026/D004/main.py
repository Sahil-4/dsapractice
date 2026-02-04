from typing import List, Optional


class Solution1:
    def maxSumTrionic(self, nums: List[int]) -> int:
        # [0, ..., p, ..., q, ...]
        # [l..., p, ..., q, ...r]
        # consider [l,p], [p,q], and [q,r] are trends
        # at every we have option to keep current element in current trend
        # or move to next trend
        # for this we obey some rules

        n = len(nums)
        NEG_INF = -(10**18)

        # memo[i][trend]
        memo: List[List[Optional[int]]] = [[None] * 4 for _ in range(n + 1)]

        def solve(i: int, trend: int) -> int:
            if i == n:
                if trend == 3:
                    return 0
                return NEG_INF

            if memo[i][trend] is not None:
                return memo[i][trend]

            take = NEG_INF
            skip = NEG_INF

            # skip (only allowed at trend 0)
            if trend == 0:
                skip = solve(i + 1, 0)

            # if already in last increasing phase, can end here
            if trend == 3:
                take = nums[i]

            if i + 1 < n:
                curr = nums[i]
                nxt = nums[i + 1]

                if trend == 0 and nxt > curr:
                    take = max(take, curr + solve(i + 1, 1))

                elif trend == 1:
                    if nxt > curr:
                        take = max(take, curr + solve(i + 1, 1))
                    elif nxt < curr:
                        take = max(take, curr + solve(i + 1, 2))

                elif trend == 2:
                    if nxt < curr:
                        take = max(take, curr + solve(i + 1, 2))
                    elif nxt > curr:
                        take = max(take, curr + solve(i + 1, 3))

                elif trend == 3 and nxt > curr:
                    take = max(take, curr + solve(i + 1, 3))

            memo[i][trend] = max(take, skip)
            return memo[i][trend]

        return solve(0, 0)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3640. Trionic Array II - https://leetcode.com/problems/trionic-array-ii/description/?envType=daily-question&envId=2026-02-04

    testcase = [
        [[0, -2, -1, -3, 0, 2, -1], -4],
        [[1, 4, 2, 7], 14],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.maxSumTrionic(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def getLastMoment(self, n, left, right):
        # code here
        # collision is not an issue
        # there will be no effect of collision
        # because when two ants collide, and swap their paths and distance
        # so we just have to return the maximum distance,
        # traveled by any ant,
        # to reach the end
        # n = 4, left = [3], right = [1]
        # 0 1 2 3 4 - plank
        # 0 > 2 < 4 - ants position and direction
        # . 3 . 3 . - time taken by ant to reach end
        # 3 - output

        max_dist = 0

        for dist in left:
            max_dist = max(max_dist, dist)

        for dist in right:
            max_dist = max(max_dist, n - dist)

        return max_dist

        # Complexity analysis
        # Time : O(N + M)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Last Moment Before All Ants Fall Out - https://www.geeksforgeeks.org/problems/last-moment-before-all-ants-fall-out-of-a-plank/1

    testcase = [
        [4, [2], [0, 1, 3], 4],
        [4, [], [0, 1, 2, 3, 4], 4],
        [3, [0], [3], 0],
    ]

    for line in testcase:
        [n, left, right, expected] = line
        s2 = Solution2()
        result = s2.getLastMoment(n, left, right)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 4 of February 2026

    p1()

    p2()
