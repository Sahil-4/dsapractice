from collections import deque


class Solution1:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        # dp[j] : minimum total cost to reach step j, step 0 costs nothing
        dp = [0] * (n + 1)

        for j in range(1, n + 1):
            best = float("inf")

            # step j can only be reached from j - 1, j - 2 or j - 3
            for i in range(max(0, j - 3), j):
                best = min(best, dp[i] + costs[j - 1] + (j - i) ** 2)

            dp[j] = int(best)

        return dp[n]

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3693. Climbing Stairs II - https://leetcode.com/problems/climbing-stairs-ii/description/?envType=daily-question&envId=2026-11-10

    testcase = [
        [4, [1, 2, 3, 4], 13],
        [4, [5, 1, 6, 2], 11],
        [3, [9, 8, 3], 12],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.climbStairs(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def firstElementKTime(self, arr: list[int], k: int) -> int:
        frequency = {}

        # the element whose k-th occurrence appears earliest is the first one
        # to reach a running count of k while scanning left to right
        for value in arr:
            frequency[value] = frequency.get(value, 0) + 1

            if frequency[value] == k:
                return value

        return -1

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks At Least K Occurrences - https://www.geeksforgeeks.org/problems/first-element-to-occur-k-times5150/1

    testcase = [
        [[1, 7, 4, 3, 4, 8, 7], 2, 4],
        [[4, 1, 6, 1, 4, 4, 1], 3, 4],
        [[1, 2, 3, 4], 2, -1],
        [[5], 1, 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.firstElementKTime(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # edge prerequisite -> course, Kahn's algorithm on the resulting graph
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # fewer than numCourses taken means a cycle, so no valid order exists
        return order if len(order) == numCourses else []

        # Complexity analysis
        # Time : O(V + E)
        # Space : O(V + E)


def p3():
    # Problem 3 : NC150 Leetcode 210. Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/?envType=problem-list-v2&envId=plakya4j

    # any valid topological order is accepted by Leetcode, expected values below are
    # the order produced by this implementation
    testcase = [
        [2, [[1, 0]], [0, 1]],
        [4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 1, 2, 3]],
        [1, [], [0]],
        [2, [[1, 0], [0, 1]], []],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.findOrder(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 10 of November 2026

    p1()

    p2()

    p3()
