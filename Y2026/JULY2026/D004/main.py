class Solution1:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        adjacency_list = [[] for _ in range(n + 1)]

        for city1, city2, distance in roads:
            adjacency_list[city1].append((city2, distance))
            adjacency_list[city2].append((city1, distance))

        visited = [False] * (n + 1)

        minimum_score = float("inf")

        def dfs(city: int) -> None:
            nonlocal minimum_score

            visited[city] = True

            for next_city, distance in adjacency_list[city]:
                minimum_score = min(minimum_score, distance)

                if not visited[next_city]:
                    dfs(next_city)

        dfs(1)

        return int(minimum_score)

        # Complexity analysis
        # Time : O(N + E)
        # Space : O(N + E)


def p1():
    # Problem 1 : POTD Leetcode 2492. Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/?envType=daily-question&envId=2026-07-04

    testcase = [
        [4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]], 5],
        [4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]], 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minScore(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countSubstring(self, s: str) -> int:
        n = len(s)

        substring_count = 0

        # offset used to keep prefix balance indices non-negative.
        offset = n

        # number of suffix prefix-balances that are <= current balance.
        less_or_equal_count = 0

        # frequency of each prefix balance.
        balance_frequency = [0] * (2 * n + 1)

        current_balance = offset

        # build prefix balances.
        for character in s:
            if character == "0":
                current_balance -= 1
            else:
                current_balance += 1

            if current_balance <= offset:
                less_or_equal_count += 1

            balance_frequency[current_balance] += 1

        current_balance = offset

        for index in range(n):
            substring_count += n - index - less_or_equal_count

            if s[index] == "1":
                balance_frequency[current_balance + 1] -= 1

                current_balance += 1

                less_or_equal_count += balance_frequency[current_balance]

            else:
                balance_frequency[current_balance - 1] -= 1

                current_balance -= 1

                less_or_equal_count -= 1
                less_or_equal_count -= balance_frequency[current_balance + 1]

        return substring_count

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Substrings with more 1's than 0's - https://www.geeksforgeeks.org/problems/count-the-substring--170645/1

    testcase = [
        ["011", 4],
        ["0000", 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.countSubstring(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 4 of July 2026

    p1()

    p2()
