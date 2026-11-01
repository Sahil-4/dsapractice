class Solution1:
    def minMoves(self, nums: list[int]) -> int:
        min_val = min(nums)
        moves = 0

        for num in nums:
            moves += num - min_val

        return moves

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 453. Minimum Moves to Equal Array Elements - https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/?envType=daily-question&envId=2026-11-01

    testcase = [
        [[1, 2, 3], 3],
        [[1, 1, 1], 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minMoves(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maximumSubarray(self, arr: list[int]) -> int:
        """code here"""
        N = len(arr)

        no_square = arr[0]
        has_square = arr[0] * arr[0]

        global_max = max(no_square, has_square)

        for i in range(1, N):
            val = arr[i]
            val_sq = val * val

            # need it to calculate the new has_square
            prev_no_square = no_square

            # 1. update no_square (Kadane)
            no_square = max(val, prev_no_square + val)

            # 2. update has_square (The 3 choices)
            has_square = max(
                val_sq,  # start fresh with a squared element
                prev_no_square + val_sq,  # append squared element to a normal streak
                has_square + val,  # append normal element to an already-squared streak
            )

            # 3. update final result global_max
            global_max = max(global_max, no_square, has_square)

        return global_max

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Maximum Subarray Sum with One Square Allowed - https://www.geeksforgeeks.org/problems/maximum-sum-subarray--143510/1

    testcase = [
        [[-1, -2, 3, -2, 3], 10],
        [[-4, -4, -2, 5, 2, -1], 27],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maximumSubarray(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        N = len(points)

        total_cost = 0

        visited = [False] * N
        min_dist = [float("inf")] * N
        min_dist[0] = 0

        for _ in range(N):
            curr_node = -1
            shortest_wire = float("inf")

            for i in range(N):
                if not visited[i] and min_dist[i] < shortest_wire:
                    shortest_wire = min_dist[i]
                    curr_node = i

            visited[curr_node] = True
            total_cost = total_cost + int(shortest_wire)

            for i in range(N):
                if visited[i]:
                    continue

                manhattan_dist = abs(points[curr_node][0] - points[i][0]) + abs(
                    points[curr_node][1] - points[i][1]
                )

                if manhattan_dist < min_dist[i]:
                    min_dist[i] = manhattan_dist

        return total_cost

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 1584. Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20],
        [[[3, 12], [-2, 5], [-4, 1]], 18],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.minCostConnectPoints(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 1 of November 2026

    p1()

    p2()

    p3()
