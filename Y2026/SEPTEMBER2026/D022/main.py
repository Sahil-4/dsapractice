from bisect import bisect_right
from collections import defaultdict


class Node:
    def __init__(self):
        self.cnt = [0] * 5
        self.prod = 0


class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.segTree = [Node() for _ in range(4 * self.n)]
        self.build(0, 0, self.n - 1, nums)

    def build(self, i, l, r, nums):
        if l == r:
            self.leafNode(i, nums[l])
            return

        mid = l + (r - l) // 2
        self.build(2 * i + 1, l, mid, nums)
        self.build(2 * i + 2, mid + 1, r, nums)
        self.segTree[i] = self.mergeNodes(
            self.segTree[2 * i + 1], self.segTree[2 * i + 2]
        )

    def leafNode(self, i, value):
        for x in range(self.k):
            self.segTree[i].cnt[x] = 0

        r = value % self.k
        self.segTree[i].cnt[r] = 1
        self.segTree[i].prod = r

    def mergeNodes(self, left, right):
        result = Node()
        result.prod = (left.prod * right.prod) % self.k

        for x in range(self.k):
            result.cnt[x] = left.cnt[x]

        for x in range(self.k):
            newRem = (left.prod * x) % self.k
            result.cnt[newRem] += right.cnt[x]

        return result

    def segTreeUpdate(self, i, l, r, index, value):
        if l == r:
            self.leafNode(i, value)
            return

        mid = l + (r - l) // 2

        if index <= mid:
            self.segTreeUpdate(2 * i + 1, l, mid, index, value)
        else:
            self.segTreeUpdate(2 * i + 2, mid + 1, r, index, value)

        self.segTree[i] = self.mergeNodes(
            self.segTree[2 * i + 1], self.segTree[2 * i + 2]
        )

    def update(self, index, value):
        self.segTreeUpdate(0, 0, self.n - 1, index, value)

    def segTreeQuery(self, start, end, i, l, r):
        if l >= start and r <= end:
            return self.segTree[i]

        mid = l + (r - l) // 2

        if end <= mid:
            return self.segTreeQuery(start, end, 2 * i + 1, l, mid)

        if start > mid:
            return self.segTreeQuery(start, end, 2 * i + 2, mid + 1, r)

        left = self.segTreeQuery(start, end, 2 * i + 1, l, mid)
        right = self.segTreeQuery(start, end, 2 * i + 2, mid + 1, r)

        return self.mergeNodes(left, right)

    def query(self, start, end):
        return self.segTreeQuery(start, end, 0, 0, self.n - 1)


class Solution1:
    def resultArray(
        self, nums: list[int], k: int, queries: list[list[int]]
    ) -> list[int]:

        n = len(nums)
        segTree = SegmentTree(nums, k)
        result = []

        for query in queries:
            index = query[0]
            value = query[1]
            start = query[2]
            x = query[3]

            segTree.update(index, value)

            node = segTree.query(start, n - 1)

            result.append(node.cnt[x])

        return result

        # Complexity analysis
        # Time : O((N + Q) * K * Log(N))
        # Space : O(N * K)


def p1():
    # Problem 1 : POTD Leetcode 3525. Find X Value of Array II - https://leetcode.com/problems/find-x-value-of-array-ii/description/?envType=daily-question&envId=2026-09-22

    testcase = [
        [[1, 2, 3, 4, 5], 3, [[2, 2, 0, 2], [3, 3, 3, 0], [0, 1, 0, 1]], [2, 2, 2]],
        [[1, 2, 4, 8, 16, 32], 4, [[0, 2, 0, 2], [0, 2, 0, 1]], [1, 0]],
        [[1, 1, 2, 1, 1], 2, [[2, 1, 0, 1]], [5]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.resultArray(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findLongestWord(self, s: str, d: list) -> str:
        # precompute positions of each character in s for fast subsequence checking
        char_indices = defaultdict(list)
        for idx, char in enumerate(s):
            char_indices[char].append(idx)

        best_word = ""

        for word in d:
            curr_pos = -1
            is_subsequence = True

            for char in word:
                positions = char_indices[char]
                # find the smallest index strictly greater than curr_pos
                next_idx_pos = bisect_right(positions, curr_pos)

                if next_idx_pos == len(positions):
                    is_subsequence = False
                    break

                curr_pos = positions[next_idx_pos]

            if is_subsequence:
                # update if longer, or if same length and lexicographically smaller
                if len(word) > len(best_word) or (
                    len(word) == len(best_word) and word < best_word
                ):
                    best_word = word

        return best_word

        # Complexity analysis
        # Time : O(S + N * M * log(S))
        # Space : O(S)


def p2():
    # Problem 2 : POTD Geeksforgeeks Longest Matching in Dictionary with Removals - https://www.geeksforgeeks.org/problems/find-largest-word-in-dictionary2430/1

    testcase = [
        ["abpcplea", ["ale", "apple", "monkey", "plea"], "apple"],
        ["abpcplea", ["a", "b", "c"], "a"],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.findLongestWord(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        _intervals = sorted(intervals)
        N = len(_intervals)

        merged_intervals = []

        prev_start = _intervals[0][0]
        prev_end = _intervals[0][1]

        for i in range(1, N + 1):
            if i == N or prev_end < _intervals[i][0]:
                merged_intervals.append([prev_start, prev_end])

                if i == N:
                    break

                prev_start = _intervals[i][0]
                prev_end = _intervals[i][1]
            else:
                prev_end = max(prev_end, _intervals[i][1])

        return merged_intervals

        # Complexity analysis
        # Time : O(N * Log(N) + 2N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 56. Merge Intervals - https://leetcode.com/problems/merge-intervals/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]],
        [[[1, 4], [4, 5]], [[1, 5]]],
        [[[4, 7], [1, 4]], [[1, 7]]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.merge(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        _intervals = sorted([*intervals, newInterval])
        N = len(_intervals)

        merged_intervals = []

        prev_start = _intervals[0][0]
        prev_end = _intervals[0][1]

        for i in range(1, N + 1):
            if i == N or prev_end < _intervals[i][0]:
                merged_intervals.append([prev_start, prev_end])

                if i == N:
                    break

                prev_start = _intervals[i][0]
                prev_end = _intervals[i][1]
            else:
                prev_end = max(prev_end, _intervals[i][1])

        return merged_intervals

        # Complexity analysis
        # Time : O(N * Log(N) + 2N)
        # Space : O(N)


def p4():
    # Problem 4 : NC150 Leetcode 57. Insert Interval - https://leetcode.com/problems/insert-interval/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            [[1, 3], [6, 9]],
            [2, 5],
            [[1, 5], [6, 9]],
        ],
        [
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.insert(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 22 of September 2026

    p1()

    p2()

    p3()

    p4()
