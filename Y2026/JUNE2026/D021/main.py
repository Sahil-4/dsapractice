from typing import List


class Solution1:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        counting = [0] * (max_cost + 1)

        for cost in costs:
            counting[cost] += 1

        bar_count = 0
        remaining_coins = coins
        for cost, count in enumerate(counting):
            if cost == 0 or count == 0:
                continue

            if remaining_coins < cost:
                break

            _count = min((remaining_coins // cost), count)
            bar_count += _count
            remaining_coins -= cost * _count

        return bar_count

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1833. Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/description/?envType=daily-question&envId=2026-06-21

    testcase = [
        [[1, 3, 2, 4, 1], 7, 4],
        [[10, 6, 8, 7, 7, 8], 5, 0],
        [[1, 6, 3, 1, 2, 5], 20, 6],
    ]

    for line in testcase:
        [costs, coins, expected] = line
        s1 = Solution1()
        result = s1.maxIceCream(costs, coins)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def chooseSwap(self, s: str) -> str:
        # code here

        s_list = list(s)

        # last occurrence of each character
        last = [-1] * 26
        for i, ch in enumerate(s_list):
            last[ord(ch) - ord("a")] = i

        seen = [False] * 26

        for i, ch in enumerate(s_list):
            curr = ord(ch) - ord("a")

            # try smaller characters
            for smaller in range(curr):
                if not seen[smaller] and last[smaller] > i:
                    x = ch
                    y = chr(smaller + ord("a"))

                    # global swap
                    for j in range(len(s_list)):
                        if s_list[j] == x:
                            s_list[j] = y
                        elif s_list[j] == y:
                            s_list[j] = x

                    return "".join(s_list)

            seen[curr] = True

        return "".join(s_list)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Choose and Swap - https://www.geeksforgeeks.org/problems/choose-and-swap0531/1

    testcase = [
        ["ccad", "aacd"],
        ["abba", "abba"],
    ]

    for line in testcase:
        [s, expected] = line
        s2 = Solution2()
        result = s2.chooseSwap(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 21 of June 2026

    p1()

    p2()
