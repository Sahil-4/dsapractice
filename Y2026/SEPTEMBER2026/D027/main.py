class Solution1:
    def reverseParentheses(self, s: str) -> str:
        N = len(s)

        wormhole: list[int] = [0] * N
        open_bracket: list[int] = []

        for i in range(N):
            if s[i] == "(":
                open_bracket.append(i)
            elif s[i] == ")":
                j = open_bracket.pop()

                wormhole[i] = j
                wormhole[j] = i

        result: list[str] = []
        direction = 1

        i = 0
        while i < N:
            if s[i] in ["(", ")"]:
                # teleport
                i = wormhole[i]
                direction = -direction
            else:
                result.append(s[i])

            i += direction

        return "".join(result)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1190. Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/?envType=daily-question&envId=2026-09-27

    testcase = [
        ["(abcd)", "dcba"],
        ["(u(love)i)", "iloveu"],
        ["(ed(et(oc))el)", "leetcode"],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.reverseParentheses(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def longestPath(self, s: str, edges: list[list[int]]) -> int:
        N = len(s)

        # build graph
        graph = [[] for _ in range(N)]
        for u, v in edges:
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)

        # root at 0
        parent = [-1] * N
        order = [0]

        for u in order:
            for v in graph[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                order.append(v)

        # dp0[u]: Longest downward path
        # starting at u with 0 color changes
        # dp1[u]: Longest downward path
        # starting at u with at most 1 color change
        dp0 = [1] * N
        dp1 = [1] * N

        answer = 1

        # process children before parents
        for u in reversed(order):

            # 0 color changes branches
            # branch0 = (length including u, child)
            branch0 = []

            # at most 1 color changes branches
            # branch1 = (length including u, child)
            branch1 = []

            for v in graph[u]:
                if parent[v] != u:
                    continue

                color_changed = s[u] != s[v]

                if not color_changed:
                    # u -> v does not introduce a color change
                    branch0.append((1 + dp0[v], v))

                    # can still use at most one change inside v's subtree
                    branch1.append((1 + dp1[v], v))
                else:
                    # The edge u -> v itself uses the one allowed
                    # color change, so the rest must have zero changes
                    branch1.append((1 + dp0[v], v))

            branch0.sort(reverse=True)
            branch1.sort(reverse=True)

            # longest downward path with no color change
            if branch0:
                dp0[u] = branch0[0][0]

            # longest downward path with at most one color change
            if branch1:
                dp1[u] = branch1[0][0]

            answer = max(answer, dp0[u], dp1[u])

            # two zero-change branches
            if len(branch0) >= 2:
                candidate = branch0[0][0] + branch0[1][0] - 1
                answer = max(answer, candidate)

            # one zero-change branch + one one-change branch
            for length0, child0 in branch0[:2]:
                for length1, child1 in branch1[:2]:
                    if child0 != child1:
                        candidate = length0 + length1 - 1
                        answer = max(answer, candidate)

        return answer

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Longest Colored Path - https://www.geeksforgeeks.org/problems/longest-colored-path--151454/1

    testcase = [
        ["RBB", [[1, 2], [1, 3]], 2],
        ["BB", [[1, 2]], 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.longestPath(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def climbStairs(self, N: int) -> int:
        # base conditions
        prev_2 = 1
        prev_1 = 1

        for i in range(2, N + 1):
            curr = prev_2 + prev_1
            prev_2 = prev_1
            prev_1 = curr

        return prev_1

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 70. Climbing Stairs - https://leetcode.com/problems/climbing-stairs/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [2, 2],
        [3, 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.climbStairs(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 27 of September 2026

    p1()

    p2()

    p3()
