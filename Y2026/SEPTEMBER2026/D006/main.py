from collections import deque


class Solution1:
    def numDistinct(self, s: str, t: str) -> int:
        SN = len(s)
        TN = len(t)

        dp_next = [0 for _ in range(TN + 1)]
        dp_next[TN] = 1

        for si in range(SN - 1, -1, -1):
            dp_curr = [0 for _ in range(TN + 1)]
            dp_curr[TN] = 1

            for ti in range(TN - 1, -1, -1):

                # skip
                dp_curr[ti] += dp_next[ti]

                # take
                if s[si] == t[ti]:
                    dp_curr[ti] += dp_next[ti + 1]

            dp_next = dp_curr

        return dp_next[0]

        # Complexity analysis
        # Time : O(SN * TN)
        # Space : O(2 * TN)


def p1():
    # Problem 1 : POTD Leetcode 115. Distinct Subsequences - https://leetcode.com/problems/distinct-subsequences/description/?envType=daily-question&envId=2026-09-06

    testcase = [
        ["rabbbit", "rabbit", 3],
        ["babgbag", "bag", 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.numDistinct(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def pairAndSum(self, arr: list[int]) -> int:
        # code here

        pair_sum = 0

        for k in range(32):
            set_count = 0
            for e in arr:
                set_count += 1 if e >> k & 1 else 0

            pairs = set_count * (set_count - 1) // 2
            contribution = pairs * 2**k

            pair_sum += contribution

        return pair_sum

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Sum of Pairwise ANDs - https://www.geeksforgeeks.org/problems/sum-of-products5049/1

    testcase = [
        [[5, 10, 15], 15],
        [[10, 20, 30, 40], 46],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.pairAndSum(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        EMPTY_CELL = 0
        FRESH_ORANGE = 1
        ROTTEN_ORANGE = 2

        M = len(grid)
        N = len(grid[0])

        queue: deque[tuple[int, int, int]] = deque()  # (r,c,t)

        # check if cell is valid or not
        def can_move(r: int, c: int) -> bool:
            check = True

            # check cell index
            check = check and r >= 0 and r < M
            check = check and c >= 0 and c < N

            # check blocking cell
            check = check and grid[r][c] == FRESH_ORANGE

            return check

        # initially rotten oranges - starting points
        for r in range(M):
            for c in range(N):
                if grid[r][c] != ROTTEN_ORANGE:
                    continue

                queue.append((r, c, 0))

        # run bfs - find the max time to rot all oranges
        max_time = 0
        while queue:
            r, c, t = queue.popleft()

            max_time = max(max_time, t)

            # explore 4 adjacent cells - top, right, bottom, left
            moves = [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]
            for mr, mc in moves:
                if not can_move(mr, mc):
                    continue

                queue.append((mr, mc, t + 1))
                grid[mr][mc] = ROTTEN_ORANGE

        # ensure all oranges are rotten - return -1 if not
        for r in range(M):
            for c in range(N):
                if grid[r][c] == FRESH_ORANGE:
                    return -1

        return max_time

        # Complexity analysis
        # Time : O(M*N)
        # Space : O(M*N)


def p3():
    # Problem 3 : NC150 Leetcode 994. Rotting Oranges - https://leetcode.com/problems/rotting-oranges/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4],
        [[[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1],
        [[[0, 2]], 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.orangesRotting(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        copy_nums = sorted(nums)
        N = len(copy_nums)

        triplets: list[list[int]] = []

        for i in range(N):
            if i > 0 and copy_nums[i] == copy_nums[i - 1]:
                continue

            l, r = i + 1, N - 1

            while l < r:
                tsum = copy_nums[i] + copy_nums[l] + copy_nums[r]

                if tsum == 0:
                    triplets.append([copy_nums[i], copy_nums[l], copy_nums[r]])
                    r -= 1
                    l += 1

                    while l < r and copy_nums[r] == copy_nums[r + 1]:
                        r -= 1

                    while l < r and copy_nums[l] == copy_nums[l - 1]:
                        l += 1

                elif tsum > 0:
                    r -= 1
                else:
                    l += 1

        return triplets

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(N)


def p4():
    # Problem 4 : NC150 Leetcode 15. 3Sum - https://leetcode.com/problems/3sum/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]],
        [[0, 1, 1], []],
        [[0, 0, 0], [[0, 0, 0]]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.threeSum(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


class Solution5:
    def letterCombinations(self, digits: str) -> list[str]:
        key_mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        N = len(digits)

        combinations = []

        def helper(di: int, combination: list[str]) -> None:
            if di == N:
                combinations.append("".join(combination))
                return

            for mapped_char in key_mapping.get(digits[di], []):
                combination.append(mapped_char)
                helper(di + 1, combination)
                combination.pop()

        helper(0, [])

        return combinations

        # Complexity analysis
        # Time : O(3^N)
        # Space : O(N)


def p5():
    # Problem 5 : NC150 Leetcode 17. Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]],
        ["2", ["a", "b", "c"]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s5 = Solution5()
        result = s5.letterCombinations(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P5): result={result}")


if __name__ == "__main__":
    # Day 6 of September 2026

    p1()

    p2()

    p3()

    p4()

    p5()

