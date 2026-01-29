from typing import List
import heapq


class Solution1:
    def dijkstra(self, source, adj, dist):
        dist[source][source] = 0
        pq = [(0, source)]  # (distance, node)

        while pq:
            curr_dist, node = heapq.heappop(pq)

            # Optional optimization
            if curr_dist > dist[source][node]:
                continue

            for wt, ne in adj[node]:
                if dist[source][ne] > dist[source][node] + wt:
                    dist[source][ne] = dist[source][node] + wt
                    heapq.heappush(pq, (dist[source][ne], ne))

    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        # use dijkstra
        # find min cost to reach from every character i to every other character
        # use this cost array to efficiently change source character to target character
        # if cost is infinity we cant change source character to target character
        # hence return -1
        # at the end return total cost of changing source to target

        # adjacency list for 26 characters
        adj = [[] for _ in range(26)]

        for i in range(len(original)):
            u = ord(original[i]) - ord("a")
            v = ord(changed[i]) - ord("a")
            adj[u].append((cost[i], v))

        INF = 10**9
        dist = [[INF] * 26 for _ in range(26)]

        # run dijkstra from every character
        for i in range(26):
            self.dijkstra(i, adj, dist)

        ans = 0
        for i in range(len(source)):
            u = ord(source[i]) - ord("a")
            v = ord(target[i]) - ord("a")

            if dist[u][v] != INF:
                ans += dist[u][v]
            else:
                return -1

        return ans

        # Complexity analysis
        # Time : O(26 * (E * Log(V)) + N)
        # Space : O((V * V) + E)


def p1():
    # Problem 1 : POTD Leetcode 2976. Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=daily-question&envId=2026-01-29

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
            "aaaa",
            "bbbb",
            ["a", "c"],
            ["c", "b"],
            [1, 2],
            12,
        ],
    ]

    for line in testcase:
        [source, target, original, changed, cost, expected] = line
        s1 = Solution1()
        result = s1.minimumCost(source, target, original, changed, cost)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def firstNonRepeating(self, s):
        # code here
        # use map to store information of characters and their frequency
        # use queue to store candidate characters
        # traverse left to right
        # update character frequency
        # push character into queue
        # while frequency of front character in queue is grater then 1 pop front
        # if queue is empty use #
        # or use front character as non repeating character prefix
        # instead of using a queue we can also use a pointer in given string s
        # and use this pointer to mimic queue behaviour

        slen = len(s)

        nrpc = []
        frequency = dict()
        qi = 0

        for i in range(slen):
            if s[i] not in frequency:
                frequency[s[i]] = 0

            frequency[s[i]] += 1

            while qi <= i and frequency[s[qi]] > 1:
                qi += 1

            if qi <= i:
                nrpc.append(s[qi])
            else:
                nrpc.append("#")

        return "".join(nrpc)

        # Complexity analysis
        # Time : O(3N)
        # Space : O(2N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Stream First Non-repeating - https://www.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream1216/1

    testcase = [
        ["aabc", "a#bb"],
        ["bb", "b#"],
    ]

    for line in testcase:
        [s, expected] = line
        s2 = Solution2()
        result = s2.firstNonRepeating(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 29 of January 2026

    p1()

    p2()
