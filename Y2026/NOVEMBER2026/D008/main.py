class Solution1:
    def countServers(self, grid: list[list[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        rows = [0] * M
        cols = [0] * N

        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1

        count = 0

        for r in range(M):
            for c in range(N):

                if grid[r][c] != 1:
                    continue

                if rows[r] > 1 or cols[c] > 1:
                    count += 1

        return count

        # Complexity analysis
        # Time : O(M * N)
        # Space : O(M + N)


def p1():
    # Problem 1 : POTD Leetcode 1267. Count Servers that Communicate - https://leetcode.com/problems/count-servers-that-communicate/?envType=daily-question&envId=2026-11-08

    testcase = [
        [[[1, 0], [0, 1]], 0],
        [[[1, 0], [1, 1]], 3],
        [[[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 4],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.countServers(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        # code here

        t_time = 0

        c1 = s1
        c2 = s2

        for _ in range(n):
            if c1 < c2:
                t_time = max(t_time, c1)
                c1 += s1
            else:
                t_time = max(t_time, c2)
                c2 += s2

        return t_time

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Time with 2 Scanners - https://www.geeksforgeeks.org/problems/find-the-minimum-time0253/1

    testcase = [
        [2, 2, 4, 4],
        [2, 1, 3, 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minTime(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


from collections import deque


class Solution3:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # build adjacency list and in-degree array
        # prerequisites[i] = [course, pre_req] -> pre_req -> course

        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, pre_req in prerequisites:
            adj[pre_req].append(course)
            in_degree[course] += 1

        # enqueue all courses with no prerequisites (in-degree == 0)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        courses_taken = 0

        while queue:
            node = queue.popleft()
            courses_taken += 1

            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # if we could take all courses,
        # there is no cycle
        return courses_taken == numCourses

        # Complexity analysis:
        # Time  : O(V + E)
        # Space : O(V + E)


def p3():
    # Problem 3 : NC150 Leetcode 207. Course Schedule - https://leetcode.com/problems/course-schedule/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [2, [[1, 0]], True],
        [2, [[1, 0], [0, 1]], False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.canFinish(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 8 of November 2026

    p1()

    p2()

    p3()
