from collections import deque


class Solution1:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        N = len(img1)

        def count_overlaps(row_diff: int, col_diff: int) -> int:
            count = 0

            for r in range(N):
                for c in range(N):
                    if r + row_diff < 0 or r + row_diff >= N:
                        continue
                    if c + col_diff < 0 or c + col_diff >= N:
                        continue

                    count += img1[r][c] * img2[r + row_diff][c + col_diff]

            return count

        max_overlap = 0

        for row_diff in range(-N + 1, N):
            for col_diff in range(-N + 1, N):
                overlaps = count_overlaps(row_diff, col_diff)
                max_overlap = max(max_overlap, overlaps)

        return max_overlap

        # Complexity analysis
        # Time : O(N^4)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 835. Image Overlap - https://leetcode.com/problems/image-overlap/description/?envType=daily-question&envId=2026-09-13

    testcase = [
        [[[1, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [0, 1, 1], [0, 0, 1]], 3],
        [[[1]], [[1]], 1],
        [[[0]], [[0]], 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.largestOverlap(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def partyHouse(self, adj: list[list[int]]) -> int:
        # code here

        # using two bfs approach

        V = len(adj)

        def bfs(source: int) -> tuple[int, int]:
            dist: list[int] = [-1] * V
            queue: deque[int] = deque()

            dist[source] = 0
            queue.append(source)

            farthest_node = source
            farthest_node_dist = 0

            while queue:
                u = queue.popleft()

                for v in adj[u]:
                    v = v - 1  # to zero based index

                    if dist[v] != -1:
                        continue

                    dist[v] = dist[u] + 1
                    queue.append(v)

                    if dist[v] > farthest_node_dist:
                        farthest_node = v
                        farthest_node_dist = dist[v]

            return (farthest_node, farthest_node_dist)

        v, _ = bfs(0)
        __, d2 = bfs(v)

        return (d2 + 1) // 2

        # Complexity analysis
        # Time : O(V + V)
        # Space : O(V)


def p2():
    # Problem 2 : POTD Geeksforgeeks Party in Town - https://www.geeksforgeeks.org/problems/party-in-town3951/1

    testcase = [
        [[[2], [1, 3, 4], [2], [2]], 1],
        [[[2], [1, 3], [2, 4], [3]], 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.partyHouse(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        N = len(candidates)

        result = []

        def helper(index: int, combination_sum: int, combination: list[int]):
            if combination_sum == target:
                result.append(combination[:])
                return

            if index == N:
                return

            # skip
            helper(index + 1, combination_sum, combination)

            # take
            if combination_sum + candidates[index] <= target:
                combination_sum += candidates[index]
                combination.append(candidates[index])
                helper(index, combination_sum, combination)
                combination.pop()
                combination_sum -= candidates[index]

        helper(0, 0, [])

        return result

        # Complexity analysis
        # Time : O(K * L) + Exponential
        # Space : O(N * T)


def p3():
    # Problem 3 : NC150 Leetcode 39. Combination Sum - https://leetcode.com/problems/combination-sum/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[2, 3, 6, 7], 7, [[2, 2, 3], [7]]],
        [[2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]],
        [[2], 1, []],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = sorted(s3.combinationSum(*inputs))
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        N = len(candidates)
        candidates.sort()

        result = []

        def helper(start: int, remaining_sum: int, combination: list[int]):
            if remaining_sum == 0:
                result.append(combination[:])
                return

            for index in range(start, N):

                if index > start and candidates[index] == candidates[index - 1]:
                    continue

                if remaining_sum < candidates[index]:
                    break

                combination.append(candidates[index])
                remaining_sum -= candidates[index]

                helper(index + 1, remaining_sum, combination)

                remaining_sum += candidates[index]
                combination.pop()

        helper(0, target, [])

        return result

        # Complexity analysis
        # Time : O(2 ^ N * N)
        # Space : O(N)


def p4():
    # Problem 4 : NC150 Leetcode 40. Combination Sum II - https://leetcode.com/problems/combination-sum-ii/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]],
        [[2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = sorted(s4.combinationSum2(*inputs))
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 13 of September 2026

    p1()

    p2()

    p3()

    p4()
