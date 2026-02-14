class Solution1:
    def champagne_memoization(
        self, poured: int, query_row: int, query_glass: int
    ) -> float:
        memo = [[-1.0 for _ in range(101)] for _ in range(101)]

        def solve(i, j):
            if i < 0 or j < 0 or j > i:
                return 0.0

            if i == 0 and j == 0:
                return poured

            if memo[i][j] != -1.0:
                return memo[i][j]

            up_left = (solve(i - 1, j - 1) - 1) / 2.0
            up_right = (solve(i - 1, j) - 1) / 2.0

            up_left = max(0.0, up_left)
            up_right = max(0.0, up_right)

            memo[i][j] = up_left + up_right
            return memo[i][j]

        return min(1.0, solve(query_row, query_glass))

        # Complexity analysis
        # Time : O(query_row*query_row)
        # Space : O(query_row*query_row)

    def champagne_tabulation(
        self, poured: int, query_row: int, query_glass: int
    ) -> float:
        dp = [[0.0 for _ in range(101)] for _ in range(101)]
        dp[0][0] = float(poured)

        for row in range(query_row + 1):
            for col in range(row + 1):
                excess = (dp[row][col] - 1.0) / 2.0
                if excess > 0:
                    dp[row + 1][col] += excess
                    dp[row + 1][col + 1] += excess

        return min(1.0, dp[query_row][query_glass])

        # Complexity analysis
        # Time : O(query_row*query_row)
        # Space : O(query_row*query_row)

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # return self.champagne_memoization(poured, query_row, query_glass)
        return self.champagne_tabulation(poured, query_row, query_glass)


def p1():
    # Problem 1 : POTD Leetcode 799. Champagne Tower - https://leetcode.com/problems/champagne-tower/description/?envType=daily-question&envId=2026-02-14

    testcase = [
        [1, 1, 1, 0.00000],
        [2, 1, 1, 0.50000],
        [100000009, 33, 17, 1.00000],
    ]

    for line in testcase:
        [poured, query_row, query_glass, expected] = line
        s1 = Solution1()
        result = s1.champagneTower(poured, query_row, query_glass)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minTime(self, arr, k):
        # code here

        # Helper function to check if we can paint within 'max_time'
        def possible_answer(max_time):
            painters = 1
            current_sum = 0

            for board in arr:
                # If a single board is larger than max_time → not possible
                if board > max_time:
                    return False

                if current_sum + board <= max_time:
                    current_sum += board
                else:
                    painters += 1
                    current_sum = board

                    if painters > k:
                        return False

            return True

        low = max(arr)
        high = sum(arr)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            if possible_answer(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

        # Complexity analysis
        # Time  : O(N * log(sum(arr)))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks The Painter's Partition Problem-II - https://www.geeksforgeeks.org/problems/the-painters-partition-problem1535/1

    testcase = [
        [[5, 10, 30, 20, 15], 3, 35],
        [[10, 20, 30, 40], 2, 60],
        [[100, 200, 300, 400], 1, 1000],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.minTime(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 14 of February 2026

    p1()

    p2()
