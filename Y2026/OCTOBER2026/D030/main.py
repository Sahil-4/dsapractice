import heapq


class Solution1:
    def shortestPath(self, N: int, edges: list[list[int]], labels: str, k: int) -> int:
        if k < 1:
            return -1

        adj = [[] for _ in range(N)]
        for u, v, w in edges:
            adj[u].append((v, w))

        # dist[(node, consecutive_count)] = min distance to reach node
        # Since graph edges are directed and we track consecutive identical characters,
        # consecutive count at node 0 is 1.
        dist = {}
        dist[(0, 1)] = 0

        # pq stores: (current_distance, node, consecutive_count)
        pq = [(0, 0, 1)]

        while pq:
            d, u, count = heapq.heappop(pq)

            if d > dist.get((u, count), float("inf")):
                continue

            if u == N - 1:
                return d

            for v, w in adj[u]:
                next_count = count + 1 if labels[v] == labels[u] else 1
                if next_count <= k:
                    if d + w < dist.get((v, next_count), float("inf")):
                        dist[(v, next_count)] = d + w
                        heapq.heappush(pq, (d + w, v, next_count))

        return -1

        # Complexity Analysis
        # Time : O(V + E * Log(V * K))
        # Space : O(V * K)


def p1():
    # Problem 1 : POTD Leetcode 3970. Shortest Path With At Most K Consecutive Identical Characters - https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/description/?envType=daily-question&envId=2026-10-30

    testcase = [
        [3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 1, 3],
        [3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 2, 2],
        [3, [[0, 1, 1], [1, 2, 1]], "aaa", 2, -1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.shortestPath(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


from collections import Counter


class Solution2:
    def cntSubsets(self, arr: list[int], l: int, r: int) -> int:
        """code here"""

        MOD = 10**9 + 7
        N = len(arr)

        pow2 = [1] * (N + 1)
        for i in range(1, N + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        ans = 0

        ways_prefix = 1
        used_counts = 0

        freq = Counter(arr)

        for m in range(r + 1):
            c_m = freq.get(m, 0)

            if m >= l:
                remaining_elements = N - used_counts - c_m
                ways_remaining = pow2[remaining_elements]
                ways_mex = (ways_prefix * ways_remaining) % MOD
                ans = (ans + ways_mex) % MOD

            if c_m == 0:
                break

            ways_prefix = (ways_prefix * (pow2[c_m] - 1)) % MOD
            used_counts += c_m

        return ans

        # Complexity Analysis
        # Time : O(N + R)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Subsets with MEX in Range - https://www.geeksforgeeks.org/problems/crazy-subsets--131708/1

    testcase = [
        [[2, 0, 1, 0], 1, 2, 9],
        [[2, 0, 1], 1, 2, 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.cntSubsets(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def checkValidString(self, s: str) -> bool:
        c_min = 0  # min possible open brackets
        c_max = 0  # max possible open brackets

        for ch in s:
            if ch == "(":
                c_min += 1
                c_max += 1
            elif ch == ")":
                c_min = max(0, c_min - 1)
                c_max -= 1
            elif ch == "*":
                c_min = max(0, c_min - 1)  # Treated as ')'
                c_max += 1  # Treated as '('

            if c_max < 0:
                return False

        return c_min == 0

        # Complexity analysis
        # Time : O(N)
        # Time : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 678. Valid Parenthesis String - https://leetcode.com/problems/valid-parenthesis-string/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["()", True],
        ["(*)", True],
        ["(*))", True],
        ["(", False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.checkValidString(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 30 of October 2026

    p1()

    p2()

    p3()
