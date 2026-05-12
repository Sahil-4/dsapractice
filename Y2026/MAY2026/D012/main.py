from math import gcd
from typing import List


class Solution1:
    def is_possible(self, tasks: List[List[int]], energy: int) -> bool:
        for actual, minimum in tasks:
            if minimum > energy:
                return False
            energy -= actual

        return True

    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda task: task[1] - task[0], reverse=True)

        left, right = 0, 10**9
        answer = right

        while left <= right:
            mid = (left + right) // 2

            if self.is_possible(tasks, mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer

        # Complexity Analysis
        # Time : O(N * Log(N))
        # Space : O(N) modify input


def p1():
    # Problem 1 : POTD Leetcode 1665. Minimum Initial Energy to Finish Tasks - https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/description/?envType=daily-question&envId=2026-05-12

    testcase = [
        [[[1, 2], [2, 4], [4, 8]], 8],
        [[[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]], 32],
        [[[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]], 27],
    ]

    for line in testcase:
        [tasks, expected] = line
        s1 = Solution1()
        result = s1.minimumEffort(tasks)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def RangeLCMQuery(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # LCM(a, b) = (a // gcd(a, b)) * b
        def lcm(a: int, b: int) -> int:
            return (a // gcd(a, b)) * b

        n = len(arr)

        # Segment Tree
        tree = [1] * (4 * n)

        def build(node: int, start: int, end: int) -> None:
            if start == end:
                tree[node] = arr[start]
                return

            mid = (start + end) // 2

            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)

            tree[node] = lcm(tree[2 * node], tree[2 * node + 1])

        def update(node: int, start: int, end: int, idx: int, val: int) -> None:
            if start == end:
                arr[idx] = val
                tree[node] = val
                return

            mid = (start + end) // 2

            if idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)

            tree[node] = lcm(tree[2 * node], tree[2 * node + 1])

        def query(node: int, start: int, end: int, left: int, right: int) -> int:
            # No overlap
            if end < left or start > right:
                return 1

            # Complete overlap
            if left <= start and end <= right:
                return tree[node]

            # Partial overlap
            mid = (start + end) // 2

            left_lcm = query(2 * node, start, mid, left, right)
            right_lcm = query(2 * node + 1, mid + 1, end, left, right)

            return lcm(left_lcm, right_lcm)

        build(1, 0, n - 1)

        ans = []

        for query_info in queries:
            query_type, x, y = query_info

            # Update Query
            if query_type == 1:
                update(1, 0, n - 1, x, y)

            # Range LCM Query
            else:
                ans.append(query(1, 0, n - 1, x, y))

        return ans

        # Complexity Analysis
        # Time  : O(N + Q * log(N) * log(min(a, b)))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Range LCM Queries - https://www.geeksforgeeks.org/problems/range-lcm-queries3348/1

    testcase = [
        [[2, 3, 4, 6, 8, 16], [[2, 0, 2], [1, 3, 8], [2, 2, 5]], [12, 16]],
        [[1, 2, 3, 4], [[2, 0, 3], [1, 0, 5], [2, 0, 1]], [12, 10]],
    ]

    for line in testcase:
        [arr, queries, expected] = line
        s2 = Solution2()
        result = s2.RangeLCMQuery(arr, queries)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 12 of May 2026

    p1()

    p2()
