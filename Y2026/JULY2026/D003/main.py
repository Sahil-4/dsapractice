from collections import deque


class Solution1:
    def findMaxPathScore(
        self,
        edges: list[list[int]],
        online: list[bool],
        k: int,
    ) -> int:
        number_of_nodes = len(online)

        adjacency_list = [[] for _ in range(number_of_nodes)]
        indegree = [0] * number_of_nodes

        maximum_edge_cost = 0

        for from_node, to_node, edge_cost in edges:
            adjacency_list[from_node].append((to_node, edge_cost))
            indegree[to_node] += 1
            maximum_edge_cost = max(maximum_edge_cost, edge_cost)

        # topological order of the DAG
        topological_order = []

        queue = deque()

        for node in range(number_of_nodes):
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            current_node = queue.popleft()
            topological_order.append(current_node)

            for next_node, _ in adjacency_list[current_node]:
                indegree[next_node] -= 1

                if indegree[next_node] == 0:
                    queue.append(next_node)

        def can_achieve_score(required_score: int) -> bool:
            INF = float("inf")

            minimum_cost = [INF] * number_of_nodes
            minimum_cost[0] = 0

            for current_node in topological_order:
                if minimum_cost[current_node] == INF:
                    continue

                if (
                    current_node != 0
                    and current_node != number_of_nodes - 1
                    and not online[current_node]
                ):
                    continue

                for next_node, edge_cost in adjacency_list[current_node]:
                    if edge_cost < required_score:
                        continue

                    if next_node != number_of_nodes - 1 and not online[next_node]:
                        continue

                    new_cost = minimum_cost[current_node] + edge_cost

                    if new_cost < minimum_cost[next_node]:
                        minimum_cost[next_node] = new_cost

            return minimum_cost[number_of_nodes - 1] <= k

        left = 0
        right = maximum_edge_cost

        answer = -1

        while left <= right:
            middle = left + (right - left) // 2

            if can_achieve_score(middle):
                answer = middle
                left = middle + 1
            else:
                right = middle - 1

        return answer

        # Complexity analysis
        # Time : O((V + E) * log(C))
        # Space : O(V + E)


def p1():
    # Problem 1 : POTD Leetcode 3620. Network Recovery Pathways - https://leetcode.com/problems/network-recovery-pathways/description/?envType=daily-question&envId=2026-07-03

    testcase = [
        [
            [[0, 1, 5], [1, 3, 10], [0, 2, 3], [2, 3, 4]],
            [True, True, True, True],
            10,
            3,
        ],
        [
            [[0, 1, 7], [1, 4, 5], [0, 2, 6], [2, 3, 6], [3, 4, 2], [2, 4, 6]],
            [True, True, True, False, True],
            12,
            6,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.findMaxPathScore(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def waysToIncreaseLCSBy1(self, s1: str, s2: str) -> int:
        n1 = len(s1)
        n2 = len(s2)

        # positions of every character in s2 (1-based indexing)
        character_positions = [[] for _ in range(26)]

        for index in range(1, n2 + 1):
            character = s2[index - 1]
            character_positions[ord(character) - ord("a")].append(index)

        # prefix_lcs[i][j] =
        # LCS of s1[0:i] and s2[0:j]
        prefix_lcs = [[0] * (n2 + 2) for _ in range(n1 + 2)]

        for row in range(1, n1 + 1):
            for col in range(1, n2 + 1):
                if s1[row - 1] == s2[col - 1]:
                    prefix_lcs[row][col] = 1 + prefix_lcs[row - 1][col - 1]
                else:
                    prefix_lcs[row][col] = max(
                        prefix_lcs[row - 1][col],
                        prefix_lcs[row][col - 1],
                    )

        # suffix_lcs[i][j] =
        # LCS of s1[i:] and s2[j:]
        suffix_lcs = [[0] * (n2 + 2) for _ in range(n1 + 2)]

        for row in range(n1, 0, -1):
            for col in range(n2, 0, -1):
                if s1[row - 1] == s2[col - 1]:
                    suffix_lcs[row][col] = 1 + suffix_lcs[row + 1][col + 1]
                else:
                    suffix_lcs[row][col] = max(
                        suffix_lcs[row + 1][col],
                        suffix_lcs[row][col + 1],
                    )

        original_lcs = prefix_lcs[n1][n2]

        ways = 0

        # try every insertion position
        for insertion_index in range(n1 + 1):

            # try every lowercase character
            for character_index in range(26):

                # try every occurrence of this character in s2
                for match_position in character_positions[character_index]:

                    left_lcs = prefix_lcs[insertion_index][match_position - 1]
                    right_lcs = suffix_lcs[insertion_index + 1][match_position + 1]

                    if left_lcs + right_lcs == original_lcs:
                        ways += 1
                        break

        return ways

        # Complexity analysis
        # Time : O(N1 * N2)
        # Space : O(N1 * N2)


def p2():
    # Problem 2 : POTD Geeksforgeeks Ways to Increase LCS by One - https://www.geeksforgeeks.org/problems/count-ways-to-increase-lcs-length-of-two-strings-by-one2236/1

    testcase = [
        ["abab", "abc", 3],
        ["abcabc", "abcd", 4],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.waysToIncreaseLCSBy1(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 3 of July 2026

    p1()

    p2()
