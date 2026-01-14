import math
from typing import List


class SegmentTree:
    def __init__(self, xs: List[int]):
        self.xs = xs
        self.n = len(xs) - 1
        self.count = [0] * (4 * self.n)
        self.covered = [0] * (4 * self.n)

    def update(self, sql, sqr, l, r, op, pos):
        if sqr <= self.xs[l] or sql >= self.xs[r + 1]:
            return

        if sql <= self.xs[l] and sqr >= self.xs[r + 1]:
            self.count[pos] += op
        else:
            mid = (l + r) // 2
            self.update(sql, sqr, l, mid, op, pos * 2 + 1)
            self.update(sql, sqr, mid + 1, r, op, pos * 2 + 2)

        if self.count[pos] > 0:
            self.covered[pos] = self.xs[r + 1] - self.xs[l]
        elif l == r:
            self.covered[pos] = 0
        else:
            self.covered[pos] = self.covered[pos * 2 + 1] + self.covered[pos * 2 + 2]

    def query(self):
        return self.covered[0]


class Solution1:
    def separateSquares(self, squares: List[List[int]]) -> float:
        xs = set()
        events = []

        for x, y, size in squares:
            xs.add(x)
            xs.add(x + size)
            events.append([y, x, x + size, 1])
            events.append([y + size, x, x + size, -1])

        events.sort()
        xs = sorted(xs)
        st = SegmentTree(xs)

        total_area = 0
        py = events[0][0]
        for y, sql, sqr, op in events:
            total_area += st.query() * (y - py)
            st.update(sql, sqr, 0, st.n - 1, op, 0)
            py = y

        acc_area = 0
        py = events[0][0]
        for y, sql, sqr, op in events:
            comb_width = st.query()
            curr_area = comb_width * (y - py)
            if acc_area + curr_area >= total_area / 2:
                return py + ((total_area / 2) - acc_area) / comb_width
            acc_area += curr_area
            st.update(sql, sqr, 0, st.n - 1, op, 0)
            py = y

        return 0

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3454. Separate Squares II - https://leetcode.com/problems/separate-squares-ii/description/?envType=daily-question&envId=2026-01-14

    BOUND = 0.00001  # 1e-5
    testcase = [
        [[[0, 0, 1], [2, 2, 1]], 1.00000],
        [[[0, 0, 2], [1, 1, 1]], 1.00000],
        [[[15, 21, 2], [19, 21, 3]], 22.30000],
    ]

    for line in testcase:
        [squares, expected] = line
        s1 = Solution1()
        result = s1.separateSquares(squares)
        assert math.isclose(
            result, expected, rel_tol=BOUND, abs_tol=BOUND
        ), f"Test failed: expected {expected}, got {result}"

        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def catchThieves(self, arr, k):
        # code here
        # use two pointers P, and T
        # init P with index of first 'P' in arr
        # init T with index of first 'T' in arr
        # while loop P < N and T < N
        # if abs(P - T) <= k
        # move P to next 'P'
        # move T to next 'T'
        # else move smaller index pointer to next
        # When a policeman and thief are too far apart,
        # the one with the smaller index can never be part of a valid future match,
        # so discarding it is safe and greedy-optimal

        N = len(arr)

        P = T = 0
        result = 0

        while P < N and arr[P] != "P":
            P += 1
        while T < N and arr[T] != "T":
            T += 1

        while P < N and T < N:
            if abs(P - T) <= k:
                P += 1
                T += 1
                result += 1
            elif P < T:
                P += 1
            else:
                T += 1

            while P < N and arr[P] != "P":
                P += 1
            while T < N and arr[T] != "T":
                T += 1

        return result

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Police and Thieves - https://www.geeksforgeeks.org/problems/police-and-thieves--141631/1

    testcase = [
        [["P", "T", "T", "P", "T"], 1, 2],
        [["T", "T", "P", "P", "T", "P"], 2, 3],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.catchThieves(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 14 of January 2026

    p1()

    p2()
