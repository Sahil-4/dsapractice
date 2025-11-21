import heapq
from collections import defaultdict


class Solution1:
    def countUnique(self, s, low, high):
        st = set()

        for i in range(low + 1, high, 1):
            st.add(s[i])

        return len(st)

    def countPalindromicSubsequence(self, s: str) -> int:
        # approach :
        # init count = 0
        # create a map of character to [fi, li]
        # where fi = index where character occurred first time
        # and li = index where character occurred last time
        # now for each character take fi, and li
        # and if fi != li
        # count unique characters in [fi, li] exclusive
        # increment count by number of unique characters

        count = 0

        char_fi_li_map = {}
        for i in range(len(s)):
            if s[i] not in char_fi_li_map:
                char_fi_li_map[s[i]] = [i, i]
            else:
                char_fi_li_map[s[i]][1] = i

        for ch in range(ord("a"), ord("z") + 1):
            if (chr(ch) in char_fi_li_map) and (
                char_fi_li_map[chr(ch)][0] != char_fi_li_map[chr(ch)][1]
            ):
                count += self.countUnique(
                    s, char_fi_li_map[chr(ch)][0], char_fi_li_map[chr(ch)][1]
                )

        return count

        # Complexity analysis
        # Time : O(26 * N)
        # Space : O(26)


def p1():
    # Problem 1 : POTD Leetcode 1930. Unique Length-3 Palindromic Subsequences - https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/?envType=daily-question&envId=2025-11-21

    testcase = [
        ["aabca", 3],
        ["adc", 0],
        ["bbcbaba", 4],
    ]

    for line in testcase:
        [s, expected] = line
        s1 = Solution1()
        result = s1.countPalindromicSubsequence(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def shortestPath(self, V, a, b, edges):
        # code here
        # approach :
        # take a distance array of size V init with inf
        # take a pririty queue (min heap - top most element will have smallest cost)
        # priority queue will manage { cost, vertex, used_curved }
        # at each step we move forward to neighbour vertex
        # if distance[v] < cost + adj[vertex][v]
        # then traverse this path and update distance array
        # if we reach to b
        # we return cost
        # else at the end we return -1

        graph = defaultdict(list)

        # Build adjacency list
        for x, y, w1, w2 in edges:
            graph[x].append((y, w1, w2))
            graph[y].append((x, w1, w2))

        INF = 10**18
        dist_st = [INF] * V  # No curved edge used
        dist_cv = [INF] * V  # One curved edge used

        pq = []
        dist_st[a] = 0
        heapq.heappush(pq, (0, a, 0))  # cost, node, used_curved

        while pq:
            cost, u, used = heapq.heappop(pq)

            # If this is an outdated entry, skip
            if used == 0 and cost > dist_st[u]:
                continue
            if used == 1 and cost > dist_cv[u]:
                continue

            for v, w1, w2 in graph[u]:

                # 1) Take straight edge (allowed always)
                new_cost = cost + w1
                if used == 0 and new_cost < dist_st[v]:
                    dist_st[v] = new_cost
                    heapq.heappush(pq, (new_cost, v, 0))

                if used == 1 and new_cost < dist_cv[v]:
                    dist_cv[v] = new_cost
                    heapq.heappush(pq, (new_cost, v, 1))

                # 2) Take curved edge (only if not used yet)
                if used == 0:
                    new_cost = cost + w2
                    if new_cost < dist_cv[v]:
                        dist_cv[v] = new_cost
                        heapq.heappush(pq, (new_cost, v, 1))

        ans = min(dist_st[b], dist_cv[b])
        return ans if ans < INF else -1

        # Complexity analysis
        # Time : O((E + V) log V)
        # Space : O(V + E)


def p2():
    # Problem 2 : POTD Geeksforgeeks Shortest Path Using Atmost One Curved Edge - https://www.geeksforgeeks.org/problems/shortest-path-using-atmost-one-curved-edge--170647/1

    testcase = [
        [2, 1, 0, 1, [[0, 1, 4, 1]], 1],
        [4, 4, 1, 3, [[0, 1, 1, 4], [0, 2, 2, 4], [0, 3, 3, 1], [1, 3, 6, 5]], 2],
    ]

    for line in testcase:
        [V, E, a, b, edges, expected] = line
        s2 = Solution2()
        result = s2.shortestPath(V, a, b, edges)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 21 of November 2025

    p1()

    p2()
