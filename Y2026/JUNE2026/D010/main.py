import heapq
from typing import List


class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)

        self.max_val = [0] * (4 * self.n)
        self.min_val = [0] * (4 * self.n)

        self._build(1, 0, self.n - 1, nums)

    def _build(self, node: int, l: int, r: int, nums: List[int]):
        if l == r:
            self.max_val[node] = self.min_val[node] = nums[l]
            return

        m = (l + r) // 2

        self._build(node * 2, l, m, nums)
        self._build(node * 2 + 1, m + 1, r, nums)

        self.max_val[node] = max(self.max_val[node * 2], self.max_val[node * 2 + 1])
        self.min_val[node] = min(self.min_val[node * 2], self.min_val[node * 2 + 1])

    def query_max(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:
            return self.max_val[node]

        m = (l + r) // 2
        res = -(10**18)
        if ql <= m:
            res = max(res, self.query_max(node * 2, l, m, ql, qr))
        if qr > m:
            res = max(res, self.query_max(node * 2 + 1, m + 1, r, ql, qr))

        return res

    def query_min(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:
            return self.min_val[node]

        m = (l + r) // 2
        res = 10**18
        if ql <= m:
            res = min(res, self.query_min(node * 2, l, m, ql, qr))
        if qr > m:
            res = min(res, self.query_min(node * 2 + 1, m + 1, r, ql, qr))

        return res

    def query(self, l: int, r: int) -> int:
        """Returns max - min for range [l, r]."""
        return self.query_max(1, 0, self.n - 1, l, r) - self.query_min(
            1, 0, self.n - 1, l, r
        )


class Solution1:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seg = SegmentTree(nums)

        # max heap via negation; entry: (-value, l, r)
        pq = [(-seg.query(l, n - 1), l, n - 1) for l in range(n)]
        heapq.heapify(pq)

        ans = 0
        while k:
            neg_val, l, r = heapq.heappop(pq)
            ans -= neg_val
            k -= 1

            if r > l:
                heapq.heappush(pq, (-seg.query(l, r - 1), l, r - 1))

        return ans

        # Complexity analysis
        # Time : O((N + K) log N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3691. Maximum Total Subarray Value II - https://leetcode.com/problems/maximum-total-subarray-value-ii/description/?envType=daily-question&envId=2026-06-10

    testcase = [
        [[1, 3, 2], 2, 4],
        [[4, 2, 5, 1], 3, 12],
    ]

    for line in testcase:
        [nums, k, expected] = line
        s1 = Solution1()
        result = s1.maxTotalValue(nums, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def binarySearchable(self, arr):
        # code here 
        count = 0
        n = len(arr)

        for i in range(n):
            target = arr[i]
            l, r = 0, n - 1

            while l <= r:
                mid = (l + r) // 2

                if arr[mid] == target:
                    if mid == i:
                        count += 1
                    break
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

        return count

        # Complexity analysis
        # Time : O(N Log(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Binary Searchable Count - https://www.geeksforgeeks.org/problems/binary-searchable-elements/1

    testcase = [
        [[1, 3, 2], 2],
        [[2, 1, 3, 5, 4, 6], 4],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.binarySearchable(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 10 of June 2026

    p1()

    p2()
