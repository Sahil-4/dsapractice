import heapq


class Solution1:
    def checkStrings(self, s1: str, s2: str) -> bool:
        N = len(s1)

        odd_map = [0 for _ in range(26)]
        even_map = [0 for _ in range(26)]

        for i in range(N):
            if i & 1:
                odd_map[ord(s1[i]) - ord("a")] += 1
                odd_map[ord(s2[i]) - ord("a")] -= 1
            else:
                even_map[ord(s1[i]) - ord("a")] += 1
                even_map[ord(s2[i]) - ord("a")] -= 1

        for i in range(26):
            if odd_map[i] != 0 or even_map[i] != 0:
                return False

        return True

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2840. Check if Strings Can be Made Equal With Operations II - https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/description/?envType=daily-question&envId=2026-03-30

    testcase = [
        ["abcdba", "cabdab", True],
        ["abe", "bea", False],
    ]

    for line in testcase:
        [str1, str2, expected] = line
        s1 = Solution1()
        result = s1.checkStrings(str1, str2)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:

    def manhattanDistance(self, h1, h2):
        return abs(h1[0] - h2[0]) + abs(h1[1] - h2[1])

    def minCost(self, houses):
        V = len(houses)

        # total cost of MST
        total_cost = 0

        # visited nodes
        visited = set()

        # min heap -> (cost, node)
        min_heap = [(0, 0)]  # start from node 0

        while min_heap:
            cost, u = heapq.heappop(min_heap)

            # skip if already visited
            if u in visited:
                continue

            # include in MST
            visited.add(u)
            total_cost += cost

            # stop early if all nodes visited
            if len(visited) == V:
                break

            # explore neighbors
            for v in range(V):
                if v not in visited:
                    dist = self.manhattanDistance(houses[u], houses[v])
                    heapq.heappush(min_heap, (dist, v))

        return total_cost

        # Complexity analysis
        # Time : O(E log E)
        # Space : O(N * N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum cost to connect all houses in a city - https://www.geeksforgeeks.org/problems/minimum-cost-to-connect-all-houses-in-a-city/1

    testcase = [
        [5, [[0, 7], [0, 9], [20, 7], [30, 7], [40, 70]], 105],
        [4, [[0, 0], [1, 1], [1, 3], [3, 0]], 7],
    ]

    for line in testcase:
        [_, houses, expected] = line
        s2 = Solution2()
        result = s2.minCost(houses)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 30 of March 2026

    p1()

    p2()
