import math
import heapq
from typing import List


class Solution1:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        N = len(bits)

        index = 0
        while index < N:
            if index == N - 1:
                return True

            if bits[index] == 1:
                index += 2
            else:
                index += 1

        return False

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 717. 1-bit and 2-bit Characters - https://leetcode.com/problems/1-bit-and-2-bit-characters/description/?envType=daily-question&envId=2025-11-18

    testcases = [
        [1, 0, 0],
        [1, 1, 1, 0],
    ]
    for testcase in testcases:
        s1 = Solution1()
        out = s1.isOneBitCharacter(testcase)
        print(out)


class Solution2:
    def countPaths(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))

        dist = [math.inf] * V
        ways = [0] * V

        dist[0] = 0
        ways[0] = 1

        pq = [(0, 0)]  # (distance, node)
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    ways[v] = ways[u]
                    heapq.heappush(pq, (nd, v))
                elif nd == dist[v]:
                    ways[v] += ways[u]

        return ways[V - 1]


def p2():
    # Problem 2 : POTD Geeksforgeeks Number of Ways to Arrive at Destination - https://www.geeksforgeeks.org/problems/number-of-ways-to-arrive-at-destination/1

    testcases = [
        [
            4,
            [
                [0, 1, 2],
                [1, 2, 3],
                [0, 3, 5],
                [1, 3, 3],
                [2, 3, 4],
            ],
        ],
        [
            6,
            [
                [0, 2, 3],
                [0, 4, 2],
                [0, 5, 7],
                [2, 3, 1],
                [2, 5, 5],
                [5, 3, 3],
                [5, 1, 4],
                [1, 4, 1],
                [4, 5, 5],
            ],
        ],
    ]

    for v, edges in testcases:
        s2 = Solution2()
        out = s2.countPaths(v, edges)
        print(out)


if __name__ == "__main__":
    # Day 18 of November 2025

    p1()

    p2()
