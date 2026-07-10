class Solution1:
    def pathExistenceQueries(
        self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]
    ) -> list[int]:

        # (value, original index)
        order = sorted((nums[i], i) for i in range(n))

        # original index -> position in sorted order
        position = [0] * n
        for i, (_, node) in enumerate(order):
            position[node] = i

        LOG = n.bit_length()

        # jump[i][0] = farthest sorted index reachable in one edge
        jump = [[0] * LOG for _ in range(n)]

        r = 0
        for l in range(n):

            if r < l:
                r = l

            while (
                r + 1 < n
                and order[r + 1][0] - order[r][0] <= maxDiff
                and order[r + 1][0] - order[l][0] <= maxDiff
            ):
                r += 1

            jump[l][0] = r

        # Binary lifting
        for j in range(1, LOG):
            for i in range(n):
                jump[i][j] = jump[jump[i][j - 1]][j - 1]

        answer = []

        for u, v in queries:

            a = position[u]
            b = position[v]

            if a > b:
                a, b = b, a

            if a == b:
                answer.append(0)
                continue

            curr = a
            dist = 0

            for j in range(LOG - 1, -1, -1):
                if jump[curr][j] < b:
                    curr = jump[curr][j]
                    dist += 1 << j

            if jump[curr][0] >= b:
                answer.append(dist + 1)
            else:
                answer.append(-1)

        return answer

        # Complexity analysis
        # Time : O((N + Q) log N)
        # Space : O(N log N)


def p1():
    # Problem 1 : POTD Leetcode 3534. Path Existence Queries in a Graph II - https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/description/?envType=daily-question&envId=2026-07-10

    testcase = [
        [
            5,
            [1, 8, 3, 4, 2],
            3,
            [[0, 3], [2, 4]],
            [1, 1],
        ],
        [
            5,
            [5, 3, 1, 9, 10],
            2,
            [[0, 1], [0, 2], [2, 3], [4, 3]],
            [1, 2, -1, 1],
        ],
        [
            3,
            [3, 6, 1],
            1,
            [[0, 0], [0, 1], [1, 2]],
            [0, -1, -1],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.pathExistenceQueries(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def getCount(self, n: int) -> int:
        # Common difference = 1
        # Sum of consecutive numbers:
        # n = len * (2 * start + len - 1) / 2
        # Rearranging:
        # start = (n - len * (len - 1) / 2) / len
        # For every possible sequence length, check whether
        # start is a positive integer.

        count = 0
        length = 2

        while length * (length - 1) // 2 < n:

            numerator = n - (length * (length - 1) // 2)

            if numerator % length == 0:
                start = numerator // length

                if start >= 1:
                    count += 1

            length += 1

        return count

        # Complexity analysis
        # Time : O(sqrt(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Ways to Express as Sum of Consecutives - https://www.geeksforgeeks.org/problems/count-of-sum-of-consecutives3741/1

    testcase = [
        [10, 1],
        [15, 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.getCount(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 10 of July 2026

    p1()

    p2()
