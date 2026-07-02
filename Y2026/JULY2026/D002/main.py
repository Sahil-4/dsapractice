from collections import deque


class Solution1:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        INF = float("inf")

        minimum_health_loss = [[INF] * cols for _ in range(rows)]

        minimum_health_loss[0][0] = grid[0][0]

        queue = deque([(0, 0)])

        while queue:
            current_row, current_col = queue.popleft()

            current_loss = minimum_health_loss[current_row][current_col]

            for row_offset, col_offset in directions:
                next_row = current_row + row_offset
                next_col = current_col + col_offset

                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                    continue

                next_loss = current_loss + grid[next_row][next_col]

                if next_loss >= minimum_health_loss[next_row][next_col]:
                    continue

                minimum_health_loss[next_row][next_col] = next_loss

                if grid[next_row][next_col] == 0:
                    queue.appendleft((next_row, next_col))
                else:
                    queue.append((next_row, next_col))

        return minimum_health_loss[rows - 1][cols - 1] < health

        # Complexity analysis
        # Time : O(M * N)
        # Space : O(M * N)


def p1():
    # Problem 1 : POTD Leetcode 3286. Find a Safe Walk Through a Grid - https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/?envType=daily-question&envId=2026-07-02

    testcase = [
        [
            [
                [0, 1, 0, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 1, 0],
            ],
            1,
            True,
        ],
        [
            [
                [0, 1, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 0],
                [0, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0],
            ],
            3,
            False,
        ],
        [
            [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1],
            ],
            5,
            True,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.findSafeWalk(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def divisibleByK(self, arr: list[int], k: int) -> bool:
        n = len(arr)

        # pigeonhole:
        # If there are more than k elements, some non-empty subset
        # must have a sum divisible by k.
        if n > k:
            return True

        # reachable remainders modulo k
        reachable = [False] * k

        for value in arr:
            # subset with sum divisible by k already exists
            if reachable[0]:
                return True

            # new remainders formed using the current value
            next_reachable = [False] * k

            # extend previously reachable remainders
            for remainder in range(k):
                if not reachable[remainder]:
                    continue

                next_remainder = (remainder + value) % k

                if not reachable[next_remainder]:
                    next_reachable[next_remainder] = True

            # merge newly reachable remainders
            for remainder in range(k):
                if next_reachable[remainder]:
                    reachable[remainder] = True

            # subset containing only the current element
            reachable[value % k] = True

        return reachable[0]

        # Complexity analysis
        # Time : O(N * K)
        # Space : O(K)


def p2():
    # Problem 2 : POTD Geeksforgeeks Check Subset sum divisible by k - https://www.geeksforgeeks.org/problems/subset-with-sum-divisible-by-m2546/1

    testcase = [
        [[3, 1, 7, 5], 6, True],
        [[1, 2, 6], 5, False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.divisibleByK(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 2 of July 2026

    p1()

    p2()
