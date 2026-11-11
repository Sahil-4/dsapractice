from collections import defaultdict


class Solution1:
    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        t_cost = 0

        cost_sum = cost1 + cost2

        t_cost += min(costBoth, cost_sum) * min(need1, need2)
        t_cost += min(costBoth, cost1) * (need1 - min(need1, need2))
        t_cost += min(costBoth, cost2) * (need2 - min(need1, need2))

        return t_cost

        # Complexity analysis
        # Time : O(1)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3789. Minimum Cost to Acquire Required Items - https://leetcode.com/problems/minimum-cost-to-acquire-required-items/?envType=daily-question&envId=2026-11-11

    testcase = [
        [3, 2, 1, 3, 2, 3],
        [5, 4, 15, 2, 3, 22],
        [5, 4, 15, 0, 0, 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minimumCost(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def checkWithinK(self, arr: list[int], k: int) -> bool:
        # code here
        N = len(arr)

        frequency = defaultdict(int)

        l = 0
        for r in range(N):
            if r - l > k:
                frequency[arr[l]] -= 1
                l += 1

            frequency[arr[r]] += 1
            if frequency[arr[r]] > 1:
                return True

        return False

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Any Duplicate Within K Distance - https://www.geeksforgeeks.org/problems/kth-distance3757/1

    testcase = [
        [[1, 5, 4, 5, 1], 3, True],
        [[10, 2, 3, 4, 10, 5], 3, False],
        [[5, 1, 3, 2, 4], 3, False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.checkWithinK(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class WordDictionary:

    def __init__(self):
        self.root: dict = {}

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]

        node["$"] = True

    def search(self, word: str) -> bool:
        def dfs(index: int, node: dict) -> bool:
            if index == len(word):
                return "$" in node

            ch = word[index]
            if ch == ".":
                for key, child in node.items():
                    if key != "$" and dfs(index + 1, child):
                        return True
                return False

            if ch not in node:
                return False
            return dfs(index + 1, node[ch])

        return dfs(0, self.root)

    # Complexity analysis
    # Time: O(L)
    # Space: O(C)


def p3():
    # Problem 3 : NC150 Leetcode 211. Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            [
                "WordDictionary",
                "addWord",
                "addWord",
                "addWord",
                "search",
                "search",
                "search",
                "search",
            ],
            [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
            [None, None, None, None, False, True, True, True],
        ]
    ]

    for line in testcase:
        [operations, arguments, expected] = line

        obj = None
        result = []
        for operation, argument in zip(operations, arguments):
            if operation == "WordDictionary":
                obj = WordDictionary(*argument)
                result.append(None)
            else:
                result.append(getattr(obj, operation)(*argument))

        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 11 of November 2026

    p1()

    p2()

    p3()
