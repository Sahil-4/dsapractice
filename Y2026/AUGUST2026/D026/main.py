from bisect import bisect_right


class Solution1:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        answer = ""

        prefix_sum = [0]
        for c in s:
            prefix_sum.append(prefix_sum[-1])
            if c == "1":
                prefix_sum[-1] += 1

        for i in range(1, len(prefix_sum)):
            # count of 1s in s[0:i]
            count_of_1 = prefix_sum[i]

            # number of extra 1s we need to remove
            reduce = count_of_1 - k

            if reduce < 0:
                continue

            # find the largest l such that prefix_sum[l] == reduce
            l = bisect_right(prefix_sum, reduce, hi=i) - 1

            if l >= 0 and prefix_sum[l] == reduce:
                t_answer = s[l:i]

                if (
                    answer == ""
                    or len(answer) > len(t_answer)
                    or (len(answer) == len(t_answer) and answer > t_answer)
                ):
                    answer = t_answer

        return answer

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2904. Shortest and Lexicographically Smallest Beautiful String - https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/description/?envType=daily-question&envId=2026-08-26

    testcase = [
        ["100011001", 3, "11001"],
        ["1011", 2, "11"],
        ["000", 1, ""],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.shortestBeautifulSubstring(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def isNegativeWeightCycle(self, V: int, edges: list[list[int]]) -> bool:
        # Bellman-Ford

        dist = [0] * V

        # if we can still relax an edge on the V-th iteration,
        # a negative weight cycle exists
        for i in range(V):
            updated = False

            for u, v, w in edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True

                    # relaxation on the V-th iteration
                    # means there is a negative weight cycle
                    if i == V - 1:
                        return True

            # no relaxation means no negative cycle
            if not updated:
                break

        return False

        # Complexity analysis
        # Time : O(V * E)
        # Space : O(V)


def p2():
    # Problem 2 : POTD Geeksforgeeks Negative Weight Cycle - https://www.geeksforgeeks.org/problems/negative-weight-cycle3504/1

    testcase = [
        [4, 4, [[0, 3, 6], [1, 0, 4], [1, 2, 6], [3, 1, 2]], False],
        [4, 4, [[1, 0, 4], [3, 1, -2], [1, 2, -6], [2, 3, 5]], True],
    ]

    for line in testcase:
        [E, *inputs, expected] = line
        s2 = Solution2()
        result = s2.isNegativeWeightCycle(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 26 of August 2026

    p1()

    p2()
