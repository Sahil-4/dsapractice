from collections import deque


class Solution1:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        r1x1, r1y1, r1x2, r1y2 = rec1
        r2x1, r2y1, r2x2, r2y2 = rec2

        x_overlap = max(r1x1, r2x1) < min(r1x2, r2x2)
        y_overlap = max(r1y1, r2y1) < min(r1y2, r2y2)

        return x_overlap and y_overlap

        # Complexity analysis
        # Time : O(1)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 836. Rectangle Overlap - https://leetcode.com/problems/rectangle-overlap/description/?envType=daily-question&envId=2026-09-14

    testcase = [
        [[0, 0, 2, 2], [1, 1, 3, 3], True],
        [[0, 0, 1, 1], [1, 0, 2, 1], False],
        [[0, 0, 1, 1], [2, 2, 3, 3], False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.isRectangleOverlap(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def shortestPath(self, mat: list[list[int]]) -> int:
        # code here

        N = len(mat)
        M = len(mat[0])

        DIRECTION_DELTA = [(-1, 0), (0, +1), (+1, 0), (0, -1)]

        # initially all cells are safe
        board = [[1 for _ in range(M)] for _ in range(N)]

        # marking cells unsafe
        for i in range(N):
            for j in range(M):
                if mat[i][j] != 0:
                    continue

                # cell itself
                board[i][j] = 0

                # adjacent cells
                for x, y in DIRECTION_DELTA:
                    r, c = i + x, j + y
                    if r >= 0 and r < N and c >= 0 and c < M:
                        board[r][c] = 0

        # starting points board[r][0]
        # ending point board[r][M-1]
        # condition board[r][c] != 0
        # find the hops/steps
        # return minimum
        # DFS/BFS can be used to find the number of steps required to reach from (sr,sc) -> (er,M-1)

        # multi-source BFS
        queue = deque()
        dist = [[-1 for _ in range(M)] for _ in range(N)]

        # safe cell in the first column is a source
        for r in range(N):
            if board[r][0] != 0:
                queue.append((r, 0))
                dist[r][0] = 1

        # bfs
        while queue:
            r, c = queue.popleft()

            # reached to the last column
            if c == M - 1:
                return dist[r][c]

            for dr, dc in DIRECTION_DELTA:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < N and 0 <= nc < M):
                    continue

                # unsafe or already visited
                if board[nr][nc] == 0 or dist[nr][nc] != -1:
                    continue

                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

        # no safe path exists
        return -1

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(N * M)


def p2():
    # Problem 2 : POTD Geeksforgeeks Shortest Safe Route in Grid - https://www.geeksforgeeks.org/problems/find-shortest-safe-route-in-a-matrix/1

    testcase = [
        [
            [
                [1, 0, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 0, 1],
                [1, 1, 1, 1, 0],
            ],
            6,
        ],
        [
            [
                [1, 1, 1, 1, 1],
                [1, 1, 0, 1, 1],
                [1, 1, 1, 1, 1],
            ],
            -1,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.shortestPath(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def trap(self, height: list[int]) -> int:

        # cant store on 0th or n-1th elevation
        # for each h in height
        # find largest h on left say lh,
        # find largest h on right say rh,
        # amount of water ith h can store max(0, min(lh, rh) - h)

        N = len(height)

        largest_left = list(range(N))
        largest_right = list(range(N))

        for i in range(1, N, 1):
            if height[largest_left[i - 1]] > height[i]:
                largest_left[i] = largest_left[i - 1]

        for i in range(N - 2, -1, -1):
            if height[largest_right[i + 1]] > height[i]:
                largest_right[i] = largest_right[i + 1]

        count = 0
        for i in range(1, N - 1, 1):
            upper_bound = min(height[largest_left[i]], height[largest_right[i]])
            count += max(0, upper_bound - height[i])

        return count

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 42. Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6],
        [[4, 2, 0, 3, 2, 5], 9],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.trap(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 14 of September 2026

    p1()

    p2()

    p3()
