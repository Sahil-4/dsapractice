import heapq
from collections import deque
from typing import List, Dict, Tuple


class Solution1:
    def dijkstra(
        self, src: int, adj: List[List[Tuple[int, int]]], dist: List[List[int]]
    ) -> None:
        pq = []

        dist[src][src] = 0
        heapq.heappush(pq, (0, src))

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[src][u]:
                continue

            for v, w in adj[u]:
                if dist[src][v] > d + w:
                    dist[src][v] = d + w
                    heapq.heappush(pq, (dist[src][v], v))

    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:

        INF = 10**18

        # ---- Map strings to ids ----
        mp: Dict[str, int] = {}
        idx = 0
        for i in range(len(original)):
            if original[i] not in mp:
                mp[original[i]] = idx
                idx += 1
            if changed[i] not in mp:
                mp[changed[i]] = idx
                idx += 1

        # ---- Build graph ----
        adj = [[] for _ in range(idx)]
        for i in range(len(original)):
            u = mp[original[i]]
            v = mp[changed[i]]
            adj[u].append((v, cost[i]))

        # ---- All-pairs shortest paths ----
        dist = [[INF] * idx for _ in range(idx)]
        for i in range(idx):
            self.dijkstra(i, adj, dist)

        # ---- Precompute valid substring lengths ----
        lens = set(len(s) for s in original)

        n = len(source)
        dp = [INF] * (n + 1)
        dp[n] = 0

        # ---- DP ----
        for i in range(n - 1, -1, -1):

            # Case 1: no operation
            if source[i] == target[i]:
                dp[i] = dp[i + 1]

            # Case 2: substring conversions
            for length in lens:
                j = i + length - 1
                if j >= n:
                    continue

                from_str = source[i : i + length]
                to_str = target[i : i + length]

                if from_str not in mp or to_str not in mp:
                    continue

                c = dist[mp[from_str]][mp[to_str]]
                if c < INF:
                    dp[i] = min(dp[i], c + dp[j + 1])

        return -1 if dp[0] >= INF else dp[0]

        # Complexity analysis
        # Time : O(M * E log M + N * K)
        # Space: O(M^2 + E + N)


def p1():
    # Problem 1 : POTD Leetcode 2977. Minimum Cost to Convert String II - https://leetcode.com/problems/minimum-cost-to-convert-string-ii/description/?envType=daily-question&envId=2026-01-30

    testcase = [
        [
            "abcd",
            "acbe",
            ["a", "b", "c", "c", "e", "d"],
            ["b", "c", "b", "e", "b", "e"],
            [2, 5, 5, 1, 2, 20],
            28,
        ],
        [
            "abcdefgh",
            "acdeeghh",
            ["bcd", "fgh", "thh"],
            ["cde", "thh", "ghh"],
            [1, 3, 5],
            9,
        ],
        [
            "abcdefgh",
            "addddddd",
            ["bcd", "defgh"],
            ["ddd", "ddddd"],
            [100, 1578],
            -1,
        ],
    ]

    for line in testcase:
        [source, target, original, changed, cost, expected] = line
        s1 = Solution1()
        result = s1.minimumCost(source, target, original, changed, cost)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def rearrangeQueue(self, q: deque) -> None:
        # code here
        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        # [1, 6, 2, 7, 3, 8, 4, 9, 5, 0]
        # first_half[i], second_half[i], first_half[i+1], second_half[i+1], ...
        # split the queue into two halves
        # walk both halves together once
        # first half :  a1  a2  a3
        # second half:  b1  b2  b3
        # result:      a1 b1 a2 b2 a3 b3

        n = len(q)
        half = n // 2

        first = deque()
        for _ in range(half):
            first.append(q.popleft())

        while first:
            q.append(first.popleft())
            q.append(q.popleft())

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Interleave the First Half of the Queue with Second Half - https://www.geeksforgeeks.org/problems/interleave-the-first-half-of-the-queue-with-second-half/1

    testcase = [
        [
            deque([2, 4, 3, 1]),
            deque([2, 3, 4, 1]),
        ],
        [
            deque([3, 5]),
            deque([3, 5]),
        ],
        [
            deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]),
            deque([1, 6, 2, 7, 3, 8, 4, 9, 5, 0]),
        ],
    ]

    for line in testcase:
        [q, expected] = line
        s2 = Solution2()
        s2.rearrangeQueue(q)
        result = q
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 30 of January 2026

    p1()

    p2()
    
