class Solution1:
    def judgeCircle(self, moves: str) -> bool:
        # simulation

        origin = [0, 0]

        for move in moves:
            if move == "U":
                origin[0] += 1
            elif move == "D":
                origin[0] -= 1
            elif move == "L":
                origin[1] += 1
            elif move == "R":
                origin[1] -= 1
            else:
                # invalid move
                pass

        return origin == [0, 0]

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 657. Robot Return to Origin - https://leetcode.com/problems/robot-return-to-origin/description/?envType=daily-question&envId=2026-04-05

    testcase = [
        ["UD", True],
        ["LL", False],
    ]

    for line in testcase:
        [moves, expected] = line
        s1 = Solution1()
        result = s1.judgeCircle(moves)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def totalWays(self, arr, target):
        # code here
        # recursion
        # either put +, or -
        totalSum = sum(arr)

        # Edge case check
        if (target + totalSum) % 2 != 0 or abs(target) > totalSum:
            return 0

        subset_sum = (target + totalSum) // 2

        # DP array
        dp = [0] * (subset_sum + 1)
        dp[0] = 1

        for num in arr:
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[subset_sum]

        # Complexity analysis
        # Time : O(N * sum)
        # Time : O(sum)


def p2():
    # Problem 2 : POTD Geeksforgeeks Target Sum - https://www.geeksforgeeks.org/problems/target-sum-1626326450/1

    testcase = [
        [[1, 1, 1, 1, 1], 3, 5],
        [[1, 2, 3], 2, 1],
    ]

    for line in testcase:
        [arr, target, expected] = line
        s2 = Solution2()
        result = s2.totalWays(arr, target)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 5 of April 2026

    p1()

    p2()
