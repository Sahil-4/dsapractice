from math import gcd


class Solution1:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        depth = 0

        for c in s:

            if c == "(":
                depth += 1

            if c == ")":
                depth -= 1

            max_depth = max(max_depth, depth)

        return max_depth

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1614. Maximum Nesting Depth of the Parentheses - https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/?envType=daily-question&envId=2026-09-28

    testcase = [
        ["(1+(2*3)+((8)/4))+1", 3],
        ["(1)+((2))+(((3)))", 3],
        ["()(())((()()))", 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maxDepth(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def processQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        N = len(arr)
        tree = [0] * (4 * N)

        def build(node: int, left: int, right: int) -> None:
            if left == right:
                tree[node] = arr[left]
                return

            mid = (left + right) // 2
            build(2 * node + 1, left, mid)
            build(2 * node + 2, mid + 1, right)

            tree[node] = gcd(tree[2 * node + 1], tree[2 * node + 2])

        def query(node: int, left: int, right: int, ql: int, qr: int) -> int:
            # no overlap
            if right < ql or left > qr:
                return 0

            # overlap
            if ql <= left and right <= qr:
                return tree[node]

            mid = (left + right) // 2

            return gcd(
                query(2 * node + 1, left, mid, ql, qr),
                query(2 * node + 2, mid + 1, right, ql, qr),
            )

        def update(node: int, left: int, right: int, index: int, value: int) -> None:
            if left == right:
                arr[index] = value
                tree[node] = value
                return

            mid = (left + right) // 2

            if index <= mid:
                update(2 * node + 1, left, mid, index, value)
            else:
                update(2 * node + 2, mid + 1, right, index, value)

            tree[node] = gcd(tree[2 * node + 1], tree[2 * node + 2])

        build(0, 0, N - 1)

        result = []

        for query_data in queries:
            query_type, x, y = query_data

            if query_type == 0:
                result.append(query(0, 0, N - 1, x, y))
            else:
                update(0, 0, N - 1, x, y)

        return result

        # Complexity analysis:
        # Time : O(N + Q * Log(N))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Range GCD Queries - https://www.geeksforgeeks.org/problems/range-gcd-queries3654/1

    testcase = [
        [
            [2, 3, 4, 6, 8, 16],
            [[0, 0, 2], [1, 3, 8], [0, 2, 5]],
            3,
            [1, 4],
        ],
        [
            [12, 18, 24, 30, 36],
            [[0, 1, 3], [1, 2, 15], [0, 0, 2], [0, 2, 4]],
            4,
            [6, 3, 3],
        ],
    ]

    for line in testcase:
        [*inputs, _, expected] = line
        s2 = Solution2()
        result = s2.processQueries(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def minDistance(self, word1: str, word2: str) -> int:
        T = 10**12

        N1 = len(word1)
        N2 = len(word2)

        dp = [[0 for _ in range(N2 + 1)] for _ in range(N1 + 1)]

        for i1 in range(N1, -1, -1):
            for i2 in range(N2, -1, -1):
                if i1 >= N1 and i2 >= N2:
                    # both strings exhausted
                    dp[i1][i2] = 0

                elif i1 >= N1:
                    # remove extra characters
                    dp[i1][i2] = N2 - i2

                elif i2 >= N2:
                    # remove extra characters
                    dp[i1][i2] = N1 - i1

                else:
                    min_operations = T

                    if word1[i1] == word2[i2]:
                        # matches - no need to perform any operation
                        min_operations = min(min_operations, dp[i1 + 1][i2 + 1])
                    else:
                        # replace
                        min_operations = min(min_operations, 1 + dp[i1 + 1][i2 + 1])

                    # insert
                    min_operations = min(min_operations, 1 + dp[i1][i2 + 1])

                    # delete
                    min_operations = min(min_operations, 1 + dp[i1 + 1][i2])

                    dp[i1][i2] = min_operations

        return dp[0][0]

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(N * N)


def p3():
    # Problem 3 : NC150 Leetcode 72. Edit Distance - https://leetcode.com/problems/edit-distance/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["horse", "ros", 3],
        ["intention", "execution", 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.minDistance(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 28 of September 2026

    p1()

    p2()

    p3()
