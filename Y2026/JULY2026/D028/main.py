from heapq import heappop, heappush


class Solution1:
    def smallestPalindrome(self, s: str) -> str:
        # frequency of each character
        frequency = {c: s.count(c) for c in set(s)}

        # build palindrome
        left = []
        middle = ""
        for c in sorted(frequency.keys()):
            count = frequency[c]
            left.extend([c] * (count // 2))
            if count % 2 == 1:
                middle = c

        right = left[::-1]

        return "".join(left) + middle + "".join(right)

        # Complexity Analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3517. Smallest Palindromic Rearrangement I - https://leetcode.com/problems/smallest-palindromic-rearrangement-i/description/?envType=daily-question&envId=2026-07-28

    testcase = [
        ["z", "z"],
        ["babab", "abbba"],
        ["daccad", "acddca"],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.smallestPalindrome(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def shortestPath(self, V: int, src: int, dest: int, edges: list[list[int]]) -> int:
        # code here
        adj = [[] for _ in range(V)]

        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        INF = float("inf")
        dist = [INF] * V
        dist[src] = 0

        pq = [(0, src)]

        while pq:
            curr_dist, node = heappop(pq)

            if curr_dist != dist[node]:
                continue

            if node == dest:
                return curr_dist

            for nei, wt in adj[node]:
                new_dist = curr_dist + wt
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heappush(pq, (new_dist, nei))

        return -1

        # Complexity Analysis
        # Time : O(V + E)
        # Space : O(V + E)


def p2():
    # Problem 2 : POTD Geeksforgeeks Shortest Path in 1-2 Graph - https://www.geeksforgeeks.org/problems/level-of-nodes1147/1

    testcase = [
        [
            4,
            0,
            3,
            [
                [0, 1, 1],
                [0, 2, 2],
                [2, 3, 1],
                [1, 2, 1],
                [1, 3, 2],
            ],
            3,
        ],
        [
            5,
            1,
            3,
            [
                [0, 1, 1],
                [0, 2, 2],
                [1, 2, 1],
                [3, 4, 2],
            ],
            -1,
        ],
        [
            5,
            1,
            4,
            [
                [1, 0, 1],
                [0, 3, 2],
                [1, 3, 1],
                [1, 2, 2],
                [2, 3, 2],
                [3, 4, 1],
                [2, 4, 1],
            ],
            2,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.shortestPath(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 28 of July 2026

    p1()

    p2()
