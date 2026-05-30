from typing import List
from sortedcontainers import SortedList


class Solution1:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        MAX_X = max(q[1] for q in queries) + 1

        # Segment tree: range max query, point update
        seg = [0] * (2 * MAX_X)

        def update(i: int, val: int) -> None:
            i += MAX_X
            seg[i] = val
            i >>= 1
            while i >= 1:
                seg[i] = max(seg[2 * i], seg[2 * i + 1])
                i >>= 1

        def query(l: int, r: int) -> int:
            # inclusive [l, r]
            res = 0
            l += MAX_X
            r += MAX_X + 1
            while l < r:
                if l & 1:
                    res = max(res, seg[l])
                    l += 1
                if r & 1:
                    r -= 1
                    res = max(res, seg[r])
                l >>= 1
                r >>= 1
            return res

        # SortedList tracks current obstacle positions; 0 is virtual obstacle
        obstacles: SortedList[int] = SortedList([0])
        # Gap stored at position p = p - prev_obstacle (gap to the left of p)
        # Initially only 0 exists, gap at 0 = 0
        update(0, 0)

        results = []

        for q in queries:
            if q[0] == 1:
                x = q[1]
                # Find neighbors
                idx = obstacles.bisect_left(x)
                prev_obs = obstacles[idx - 1]  # always exists (0 is sentinel)
                if idx < len(obstacles):
                    next_obs = obstacles[idx]  # obstacle immediately to right
                    # next_obs had gap = next_obs - prev_obs; now split
                    update(next_obs, next_obs - x)
                # New obstacle gap = x - prev_obs
                update(x, x - prev_obs)
                obstacles.add(x)

            else:  # q[0] == 2
                x, sz = q[1], q[2]
                # Max gap fully within [0, x] from segment tree
                max_gap = query(0, x)
                # Partial gap: from last obstacle <= x to x
                idx = obstacles.bisect_right(x) - 1
                last_obs = obstacles[idx]
                max_gap = max(max_gap, x - last_obs)
                results.append(max_gap >= sz)

        return results

        # Complexity Analysis
        # Time: O(Q * Log(N))
        # Space: O(N)


def p1():
    # Problem 1 : POTD Leetcode 3161. Block Placement Queries - https://leetcode.com/problems/block-placement-queries/description/?envType=daily-question&envId=2026-05-30

    testcase = [
        [[[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]], [False, True, True]],
        [[[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]], [True, True, False]],
    ]

    for line in testcase:
        [queries, expected] = line
        s1 = Solution1()
        result = s1.getResults(queries)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def replaceElements(self, arr: list[int]) -> None:
        N = len(arr)

        prev = arr[0]

        arr[0] = arr[0] ^ arr[1]

        for i in range(1, N - 1):
            curr = arr[i]
            arr[i] = prev ^ arr[i + 1]
            prev = curr

        arr[N - 1] = prev ^ arr[N - 1]

        # Complexity Analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Replace with XOR of Adjacent - https://www.geeksforgeeks.org/problems/replace-with-xor-of-adjacent/1

    testcase = [
        [[2, 1, 4, 7], [3, 6, 6, 3]],
        [[5, 9, 2, 6, 7], [12, 7, 15, 5, 1]],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        s2.replaceElements(arr)
        result = arr
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 30 of May 2026

    p1()

    p2()
