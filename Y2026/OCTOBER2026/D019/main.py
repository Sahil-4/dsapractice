from collections import deque
from typing import Optional


class Solution1:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        # sorted position of target depends only on how many numbers are smaller,
        # and how many are equal, no need to actually sort
        smaller_count = 0
        equal_count = 0

        for num in nums:
            if num < target:
                smaller_count += 1
            elif num == target:
                equal_count += 1

        return list(range(smaller_count, smaller_count + equal_count))

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2089. Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/description/?envType=daily-question&envId=2026-10-19

    testcase = [
        [[1, 2, 5, 2, 3], 2, [1, 2]],
        [[1, 2, 5, 2, 3], 3, [3]],
        [[1, 2, 5, 2, 3], 5, [4]],
        [[1, 2, 5, 2, 3], 4, []],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.targetIndices(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def goodIndices(self, arr):
        # code here

        N = len(arr)

        # every index has exactly one outgoing jump (i -> i + arr[i]),
        # so the indices form a functional graph : paths that either leave the array
        # or end up in a cycle. an index is good only if its path leaves the array
        UNVISITED, ON_PATH, RESOLVED = 0, 1, 2

        state = [UNVISITED] * N
        good = [False] * N

        for start in range(N):
            if state[start] != UNVISITED:
                continue

            path = []
            i = start
            escapes = False

            while True:
                if i < 0 or i >= N:
                    escapes = True
                    break

                # reached an index whose answer is already known
                if state[i] == RESOLVED:
                    escapes = good[i]
                    break

                # came back to an index on the current path : cycle
                if state[i] == ON_PATH:
                    escapes = False
                    break

                state[i] = ON_PATH
                path.append(i)
                i += arr[i]

            # every index on this path shares the same fate
            for p in path:
                state[p] = RESOLVED
                good[p] = escapes

        return sum(good)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count Indices That Escape Array - https://www.geeksforgeeks.org/problems/good-stones--170647/1

    testcase = [
        [[2, 3, -1, 2, -2, 4, 1], 3],
        [[1], 1],
        [[0], 0],
        [[1, -1], 0],
        [[-1, 1, -1], 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.goodIndices(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    @staticmethod
    def from_list(adj: list[list[int]]) -> Optional["Node"]:
        # adj[i] holds the neighbors of the node with val i + 1
        if not adj:
            return None

        nodes = [Node(i + 1) for i in range(len(adj))]

        for i, neighbors in enumerate(adj):
            for val in neighbors:
                nodes[i].neighbors.append(nodes[val - 1])

        return nodes[0]

    @staticmethod
    def to_list(node: Optional["Node"]) -> list[list[int]]:
        if node is None:
            return []

        adj = {}
        seen = {node}
        q: deque[Node] = deque([node])

        while q:
            u = q.popleft()
            adj[u.val] = [v.val for v in u.neighbors]

            for v in u.neighbors:
                if v not in seen:
                    seen.add(v)
                    q.append(v)

        return [adj[val] for val in range(1, len(adj) + 1)]

    @staticmethod
    def collect(node: Optional["Node"]) -> set["Node"]:
        # every node reachable from node
        if node is None:
            return set()

        seen = {node}
        q: deque[Node] = deque([node])

        while q:
            u = q.popleft()

            for v in u.neighbors:
                if v not in seen:
                    seen.add(v)
                    q.append(v)

        return seen


class Solution3:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if node is None:
            return None

        # original node -> its clone
        clones = {node: Node(node.val)}
        q: deque[Node] = deque([node])

        while q:
            u = q.popleft()

            for v in u.neighbors:
                if v not in clones:
                    clones[v] = Node(v.val)
                    q.append(v)

                clones[u].neighbors.append(clones[v])

        return clones[node]

        # Complexity analysis
        # Time : O(V + E)
        # Space : O(V)


def p3():
    # Problem 3 : NC150 Leetcode 133. Clone Graph - https://leetcode.com/problems/clone-graph/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            Node.from_list([[2, 4], [1, 3], [2, 4], [1, 3]]),
            [[2, 4], [1, 3], [2, 4], [1, 3]],
        ],
        [Node.from_list([[]]), [[]]],
        [Node.from_list([]), []],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.cloneGraph(*inputs)
        assert (
            Node.to_list(result) == expected
        ), f"Test failed: expected {expected}, got {Node.to_list(result)}"
        # a deep copy must not share any node with the original graph
        assert not (
            Node.collect(result) & Node.collect(*inputs)
        ), "Test failed: shared nodes"
        print(f"Testcase passed (P3): result={Node.to_list(result)}")


if __name__ == "__main__":
    # Day 19 of October 2026

    p1()

    p2()

    p3()
