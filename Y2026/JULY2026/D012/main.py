from bisect import bisect_left
import heapq


class Solution1:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        copy_arr = list(set(arr))
        copy_arr.sort()

        ranks = []

        for el in arr:
            el_index = bisect_left(copy_arr, el)
            el_rank = el_index + 1

            ranks.append(el_rank)

        return ranks

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1331. Rank Transform of an Array - https://leetcode.com/problems/rank-transform-of-an-array/description/?envType=daily-question&envId=2026-07-12

    testcase = [
        [
            [40, 10, 20, 30],
            [4, 1, 2, 3],
        ],
        [
            [100, 100, 100],
            [1, 1, 1],
        ],
        [
            [37, 12, 28, 9, 100, 56, 80, 5, 12],
            [5, 3, 4, 2, 8, 6, 7, 1, 3],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.arrayRankTransform(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxAmount(self, arr: list[int], k: int) -> int:
        # code here
        MOD = 1000000007

        t_amount = 0

        max_pq = []
        for el in arr:
            heapq.heappush(max_pq, -el)

        while k > 0 and max_pq:
            t = -heapq.heappop(max_pq)
            if t - 1 > 0:
                heapq.heappush(max_pq, -(t - 1))

            t_amount = (t_amount + t) % MOD

            k -= 1

        return t_amount % MOD

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max Amount by Selling K Tickets - https://www.geeksforgeeks.org/problems/ticket-sellers3241/1

    testcase = [
        [[4, 3, 6, 2, 4], 3, 15],
        [[5, 3, 5, 2, 4, 4], 2, 10],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxAmount(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 12 of July 2026

    p1()

    p2()
