class ProductOfNumbers:
    def __init__(self):
        # prefix[i] : product of the numbers added since the last zero, prefix[0] = 1
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # any product that reaches back past a zero is zero, so start over
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # fewer than k numbers since the last zero : the last k numbers contain that zero
        if k >= len(self.prefix):
            return 0

        return self.prefix[-1] // self.prefix[-1 - k]

    # Complexity analysis
    # Time : O(1) per operation
    # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1352. Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/?envType=daily-question&envId=2026-11-23

    testcase = [
        [
            [
                "ProductOfNumbers",
                "add",
                "add",
                "add",
                "add",
                "add",
                "getProduct",
                "getProduct",
                "getProduct",
                "add",
                "getProduct",
            ],
            [[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]],
            [None, None, None, None, None, None, 20, 40, 0, None, 32],
        ]
    ]

    for line in testcase:
        [operations, arguments, expected] = line

        # design problem : run every operation in order on one object
        obj = None
        result = []
        for operation, argument in zip(operations, arguments):
            if operation == "ProductOfNumbers":
                obj = ProductOfNumbers(*argument)
                result.append(None)
            else:
                result.append(getattr(obj, operation)(*argument))

        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def posInfinite(self, s: str, pos: int) -> str:
        # s_0 = s, s_i = s_(i-1) + "$" * i + reverse(s_(i-1)), pos is 1-indexed
        lengths = [len(s)]
        while lengths[-1] < pos:
            lengths.append(2 * lengths[-1] + len(lengths))

        index = pos - 1

        # walk down from the smallest level that contains the position
        for i in range(len(lengths) - 1, 0, -1):
            previous = lengths[i - 1]

            if index < previous:
                continue

            if index < previous + i:
                return "$"

            # reversed copy : mirror the index back into s_(i-1)
            index = previous - 1 - (index - previous - i)

        return s[index]

        # Complexity analysis
        # Time : O(Log(pos))
        # Space : O(Log(pos))


def p2():
    # Problem 2 : POTD Geeksforgeeks Character at Position in Infinite String - https://www.geeksforgeeks.org/problems/the-infinite-string1049/1

    # s = "ab" : "ab" -> "ab$ba" -> "ab$ba$$ab$ba" -> ...
    testcase = [
        ["ab", 1, "a"],
        ["ab", 3, "$"],
        ["ab", 4, "b"],
        ["ab", 6, "$"],
        ["ab", 8, "a"],
        ["ab", 12, "a"],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.posInfinite(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        N = len(cost)

        # first, second : minimum cost to stand on step i - 2 and i - 1 (paying their cost)
        first, second = cost[0], cost[1]

        for i in range(2, N):
            first, second = second, cost[i] + min(first, second)

        # the top is reached from either of the last two steps
        return min(first, second)

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 746. Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[10, 15, 20], 15],
        [[1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6],
        [[5, 5], 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.minCostClimbingStairs(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 23 of November 2026

    p1()

    p2()

    p3()
