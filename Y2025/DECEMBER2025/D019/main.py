import heapq
from collections import defaultdict


class Solution1:
    def findAllPeople(self, n, meetings, firstPerson):
        adj = defaultdict(list)

        for p1, p2, time in meetings:
            adj[p1].append((p2, time))
            adj[p2].append((p1, time))

        # min-heap: (time, person)
        pq = []
        heapq.heappush(pq, (0, 0))
        heapq.heappush(pq, (0, firstPerson))

        visited = [False] * n

        while pq:
            time, person = heapq.heappop(pq)

            if visited[person]:
                continue

            visited[person] = True

            for next_person, t in adj[person]:
                if t >= time and not visited[next_person]:
                    heapq.heappush(pq, (t, next_person))

        return [i for i in range(n) if visited[i]]


def p1():
    # Problem 1 : POTD Leetcode 2092. Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/description/?envType=daily-question&envId=2025-12-19

    testcase = [
        [6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1, [0, 1, 2, 3, 5]],
        [4, [[3, 1, 3], [1, 2, 2], [0, 3, 3]], 3, [0, 1, 3]],
    ]

    for line in testcase:
        [n, meetings, firstPerson, expected] = line
        s1 = Solution1()
        result = s1.findAllPeople(n, meetings, firstPerson)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findMoves(self, chairs, passengers):
        chairs.sort()
        passengers.sort()

        moves = 0
        for c, p in zip(chairs, passengers):
            moves += abs(c - p)

        return moves

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Bus Conductor - https://www.geeksforgeeks.org/problems/bus-conductor--170647/1

    testcase = [
        [[3, 1, 5], [2, 7, 4], 4],
        [[2, 2, 6, 6], [1, 3, 2, 6], 4],
    ]

    for line in testcase:
        [chairs, passengers, expected] = line
        s2 = Solution2()
        result = s2.findMoves(chairs, passengers)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 19 of December 2025

    p1()

    p2()
