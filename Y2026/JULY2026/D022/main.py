from bisect import bisect_left, bisect_right


class RangeMaxTree:
    """Bottom-up segment tree answering range maximum over a static array."""

    def __init__(self, values: list[int]) -> None:
        self.width = len(values)
        self.nodes = [0] * (2 * self.width)
        self.nodes[self.width :] = values

        for parent in range(self.width - 1, 0, -1):
            self.nodes[parent] = max(
                self.nodes[parent << 1], self.nodes[parent << 1 | 1]
            )

    def range_max(self, lo: int, hi: int) -> int:
        """Maximum over the inclusive interval [lo, hi]; 0 when empty."""
        if lo > hi:
            return 0

        best = 0

        lo += self.width
        hi += self.width + 1

        while lo < hi:
            if lo & 1:
                best = max(best, self.nodes[lo])
                lo += 1
            if hi & 1:
                hi -= 1
                best = max(best, self.nodes[hi])
            lo >>= 1
            hi >>= 1

        return best


class Solution1:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: list[list[int]]
    ) -> list[int]:
        N = len(s)
        active_total = s.count("1")

        gap_start: list[int] = []
        gap_end: list[int] = []
        gap_size: list[int] = []

        cursor = 0
        while cursor < N:
            if s[cursor] == "1":
                cursor += 1
                continue
            run_begin = cursor
            while cursor < N and s[cursor] == "0":
                cursor += 1
            gap_start.append(run_begin)
            gap_end.append(cursor - 1)
            gap_size.append(cursor - run_begin)

        gap_count = len(gap_size)
        if gap_count < 2:
            return [active_total] * len(queries)

        # fused[k] = sections gained by merging inactive runs k and k + 1
        fused = [gap_size[k] + gap_size[k + 1] for k in range(gap_count - 1)]
        tree = RangeMaxTree(fused)

        answer: list[int] = []
        for left, right in queries:
            head = bisect_left(gap_end, left)
            tail = bisect_right(gap_start, right) - 1

            if head >= gap_count or tail < 0 or head >= tail:
                answer.append(active_total)
                continue

            head_len = gap_end[head] - max(gap_start[head], left) + 1
            tail_len = min(gap_end[tail], right) - gap_start[tail] + 1

            if tail == head + 1:
                answer.append(active_total + head_len + tail_len)
                continue

            best_gain = max(
                head_len + gap_size[head + 1],
                gap_size[tail - 1] + tail_len,
                tree.range_max(head + 1, tail - 2),
            )
            answer.append(active_total + best_gain)

        return answer

        # Complexity analysis
        # Time : O(N + Q * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3501. Maximize Active Section with Trade II - https://leetcode.com/problems/maximize-active-section-with-trade-ii/description/?envType=daily-question&envId=2026-07-22

    testcase = [
        ["01", [[0, 1]], [1]],
        ["0100", [[0, 3], [0, 2], [1, 3], [2, 3]], [4, 3, 1, 1]],
        ["1000100", [[1, 5], [0, 6], [0, 4]], [6, 7, 2]],
        ["01010", [[0, 3], [1, 4], [1, 3]], [4, 4, 2]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maxActiveSectionsAfterTrade(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minDeletions(self, arr: list[int]) -> int:
        # code here
        # find longest strictly increasing subsequence length l_lis
        # return N - l_lis

        tails = []

        for num in arr:

            # first tail >= num
            lo = bisect_left(tails, num)

            # extend LIS - if num is greater than all tails
            if lo == len(tails):
                tails.append(num)

            # maintain smallest possible tail
            else:
                tails[lo] = num

        return len(arr) - len(tails)

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Deletions to Make Sorted - https://www.geeksforgeeks.org/problems/minimum-number-of-deletions-to-make-a-sorted-sequence3248/1

    testcase = [
        [[5, 6, 1, 7, 4], 2],
        [[1, 1, 1], 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minDeletions(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 22 of July 2026

    p1()

    p2()
