from typing import List


class Solution1:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
            1: [[0, -1], [0, 1]],
            2: [[-1, 0], [1, 0]],
            3: [[0, -1], [1, 0]],
            4: [[0, 1], [1, 0]],
            5: [[0, -1], [-1, 0]],
            6: [[-1, 0], [0, 1]],
        }

        M = len(grid)
        N = len(grid[0])

        visited = [[False] * N for _ in range(M)]

        can_move_to_cell = lambda i, j: 0 <= i < M and 0 <= j < N and not visited[i][j]

        def dfs(i, j) -> bool:
            # reached to destination
            if i == M - 1 and j == N - 1:
                return True

            # mark visited
            visited[i][j] = True

            # move to next cell
            for direction in directions[grid[i][j]]:
                new_i = i + direction[0]
                new_j = j + direction[1]

                if not can_move_to_cell(new_i, new_j):
                    continue

                # both streets connected
                for back_direction in directions[grid[new_i][new_j]]:
                    back_i = new_i + back_direction[0]
                    back_j = new_j + back_direction[1]

                    if back_i == i and back_j == j:
                        # can reach to destination through this path
                        if dfs(new_i, new_j):
                            return True

            return False

        return dfs(0, 0)

        # Complexity analysis
        # Time : O(M*N)
        # Space : O(M*N)


def p1():
    # Problem 1 : POTD Leetcode 1391. Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/description/?envType=daily-question&envId=2026-04-27

    testcase = [
        [[[2, 4, 3], [6, 5, 2]], True],
        [[[1, 2, 1], [1, 2, 1]], False],
        [[[1, 1, 2]], False],
    ]

    for line in testcase:
        [grid, expected] = line
        s1 = Solution1()
        result = s1.hasValidPath(grid)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def smallestSubstring(self, s: str) -> int:
        # code here

        N = len(s)
        slen = N + 1

        mp = dict()
        l = 0

        for r in range(N):
            if s[r] not in mp:
                mp[s[r]] = 0

            mp[s[r]] += 1

            while len(mp) == 3:
                slen = min(slen, r - l + 1)
                mp[s[l]] -= 1
                if mp[s[l]] == 0:
                    del mp[s[l]]
                l += 1

        return slen if slen <= N else -1

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Smallest window containing 0, 1 and 2 - https://www.geeksforgeeks.org/problems/smallest-window-containing-0-1-and-2--170637/1

    testcase = [
        ["10212", 3],
        ["12121", -1],
        ["120", 3],
    ]

    for line in testcase:
        [s, expected] = line
        s2 = Solution2()
        result = s2.smallestSubstring(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 27 of April 2026

    p1()

    p2()
