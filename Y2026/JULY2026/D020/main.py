class Solution1:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        N = len(grid)
        M = len(grid[0])

        T = N * M

        result = [[0] * M for _ in range(N)]

        for i in range(N):
            for j in range(M):
                _index = (i * M) + j
                _new_index = (_index + k) % T

                _new_j = _new_index % M
                _new_i = (_new_index - _new_j) // M

                result[_new_i][_new_j] = grid[i][j]

        return result

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1260. Shift 2D Grid - https://leetcode.com/problems/shift-2d-grid/description/?envType=daily-question&envId=2026-07-20

    testcase = [
        [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            1,
            [[9, 1, 2], [3, 4, 5], [6, 7, 8]],
        ],
        [
            [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]],
            4,
            [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]],
        ],
        [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            9,
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.shiftGrid(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findPrefixes(self, arr: list[str]) -> list[str]:
        # code here

        def lcp(a: str, b: str) -> int:
            i = 0
            limit = min(len(a), len(b))

            while i < limit and a[i] == b[i]:
                i += 1

            return i

        N = len(arr)

        # (word, original_index)
        words = [(word, idx) for idx, word in enumerate(arr)]
        words.sort()

        result = [""] * N

        for i in range(N):

            word, original_idx = words[i]

            prev_lcp = 0
            next_lcp = 0

            if i > 0:
                prev_lcp = lcp(word, words[i - 1][0])

            if i + 1 < N:
                next_lcp = lcp(word, words[i + 1][0])

            prefix_len = max(prev_lcp, next_lcp) + 1
            result[original_idx] = word[:prefix_len]

        return result

        # Complexity analysis
        # Time : O(N log N + total_characters)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Shortest Unique Prefix for Every Word - https://www.geeksforgeeks.org/problems/shortest-unique-prefix-for-every-word/1

    testcase = [
        [["zebra", "dog", "duck", "dove"], ["z", "dog", "du", "dov"]],
        [["geeksgeeks", "geeksquiz", "geeksforgeeks"], ["geeksg", "geeksq", "geeksf"]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.findPrefixes(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 20 of July 2026

    p1()

    p2()
