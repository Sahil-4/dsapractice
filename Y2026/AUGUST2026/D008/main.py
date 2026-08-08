class Solution1:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        N, M = len(word1), len(word2)

        # next_match[j] = earliest index in word1 where word2[j:]
        # can be matched as a subsequence
        next_match = [-1] * M

        word2_index = M - 1

        for word1_index in range(N - 1, -1, -1):
            if word2_index < 0 or word1[word1_index] != word2[word2_index]:
                continue

            next_match[word2_index] = word1_index
            word2_index -= 1

        result = []
        word2_index = 0
        changed_char = False

        for word1_index, char in enumerate(word1):
            if word2_index == M:
                break

            if char == word2[word2_index] or (
                not changed_char
                and (word2_index == M - 1 or word1_index < next_match[word2_index + 1])
            ):
                changed_char |= char != word2[word2_index]
                result.append(word1_index)
                word2_index += 1

        return result if word2_index == M else []

        # Complexity analysis
        # Time : O(N)
        # Space : O(M)


def p1():
    # Problem 1 : POTD Leetcode 3302. Find the Lexicographically Smallest Valid Sequence - https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/description/?envType=daily-question&envId=2026-08-08

    testcase = [
        ["vbcca", "abc", [0, 1, 2]],
        ["bacdc", "abc", [1, 2, 4]],
        ["aaaaaa", "aaabc", []],
        ["abc", "ab", [0, 1]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.validSequence(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


# Disjoint Set Union
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x: int):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return False

        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        elif self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        else:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1

        return True


class Solution2:
    def minEdgesReq(self, n: int, edges: list[list[int]]) -> int:
        # code here

        dsu = DSU(n)
        extra_edges = 0

        for edge in edges:
            u, v = edge

            if not dsu.union(u, v):
                extra_edges += 1

        C = 0
        for p in range(n):
            if dsu.find(p) == p:
                C += 1

        return C - 1 if extra_edges >= C - 1 else -1

        # Complexity analysis
        # Time : O(E * A(V) + V * A(V))
        # Space : O(V)


def p2():
    # Problem 2 : POTD Geeksforgeeks Min Edge Movements to Connect a Graph - https://www.geeksforgeeks.org/problems/connecting-the-graph/1

    testcase = [
        [4, [[0, 1], [0, 2], [1, 2]], 1],
        [6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]], 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minEdgesReq(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 8 of August 2026

    p1()

    p2()
