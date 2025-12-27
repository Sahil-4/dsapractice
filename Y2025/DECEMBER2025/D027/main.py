import heapq
from typing import List


class Solution1:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # count of meetings per room
        room_count = [0] * n

        # sort meetings by start, then end
        meetings.sort(key=lambda x: (x[0], x[1]))

        # min-heaps
        # occupied: (end_time, room)
        occupied = []
        # available: room numbers
        available = list(range(n))
        heapq.heapify(available)

        for start, end in meetings:
            # free rooms that have finished
            while occupied and occupied[0][0] <= start:
                _, room = heapq.heappop(occupied)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(occupied, (end, room))
            else:
                end_time, room = heapq.heappop(occupied)
                new_end = end_time + (end - start)
                heapq.heappush(occupied, (new_end, room))

            room_count[room] += 1

        # room with max meetings (smallest index on tie)
        return room_count.index(max(room_count))

        # Complexity analysis
        # Time : O(M * N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 POTD Leetcode 2402. Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/?envType=daily-question&envId=2025-12-27

    testcase = [
        [2, [[0, 10], [1, 5], [2, 7], [3, 4]], 0],
        [3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]], 1],
    ]

    for line in testcase:
        [n, meetings, expected] = line
        s1 = Solution1()
        result = s1.mostBooked(n, meetings)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def kthSmallest(self, matrix, k):
        n = len(matrix)

        def count_smaller_equal(x):
            count = 0
            row = 0
            col = n - 1

            while row < n and col >= 0:
                if matrix[row][col] <= x:
                    count += col + 1
                    row += 1
                else:
                    col -= 1
            return count

        low = matrix[0][0]
        high = matrix[n - 1][n - 1]
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            smallers = count_smaller_equal(mid)

            if smallers < k:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1

        return ans

        # Complexity analysis
        # Time : O(Log(N * E))
        # Space : O(1)


def p2():
    # Problem 2 POTD Geeksforgeeks Kth smallest element in a Matrix - https://www.geeksforgeeks.org/problems/kth-element-in-matrix/1

    testcase = [
        [
            3,
            [
                [16, 28, 60, 64],
                [22, 41, 63, 91],
                [27, 50, 87, 93],
                [36, 78, 87, 94],
            ],
            27,
        ],
        [
            7,
            [
                [10, 20, 30, 40],
                [15, 25, 35, 45],
                [24, 29, 37, 48],
                [32, 33, 39, 50],
            ],
            30,
        ],
    ]

    for line in testcase:
        [matrix, k, expected] = line
        s2 = Solution2()
        result = s2.kthSmallest(matrix, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 27 of December 2025

    p1()

    p2()
