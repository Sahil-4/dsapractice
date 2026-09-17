from collections import deque


class Solution1:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        INT_MAX = 1000000000000

        N = len(arr)

        best_length_till_index = [INT_MAX] * N

        i, j = 0, 0

        best_min_length = INT_MAX
        result = INT_MAX

        curr_sum = 0

        while j < N:
            curr_sum += arr[j]

            while i < j and curr_sum > target:
                curr_sum -= arr[i]
                i += 1

            if curr_sum == target:
                length = j - i + 1

                if i > 0 and best_length_till_index[i - 1] != INT_MAX:
                    result = min(result, length + best_length_till_index[i - 1])

                best_min_length = min(best_min_length, length)

            best_length_till_index[j] = best_min_length
            j += 1

        return -1 if result == INT_MAX else result

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum - https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/description/?envType=daily-question&envId=2026-09-17

    testcase = [
        [[3, 2, 2, 4, 3], 3, 2],
        [[7, 3, 4, 7], 7, 2],
        [[4, 3, 2, 6, 2, 3, 4], 6, -1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minSumOfLengths(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minimumEdgeReversal(
        self, edges: list[list[int]], n: int, src: int, dst: int
    ) -> int:
        # code here
        INT_MAX = 100000000000

        # create adjacency list with both directions
        adj = [[] for _ in range(n + 1)]
        for edge in edges:
            u = edge[0]
            v = edge[1]

            # original direction requires no reversal
            adj[u].append([v, 0])

            # reverse direction requires one reversal
            adj[v].append([u, 1])

        # store the minimum reversals required to reach each node
        dist = [INT_MAX] * (n + 1)

        dq = deque()

        # distance of source is 0
        dist[src] = 0
        dq.appendleft(src)

        # 0-1 BFS
        while dq:
            node = dq.popleft()

            # adjacent nodes
            for edge in adj[node]:
                _next = edge[0]
                _cost = edge[1]

                # better path found
                if dist[node] + _cost < dist[_next]:
                    # update the distance
                    dist[_next] = dist[node] + _cost

                    # process zero-cost edges first
                    if _cost == 0:
                        dq.appendleft(_next)
                    else:
                        dq.append(_next)

        return -1 if dist[dst] == INT_MAX else dist[dst]

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Min Edge Reversals for Path - https://www.geeksforgeeks.org/problems/minimum-edges/1

    testcase = [
        [[[1, 2], [3, 2]], 3, 1, 3, 1],
        [[[1, 2], [2, 3], [3, 4]], 4, 1, 4, 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minimumEdgeReversal(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def rotate(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        Do not return anything, modify matrix in-place instead.
        """

        N = len(matrix)

        for i in range(N):
            for j in range(i, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(N):
            matrix[i].reverse()

        return matrix

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 48. Rotate Image - https://leetcode.com/problems/group-anagrams/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
        ],
        [
            [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
            [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.rotate(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def groupAnagrams(self, words: list[str]) -> list[list[str]]:
        def generate_hash(w: str) -> str:
            C = 26
            frequency = [0] * C

            for l in w:
                idx = ord(l) - ord("a")
                frequency[idx] += 1

            return ".".join(str(f) for f in frequency)

        mapped_groups: dict[str, list[str]] = dict()

        for word in words:
            _hash = generate_hash(word)

            if _hash not in mapped_groups:
                mapped_groups[_hash] = []

            mapped_groups[_hash].append(word)

        return [group for _, group in mapped_groups.items()]

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(N)


def p4():
    # Problem 4 : NC150 Leetcode 49. Group Anagrams - https://leetcode.com/problems/group-anagrams/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ],
        [
            [""],
            [[""]],
        ],
        [
            ["a"],
            [["a"]],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.groupAnagrams(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4: result={result}")


if __name__ == "__main__":
    # Day 17 of September 2026

    p1()

    p2()

    p3()

    p4()
