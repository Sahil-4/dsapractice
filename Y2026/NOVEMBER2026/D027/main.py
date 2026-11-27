class Solution1:
    def maxItems(self, items: list[list[int]], budget: int) -> int:
        N = len(items)

        # first purchase of a type i : costs price_i and gives value_i copies in total,
        # itself (bought) plus one free copy of every other type whose factor is divisible by factor_i.
        # Further copies of a type give nothing extra, they just add one copy for their price
        value = [0] * N
        for i in range(N):
            for j in range(N):
                if items[j][0] % items[i][0] == 0:
                    value[i] += 1

        # 0/1 knapsack over the first purchases, dp[s] : best value with a total cost of at most s
        dp = [0] * (budget + 1)
        for i in range(N):
            price = items[i][1]

            for s in range(budget, price - 1, -1):
                dp[s] = max(dp[s], dp[s - price] + value[i])

        # whatever is left after the first purchases buys more copies of the cheapest type
        cheapest = min(price for _, price in items)

        return max(dp[s] + (budget - s) // cheapest for s in range(budget + 1))

        # Complexity analysis
        # Time : O(N^2 + N * budget)
        # Space : O(N + budget)


def p1():
    # Problem 1 : POTD Leetcode 3946. Maximum Number of Items From Sale I - https://leetcode.com/problems/maximum-number-of-items-from-sale-i/description/?envType=daily-question&envId=2026-11-27

    testcase = [
        [[[6, 2], [2, 6], [3, 4]], 9, 4],
        [[[2, 4], [3, 2], [4, 1], [6, 4], [12, 4]], 8, 10],
        [[[2, 3], [4, 2], [6, 5]], 6, 4],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maxItems(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countEdges(self, adj: list[list[int]]) -> int:
        # every undirected edge is listed twice, once in each endpoint's neighbor list
        return sum(len(neighbors) for neighbors in adj) // 2

        # Complexity analysis
        # Time : O(V)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count Edges in Graph - https://www.geeksforgeeks.org/problems/count-number-of-edges-in-an-undirected-graph/1

    testcase = [
        [[[1, 2], [0, 2], [0, 1]], 3],
        [[[1], [0, 2], [1]], 2],
        [[[], []], 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.countEdges(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def partitionLabels(self, s: str) -> list[int]:
        # last position of every character
        last = {ch: i for i, ch in enumerate(s)}

        sizes = []
        start = 0
        end = 0

        # a part can only be closed once every character seen so far has also ended
        for i, ch in enumerate(s):
            end = max(end, last[ch])

            if i == end:
                sizes.append(end - start + 1)
                start = i + 1

        return sizes

        # Complexity analysis
        # Time : O(N)
        # Space : O(1), at most 26 characters


def p3():
    # Problem 3 : NC150 Leetcode 763. Partition Labels - https://leetcode.com/problems/partition-labels/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["ababcbacadefegdehijhklij", [9, 7, 8]],
        ["eccbbbbdec", [10]],
        ["abc", [1, 1, 1]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.partitionLabels(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 27 of November 2026

    p1()

    p2()

    p3()
