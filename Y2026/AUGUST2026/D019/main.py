from bisect import bisect_left, bisect_right


class Solution1:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # reserved seats for only the rows that actually have reservations
        rows = {}

        for row, seat in reservedSeats:
            rows[row] = rows.get(row, 0) | (1 << seat)

        # masks for the three possible 4-seat blocks
        LEFT = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        MIDDLE = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        RIGHT = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)

        # completely empty row can fit 2 families
        answer = (n - len(rows)) * 2

        # process only rows containing reserved seats
        for reserved in rows.values():
            left_available = (reserved & LEFT) == 0
            middle_available = (reserved & MIDDLE) == 0
            right_available = (reserved & RIGHT) == 0

            if left_available and right_available:
                # both non-overlapping blocks can be used
                answer += 2
            elif left_available or middle_available or right_available:
                # at least one block can be used
                answer += 1

        return answer

        # Complexity analysis
        # Time  : O(M)
        # Space : O(M)


def p1():
    # Problem 1 : POTD Leetcode 1386. Cinema Seat Allocation - https://leetcode.com/problems/cinema-seat-allocation/description/?envType=daily-question&envId=2026-08-19

    testcase = [
        [3, [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]], 4],
        [2, [[2, 1], [1, 8], [2, 6]], 2],
        [4, [[4, 3], [1, 4], [4, 6], [1, 7]], 4],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maxNumberOfFamilies(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        # code here

        arr_copy = arr.copy()
        arr_copy.sort()
        N = len(arr_copy)

        triplets_count = 0

        for i in range(N):
            for j in range(i + 1, N):
                l_bound = l - arr_copy[i] - arr_copy[j]
                r_bound = r - arr_copy[i] - arr_copy[j]

                left = bisect_left(arr_copy, l_bound, j + 1, N)
                right = bisect_right(arr_copy, r_bound, j + 1, N)

                triplets_count += right - left

        return triplets_count

        # Complexity analysis
        # Time : O(N * N * Log(N))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Triplets with Sum in Range - https://www.geeksforgeeks.org/problems/triplets-with-sum-with-given-range/1

    testcase = [
        [[8, 3, 5, 2], 7, 11, 1],
        [[5, 1, 4, 3, 2], 2, 7, 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.countTriplets(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 19 of August 2026

    p1()

    p2()
