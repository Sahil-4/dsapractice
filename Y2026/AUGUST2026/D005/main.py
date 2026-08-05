class Solution1:
    def remainingMethods(
        self, n: int, k: int, invocations: list[list[int]]
    ) -> list[int]:
        # assume the functions are nodes of tree
        # perform a tree traversal from node k
        # whatever node we encounter in traversal should be removed
        # we have collected nodes to be removed
        # now check other paths
        # if we can reach from any path or node to any node present in to be deleted set
        # we return all nodes - as not possible to remove any
        # else we return remaining nodes only
        # keep a set nodes_to_be_deleted = {}
        # approach use BFS to start traversing from node k
        # update set include nodes which are reachable from node k, including node k
        # than for each node not present in set nodes_to_be_deleted
        # check if its adjacent node is present in set nodes_to_be_deleted
        # if present return all nodes
        # finally return all nodes - nodes_to_be_deleted

        adjacency_map = [[] for _ in range(n)]
        for invocation in invocations:
            u, v = invocation
            adjacency_map[u].append(v)

        nodes_to_be_deleted: set[int] = set()

        visited = set([k])
        queue = [k]

        while queue:
            u = queue.pop()
            nodes_to_be_deleted.add(u)

            for v in adjacency_map[u]:
                if v in visited:
                    continue

                visited.add(v)
                queue.append(v)

        for connection in invocations:
            u, v = connection[0], connection[1]
            if v in nodes_to_be_deleted and u not in nodes_to_be_deleted:
                return list(range(n))

        remaining_nodes = []
        for i in range(n):
            if i not in nodes_to_be_deleted:
                remaining_nodes.append(i)

        return remaining_nodes

        # Complexity analysis
        # Time : O(V + E) + O(E)
        # Space : O(V + E)


def p1():
    # Problem 1 : POTD Leetcode 3310. Remove Methods From Project - https://leetcode.com/problems/remove-methods-from-project/description/?envType=daily-question&envId=2026-08-05

    testcase = [
        [4, 1, [[1, 2], [0, 1], [3, 2]], [0, 1, 2, 3]],
        [5, 0, [[1, 2], [0, 2], [0, 1], [3, 4]], [3, 4]],
        [3, 2, [[1, 2], [0, 1], [2, 0]], []],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.remainingMethods(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countSubarray(self, arr: list[int], l: int, r: int) -> int:
        # code here
        # sliding window + inclusion exclusion principle
        # count subarrays with sum at most r r_cnt
        # count subarrays with sum at most l-1 l_cnt
        # return r_cnt - l_cnt

        def count_subarray_sum_k(arr: list[int], k: int) -> int:
            """Count subarray with sum at most k"""

            N = len(arr)

            cnt = 0

            _sum = 0
            _s = 0
            _e = 0

            while _e < N:
                _sum += arr[_e]

                while _s <= _e and _sum > k:
                    _sum -= arr[_s]
                    _s += 1

                cnt += _e - _s + 1
                _e += 1

            return cnt

        r_cnt = count_subarray_sum_k(arr, r)
        l_cnt = count_subarray_sum_k(arr, l - 1)

        return r_cnt - l_cnt

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Subarrays with Sum in Range - https://www.geeksforgeeks.org/problems/count-the-number-of-subarrays/1

    testcase = [
        [[1, 4, 6], 3, 8, 3],
        [[2, 3, 5, 8], 4, 13, 6],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.countSubarray(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 5 of August 2026

    p1()

    p2()
