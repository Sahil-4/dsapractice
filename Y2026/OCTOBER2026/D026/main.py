class Solution1:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        # find islands total value using DFS
        # check if total value is divisible by k
        # increment count if divisible
        # return count

        count = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0

            total = grid[i][j]
            grid[i][j] = 0  # mark as visited

            total += dfs(i + 1, j)
            total += dfs(i - 1, j)
            total += dfs(i, j + 1)
            total += dfs(i, j - 1)

            return total

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    island_total = dfs(i, j)
                    if island_total % k == 0:
                        count += 1

        return count

        # Complexity Analysis
        # Time : O(M * N)
        # Space : O(M * N) stack


def p1():
    # Problem 1 : POTD Leetcode 3619. Count Islands With Total Value Divisible by K - https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/description/?envType=daily-question&envId=2026-10-26

    testcase = [
        [
            [
                [0, 2, 1, 0, 0],
                [0, 5, 0, 0, 5],
                [0, 0, 1, 0, 0],
                [0, 1, 4, 7, 0],
                [0, 2, 0, 0, 8],
            ],
            5,
            2,
        ],
        [[[3, 0, 3, 0], [0, 3, 0, 3], [3, 0, 3, 0]], 3, 6],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.countIslands(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minDiff(self, k: int, arr: list[int]) -> int:
        # code here
        N = len(arr)

        # Edge case: If removing 0 elements or array is empty
        if k == 0:
            return max(arr) - min(arr)
        if k >= N:
            return 0

        # Precompute prefix max and min
        prefix_min = [0] * N
        prefix_max = [0] * N
        prefix_min[0] = arr[0]
        prefix_max[0] = arr[0]
        for i in range(1, N):
            prefix_min[i] = min(prefix_min[i - 1], arr[i])
            prefix_max[i] = max(prefix_max[i - 1], arr[i])

        # Precompute suffix max and min
        suffix_min = [0] * N
        suffix_max = [0] * N
        suffix_min[-1] = arr[-1]
        suffix_max[-1] = arr[-1]
        for i in range(N - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], arr[i])
            suffix_max[i] = max(suffix_max[i + 1], arr[i])

        min_difference = float("inf")

        # Try removing every subarray arr[i : i + k]
        for i in range(N - k + 1):
            # Case 1: Removing from the start (i == 0)
            if i == 0:
                current_min = suffix_min[k]
                current_max = suffix_max[k]
            # Case 2: Removing from the end (i + k == N)
            elif i + k == N:
                current_min = prefix_min[i - 1]
                current_max = prefix_max[i - 1]
            # Case 3: Removing from the middle
            else:
                current_min = min(prefix_min[i - 1], suffix_min[i + k])
                current_max = max(prefix_max[i - 1], suffix_max[i + k])

            min_difference = min(min_difference, current_max - current_min)

        return int(min_difference)

        # Complexity Analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimize Max Min Diff with Subarray Removal - https://www.geeksforgeeks.org/problems/minimize-the-difference/1

    testcase = [
        [3, [1, 2, 3, 4, 5], 1],
        [3, [2, 3, 1, 4, 6, 7], 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minDiff(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head (MRU side) and dummy tail (LRU side)
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Splice out an existing node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node: Node) -> None:
        """Insert node right after head (marks as Most Recently Used)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # Evict LRU node (node right before tail)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]

            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)


def p3():
    # Problem 3 : NC150 Leetcode 146. LRU Cache - https://leetcode.com/problems/lru-cache/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            [None, None, None, 1, None, -1, None, -1, 3, 4],
        ]
    ]

    for commands, args, expected in testcase:
        obj = None
        result = []
        for cmd, arg in zip(commands, args):
            if cmd == "LRUCache":
                obj = LRUCache(arg[0])
                result.append(None)
            elif cmd == "put":
                obj.put(arg[0], arg[1])
                result.append(None)
            elif cmd == "get":
                result.append(obj.get(arg[0]))

        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 26 of October 2026

    p1()

    p2()

    p3()
