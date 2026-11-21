import heapq
from collections import defaultdict


class Solution1:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        N = len(parent)

        children = [[] for _ in range(N)]
        for node in range(1, N):
            children[parent[node]].append(node)

        # last[c] : stack of the ancestors (on the current root-to-node path) holding character c,
        # its top is the closest ancestor with that character
        last = defaultdict(list)
        new_parent = parent[:]
        preorder = []

        # iterative DFS, (node, True) marks leaving the node
        stack = [(0, False)]
        while stack:
            node, leaving = stack.pop()

            if leaving:
                last[s[node]].pop()
                continue

            preorder.append(node)

            # closest ancestor with the same character becomes the new parent,
            # ancestors are taken from the original tree, all changes happen simultaneously
            if last[s[node]]:
                new_parent[node] = last[s[node]][-1]

            last[s[node]].append(node)
            stack.append((node, True))

            for child in children[node]:
                stack.append((child, False))

        # the new parent is always an ancestor of the node in the original tree,
        # so it appears earlier in the preorder : in reverse preorder every node
        # is complete before it is added to its new parent
        size = [1] * N
        for node in reversed(preorder):
            if node != 0:
                size[new_parent[node]] += size[node]

        return size

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3331. Find Subtree Sizes After Changes - https://leetcode.com/problems/find-subtree-sizes-after-changes/description/?envType=daily-question&envId=2026-11-21

    testcase = [
        [[-1, 0, 0, 1, 1, 1], "abaabc", [6, 3, 1, 1, 1, 1]],
        [[-1, 0, 4, 0, 1], "abbba", [5, 2, 1, 1, 1]],
        [[-1, 0, 1], "aaa", [3, 2, 1]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.findSubtreeSizes(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def smallestSubWithSum(self, x: int, arr: list[int]) -> int:
        N = len(arr)

        # sliding window,
        # valid because the elements are non-negative:
        # shrinking from the left never increases the sum
        smallest = N + 1
        window_sum = 0
        left = 0

        for right in range(N):
            window_sum += arr[right]

            while window_sum > x:
                smallest = min(smallest, right - left + 1)
                window_sum -= arr[left]
                left += 1

        return smallest if smallest <= N else 0

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Smallest Subarray Sum Greater Than x - https://www.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1

    testcase = [
        [51, [1, 4, 45, 6, 0, 19], 3],
        [100, [1, 10, 5, 2, 7], 0],
        [9, [1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 1],
        [0, [0, 0, 1], 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.smallestSubWithSum(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))

        # Dijkstra from k,
        # the answer is the largest shortest distance
        distance = [float("inf")] * (n + 1)
        distance[k] = 0
        heap = [(0, k)]

        while heap:
            d, node = heapq.heappop(heap)

            if d > distance[node]:
                continue

            for neighbor, weight in graph[node]:
                if d + weight < distance[neighbor]:
                    distance[neighbor] = d + weight
                    heapq.heappush(heap, (distance[neighbor], neighbor))

        answer = max(distance[1:])

        return int(answer if answer != float("inf") else -1)

        # Complexity analysis
        # Time : O(E * Log(V))
        # Space : O(V + E)


def p3():
    # Problem 3 : NC150 Leetcode 743. Network Delay Time - https://leetcode.com/problems/network-delay-time/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2],
        [[[1, 2, 1]], 2, 1, 1],
        [[[1, 2, 1]], 2, 2, -1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.networkDelayTime(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 21 of November 2026

    p1()

    p2()

    p3()
