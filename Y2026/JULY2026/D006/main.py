class Solution1:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        # sort by increasing start and decreasing end
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))

        remaining_intervals = 0

        previous_start = -1
        previous_end = -1

        for current_start, current_end in intervals:
            # current interval is covered by the previous interval
            if current_start >= previous_start and current_end <= previous_end:
                continue

            remaining_intervals += 1

            previous_start = current_start
            previous_end = current_end

        return remaining_intervals

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1288. Remove Covered Intervals - https://leetcode.com/problems/remove-covered-intervals/description/?envType=daily-question&envId=2026-07-06

    testcase = [
        [[[1, 4], [3, 6], [2, 8]], 2],
        [[[1, 4], [2, 3]], 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.removeCoveredIntervals(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxPathSum(self, a: list[int], b: list[int]) -> int:
        N = len(a)
        M = len(b)

        index_a = 0
        index_b = 0

        prefix_sum_a = 0
        prefix_sum_b = 0

        maximum_path_sum = 0

        while index_a < N and index_b < M:
            if a[index_a] < b[index_b]:
                prefix_sum_a += a[index_a]
                index_a += 1

            elif a[index_a] > b[index_b]:
                prefix_sum_b += b[index_b]
                index_b += 1

            else:
                common_value = a[index_a]

                maximum_path_sum += max(prefix_sum_a, prefix_sum_b) + common_value

                prefix_sum_a = 0
                prefix_sum_b = 0

                index_a += 1
                index_b += 1

        while index_a < N:
            prefix_sum_a += a[index_a]
            index_a += 1

        while index_b < M:
            prefix_sum_b += b[index_b]
            index_b += 1

        maximum_path_sum += max(prefix_sum_a, prefix_sum_b)

        return maximum_path_sum

        # Complexity analysis
        # Time : O(N + M)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Sum Path in Two Arrays - https://www.geeksforgeeks.org/problems/max-sum-path-in-two-arrays/1

    testcase = [
        [[2, 3, 7, 10, 12], [1, 5, 7, 8], 35],
        [[1, 2, 3], [3, 4, 5], 15],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxPathSum(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 6 of July 2026

    p1()

    p2()
