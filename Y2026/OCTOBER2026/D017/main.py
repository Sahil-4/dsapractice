class Solution1:
    @staticmethod
    def _get_digit_sum(num: int) -> int:
        """Computes the sum of digits of a non-negative integer."""

        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        return total

    def min_swaps_to_target(self, target_order_indices: list[int]) -> int:
        """
        Generic helper: computes the minimum number of swaps needed to
        sort an array given each element's original index in the desired sorted order.

        target_order_indices[i] represents which original array index
        belongs at position i in the final sorted array.
        """

        N = len(target_order_indices)
        visited = [False] * N
        total_swaps = 0

        for i in range(N):
            if visited[i] or target_order_indices[i] == i:
                continue

            cycle_length = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = target_order_indices[curr]
                cycle_length += 1

            if cycle_length > 1:
                total_swaps += cycle_length - 1

        return total_swaps

    def minSwaps(self, nums: list[int]) -> int:
        """
        Calculates the minimum swaps to sort nums by:
        1. Digit sum (ascending)
        2. Value (ascending, tie-breaker)
        """
        # Step 1: Precompute sort keys alongside original indices
        # Key format: (digit_sum, value)
        indexed_items = [
            (self._get_digit_sum(val), val, idx) for idx, val in enumerate(nums)
        ]

        # Step 2: Sort items by (digit_sum, val)
        indexed_items.sort(key=lambda item: (item[0], item[1]))

        # Step 3: Extract the permutation mapping
        # target_indices[i] tells which original index ends up at position i
        target_indices = [item[2] for item in indexed_items]

        # Step 4: Calculate swaps via cycle decomposition
        return self.min_swaps_to_target(target_indices)

        # Complexity analysis
        # Time : O(N Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3551. Minimum Swaps to Sort by Digit Sum - https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/description/?envType=daily-question&envId=2026-10-17

    testcase = [
        [[37, 100], 1],
        [[22, 14, 33, 7], 0],
        [[18, 43, 34, 16], 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minSwaps(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def isItPossible(self, s1: str, s2: str) -> bool:
        # code here

        # A and B can not cross each other
        # A can move to left only,
        # B can move to right only
        # # are empty positions

        N = len(s1)
        M = len(s2)

        if N != M:
            return False

        i = j = 0

        while i < N or j < M:

            while i < N and s1[i] == "#":
                i += 1
            while j < N and s2[j] == "#":
                j += 1

            if i == N or j == M:
                return i == N and j == M

            if s1[i] != s2[j]:
                return False

            if s1[i] == "A" and i < j:
                return False

            if s1[i] == "B" and i > j:
                return False

            i += 1
            j += 1

        return True

        # Complexity analysis
        # Time : O(N+M)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Convert One String to Another with Constraints - https://www.geeksforgeeks.org/problems/check-if-it-is-possible-to-convert-one-string-into-another-with-given-constraints4116/1

    testcase = [
        ["#A#B#B#", "A###B#B", True],
        ["#A#B#", "#B#A#", False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.isItPossible(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


from collections import deque


class Solution3:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board or not board[0]:
            return

        M, N = len(board), len(board[0])
        queue = deque()

        # Step 1: Add all border 'O's to the queue and mark them as 'S'
        for r in range(M):
            for c in (0, N - 1):
                if board[r][c] == "O":
                    board[r][c] = "S"
                    queue.append((r, c))

        for c in range(N):
            for r in (0, M - 1):
                if board[r][c] == "O":
                    board[r][c] = "S"
                    queue.append((r, c))

        # Step 2: BFS to mark all connected 'O' cells as safe ('S')
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < M and 0 <= nc < N and board[nr][nc] == "O":
                    board[nr][nc] = "S"
                    queue.append((nr, nc))

        # Step 3: Final sweep - 'O' -> 'X', 'S' -> 'O'
        for r in range(M):
            for c in range(N):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"

        # Complexity analysis
        # Time : O(N*M)
        # Space : O(N*M)


def p3():
    # Problem 3 : NC150 Leetcode 130. Surrounded Regions - https://leetcode.com/problems/surrounded-regions/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
            ],
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"],
            ],
        ],
        [
            [["X"]],
            [["X"]],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        s3.solve(*inputs)
        result = inputs[0]
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 17 of October 2026

    p1()

    p2()

    p3()
