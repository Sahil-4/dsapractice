from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.setCount = n
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        # Union by size

        if self.size[x] < self.size[y]:
            x, y = y, x

        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1

    def find_and_union(self, x: int, y: int) -> bool:
        parentX, parentY = self.find(x), self.find(y)

        if parentX != parentY:
            self.union(parentX, parentY)
            return True

        return False


class Solution1:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        M, N = len(grid), len(grid[0])

        dsu = UnionFind(M * N)

        for i in range(M):
            for j in range(N):
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    if not dsu.find_and_union(i * N + j, (i - 1) * N + j):
                        return True

                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    if not dsu.find_and_union(i * N + j, i * N + j - 1):
                        return True

        return False

        # Complexity analysis
        # Time : O(M*N*4A)
        # Space : O(M*N)


def p1():
    # Problem 1 : POTD Leetcode 1559. Detect Cycles in 2D Grid - https://leetcode.com/problems/detect-cycles-in-2d-grid/description/?envType=daily-question&envId=2026-04-26

    testcase = [
        [
            [
                ["a", "a", "a", "a"],
                ["a", "b", "b", "a"],
                ["a", "b", "b", "a"],
                ["a", "a", "a", "a"],
            ],
            True,
        ],
        [
            [
                ["c", "c", "c", "a"],
                ["c", "d", "c", "c"],
                ["c", "c", "e", "c"],
                ["f", "c", "c", "c"],
            ],
            True,
        ],
        [[["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]], False],
    ]

    for line in testcase:
        [grid, expected] = line
        s1 = Solution1()
        result = s1.containsCycle(grid)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def commonElements(self, a: List[int], b: List[int], c: List[int]) -> List[int]:
        # code here

        ai = bi = ci = 0
        N, M, P = len(a), len(b), len(c)

        result = []

        while ai < N and bi < M and ci < P:
            # skip duplicates
            if ai > 0 and a[ai] == a[ai - 1]:
                ai += 1
                continue
            if bi > 0 and b[bi] == b[bi - 1]:
                bi += 1
                continue
            if ci > 0 and c[ci] == c[ci - 1]:
                ci += 1
                continue

            # common
            if a[ai] == b[bi] == c[ci]:
                result.append(a[ai])
                ai += 1
                bi += 1
                ci += 1

            else:
                # increment min pointer
                mn = min(a[ai], b[bi], c[ci])
                if a[ai] == mn:
                    ai += 1
                elif b[bi] == mn:
                    bi += 1
                else:
                    ci += 1

        return result

        # Complexity analysis
        # Time : O(N + M + P)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Common in 3 Sorted Arrays - https://www.geeksforgeeks.org/problems/common-elements1132/1

    testcase = [
        [
            [1, 5, 10, 20, 40, 80],
            [6, 7, 20, 80, 100],
            [3, 4, 15, 20, 30, 70, 80, 120],
            [20, 80],
        ],
        [[1, 2, 3, 4, 5], [6, 7], [8, 9, 10], []],
        [[1, 1, 1, 2, 2, 2], [1, 1, 2, 2, 2], [1, 1, 1, 1, 2, 2, 2, 2], [1, 2]],
    ]

    for line in testcase:
        [a, b, c, expected] = line
        s2 = Solution2()
        result = s2.commonElements(a, b, c)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 26 of April 2026

    p1()

    p2()
