import heapq
from collections import deque


class Solution1:
    def maxItems(self, items: list[list[int]], budget: int) -> int:
        max_factor = max(factor for factor, _ in items)

        # count[f] : number of item types with factor f,
        # multiples[f] : number of item types whose factor is a multiple of f (sieve)
        count = [0] * (max_factor + 1)
        for factor, _ in items:
            count[factor] += 1

        multiples = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            for k in range(f, max_factor + 1, f):
                multiples[f] += count[k]

        # buying c copies of type i gives min(c, g_i) free copies, where g_i is the number of
        # other types whose factor is a multiple of factor_i.
        # So the first g_i copies of a type are worth 2 each, any further copy is worth 1
        cheapest = min(price for _, price in items)

        # a copy worth 2 that costs more than two copies of the cheapest type is never needed :
        # two cheap copies are worth the same and cost less
        pairs = []
        for factor, price in items:
            g = multiples[factor] - 1

            if g > 0 and price <= 2 * cheapest:
                pairs.append((price, g))

        pairs.sort()

        # every kept copy costs at most 2 * cheapest, so replacing it by cheap copies
        # never gains anything : take the cheapest worth-2 copies while the budget allows
        remaining = budget
        copies = 0

        for price, g in pairs:
            take = min(g, remaining // price)
            copies += take
            remaining -= take * price

            if take < g:
                break

        # the rest of the budget buys copies of the cheapest type, worth 1 each
        return 2 * copies + remaining // cheapest

        # Complexity analysis
        # Time : O(N Log(N) + F Log(F)), F = maximum factor
        # Space : O(N + F)


def p1():
    # Problem 1 : POTD Leetcode 3947. Maximum Number of Items From Sale II - https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/description/?envType=daily-question&envId=2026-11-28

    testcase = [
        [[[1, 6], [2, 4], [3, 5]], 19, 5],
        [[[2, 8], [1, 10], [6, 6], [4, 12], [5, 20], [5, 17]], 35, 7],
        [[[1, 3]], 10, 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maxItems(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def checkPath(self, adj: list[list[int]], src: int, dest: int) -> bool:
        visited = [False] * len(adj)
        visited[src] = True
        queue = deque([src])

        # breadth first search from the source
        while queue:
            node = queue.popleft()

            if node == dest:
                return True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return False

        # Complexity analysis
        # Time : O(V + E)
        # Space : O(V)


def p2():
    # Problem 2 : POTD Geeksforgeeks Path Exists Between Two Vertices - https://www.geeksforgeeks.org/problems/path-exists/1

    testcase = [
        [[[1, 2], [0, 2], [0, 1], []], 0, 2, True],
        [[[1], [0], [3], [2]], 0, 3, False],
        [[[], []], 1, 1, True],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.checkPath(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def missingNumber(self, nums: list[int]) -> int:
        N = len(nums)

        # the numbers 0..N add up to N * (N + 1) / 2,
        # the missing one is the difference
        return N * (N + 1) // 2 - sum(nums)

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 268. Missing Number - https://leetcode.com/problems/missing-number/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[3, 0, 1], 2],
        [[0, 1], 2],
        [[9, 6, 4, 2, 3, 5, 7, 0, 1], 8],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.missingNumber(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k

        # min heap holding the k largest values seen so far, its root is the k-th largest
        self.heap = []

        for value in nums:
            self._push(value)

    def _push(self, value: int) -> None:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, value)
        elif value > self.heap[0]:
            heapq.heapreplace(self.heap, value)

    def add(self, val: int) -> int:
        self._push(val)

        return self.heap[0]

    # Complexity analysis
    # Time : O(Log(K)) per add, O(N Log(K)) to build
    # Space : O(K)


def p4():
    # Problem 4 : NC150 Leetcode 703. Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            ["KthLargest", "add", "add", "add", "add", "add"],
            [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
            [None, 4, 5, 5, 8, 8],
        ],
        [
            ["KthLargest", "add", "add", "add", "add", "add"],
            [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9], [1]],
            [None, 7, 7, 7, 8, 8],
        ],
    ]

    for line in testcase:
        [operations, arguments, expected] = line

        # design problem : run every operation in order on one object
        obj = None
        result = []
        for operation, argument in zip(operations, arguments):
            if operation == "KthLargest":
                obj = KthLargest(*argument)
                result.append(None)
            else:
                result.append(getattr(obj, operation)(*argument))

        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 28 of November 2026

    p1()

    p2()

    p3()

    p4()
