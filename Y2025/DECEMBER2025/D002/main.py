from typing import List
from collections import defaultdict


class Solution1:
    MOD = 10**9 + 7

    def countTrapezoids(self, points: List[List[int]]) -> int:
        ans = 0

        cmap = dict()
        for point in points:
            cmap[point[1]] = cmap.get(point[1], 0) + 1

        edges_sum = 0

        for point, count in cmap.items():
            edges = (count * (count - 1)) // 2
            ans = (ans + (edges * edges_sum)) % self.MOD
            edges_sum += edges

        return int(ans)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3623. Count Number of Trapezoids I - https://leetcode.com/problems/count-number-of-trapezoids-i/description/?envType=daily-question&envId=2025-12-02

    testcase = [
        [[[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]], 3],
        [[[0, 0], [1, 0], [0, 1], [2, 1]], 1],
    ]

    for line in testcase:
        [points, expected] = line
        s1 = Solution1()
        result = s1.countTrapezoids(points)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxScore(self, s, jumps):
        # code here
        n = len(s)

        # prefix sum of ASCII values
        prefixScore = [0] * (n + 1)
        for i in range(1, n + 1):
            prefixScore[i] = prefixScore[i - 1] + ord(s[i - 1])

        # next index of character c
        nextInd = [[-1] * 26 for _ in range(n)]
        lastInd = [-1] * 26
        for i in range(n - 1, -1, -1):
            for c in range(26):
                nextInd[i][c] = lastInd[c]
            lastInd[ord(s[i]) - ord("a")] = i

        # adjacency map

        # as per jump rules
        adj = defaultdict(list)
        for u, v in jumps:
            if isinstance(u, int):
                u = chr(u)
            if isinstance(v, int):
                v = chr(v)

            adj[u].append(v)

        # every character can always jump to itself
        for c in range(26):
            ch = chr(ord("a") + c)
            adj[ch].append(ch)

        # dp
        dp = [-1] * n

        def helper(ind):
            if ind == n - 1:
                return 0
            if dp[ind] != -1:
                return dp[ind]

            best = 0
            cur_char = s[ind]

            for ch in adj[cur_char]:
                nxt = nextInd[ind][ord(ch) - ord("a")]
                if nxt == -1:
                    continue

                # Same logic as Java
                if ch == cur_char:
                    temp = prefixScore[nxt] - prefixScore[ind + 1] + helper(nxt)
                else:
                    temp = prefixScore[nxt] - prefixScore[ind] + helper(nxt)

                best = max(best, temp)

            dp[ind] = best
            return best

        return helper(0)

        # Complexity analysis
        # Time : O(N * 26)
        # Space : O(N * 26)


def p2():
    # Problem 2 : POTD Geeksforgeeks Maximise String Score - https://www.geeksforgeeks.org/problems/maximise-string-score--172902/1

    testcase = [
        ["forgfg", [["f", "r"], ["r", "g"]], 429],
        ["abcda", [["b", "d"]], 297],
    ]

    for line in testcase:
        [s, jumps, expected] = line
        s2 = Solution2()
        result = s2.maxScore(s, jumps)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 2 of December 2025

    p1()

    p2()
