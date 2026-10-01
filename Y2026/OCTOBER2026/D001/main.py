from collections import deque


class Solution1:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or stack.pop() != mapping[char]:
                    return False

        return not stack

        # Complexity Analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 20. Valid Parentheses - https://leetcode.com/problems/valid-parentheses/description/?envType=daily-question&envId=2026-10-01

    testcase = [
        ["()", True],
        ["()[]{}", True],
        ["(]", False],
        ["([])", True],
        ["([)]", False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.isValid(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minTime(self, duration: list[int], dependencies: list[list[int]]) -> int:
        # code here

        N = len(duration)

        # dependency graph
        adj = [[] for _ in range(N)]
        indegree = [0] * N

        for u, v in dependencies:
            adj[u].append(v)
            indegree[v] += 1

        # earliest completion time for every module
        finishTime = duration[:]

        q = deque()

        # start with modules having no dependencies
        for i in range(N):
            if indegree[i] == 0:
                q.append(i)

        visited = 0
        m_time = 0

        # perform topological traversal
        while q:

            u = q.popleft()

            visited += 1
            m_time = max(m_time, finishTime[u])

            # update completion time of dependent modules
            for v in adj[u]:

                finishTime[v] = max(finishTime[v], finishTime[u] + duration[v])

                indegree[v] -= 1

                if indegree[v] == 0:
                    q.append(v)

        # cycle
        if visited != N:
            return -1

        return m_time

        # Complexity Analysis
        # Time : O(N + M)
        # Space : O(N + M)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Time to Finish Project - https://www.geeksforgeeks.org/problems/project-manager--141631/1

    testcase = [
        [
            [10, 20, 30, 10, 30, 20],
            [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]],
            80,
        ],
        [
            [5, 5, 5],
            [[0, 1], [1, 2], [2, 0]],
            -1,
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minTime(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def minWindow(self, s: str, t: str) -> str:

        def is_window_valid(arr1: list[int], arr2: list[int]) -> bool:
            for i in range(26):
                if arr1[i] > arr2[i]:
                    return False

            return True

        CL = 26

        t_upper = [0] * CL
        t_lower = [0] * CL

        for c in t:
            if c >= "a" and c <= "z":
                idx = ord(c) - ord("a")
                t_lower[idx] += 1
            elif c >= "A" and c <= "Z":
                idx = ord(c) - ord("A")
                t_upper[idx] += 1

        s_upper = [0] * CL
        s_lower = [0] * CL

        answer_i = -1
        answer_len = 0

        M = len(s)
        l = 0
        for r in range(M):
            c = s[r]

            if c >= "a" and c <= "z":
                idx = ord(c) - ord("a")
                s_lower[idx] += 1
            elif c >= "A" and c <= "Z":
                idx = ord(c) - ord("A")
                s_upper[idx] += 1

            while (
                l <= r
                and is_window_valid(t_lower, s_lower)
                and is_window_valid(t_upper, s_upper)
            ):
                if answer_len == 0 or answer_len > r - l + 1:
                    answer_i = l
                    answer_len = r - l + 1

                c = s[l]

                if c >= "a" and c <= "z":
                    idx = ord(c) - ord("a")
                    s_lower[idx] -= 1
                elif c >= "A" and c <= "Z":
                    idx = ord(c) - ord("A")
                    s_upper[idx] -= 1

                l += 1

        return s[answer_i : answer_i + answer_len] if answer_len != 0 else ""

        # Complexity Analysis
        # Time : O(N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 76. Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["ADOBECODEBANC", "ABC", "BANC"],
        ["a", "a", "a"],
        ["a", "aa", ""],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.minWindow(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)
        L = 2**N

        result = []

        for i in range(L):
            _subset = []

            for j in range(N):
                if (i >> j) & 1:
                    _subset.append(nums[j])

            result.append(_subset)

        return result

        # Complexity Analysis
        # Time : O(L * N)
        # Space : O(N)


def p4():
    # Problem 4 : NC150 Leetcode 78. Subsets - https://leetcode.com/problems/subsets/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            [1, 2, 3],
            [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
        ],
        [
            [0],
            [[], [0]],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.subsets(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 1 of October 2026

    p1()

    p2()

    p3()

    p4()
