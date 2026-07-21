from cmath import inf


class Solution1:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        N = len(s)

        bestGain = 0
        _prev = -inf

        i = 0
        while i < N:
            start = i

            while i < N and s[i] == s[start]:
                i += 1

            if s[start] == "0":
                cur = i - start
                bestGain = max(bestGain, _prev + cur)
                _prev = cur

        count_1 = s.count("1")
        return int(count_1 + bestGain)

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3499. Maximize Active Section with Trade I - https://leetcode.com/problems/maximize-active-section-with-trade-i/description/?envType=daily-question&envId=2026-07-21

    testcase = [
        ["01", 1],
        ["0100", 4],
        ["1000100", 7],
        ["01010", 4],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maxActiveSectionsAfterTrade(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxIndexDifference(self, s: str) -> int:
        N = len(s)

        # best[ch] = maximum reachable ending index starting
        # from any occurrence of character ch seen so far (to the right)
        best = [-1] * 26

        answer = -1

        for i in range(N - 1, -1, -1):

            curr = ord(s[i]) - ord("a")

            # by default, can always stay at itself
            furthest = i

            # if next character exists and is reachable, inherit its end
            if curr < 25 and best[curr + 1] != -1:
                furthest = best[curr + 1]

            # update best occurrence of this character
            best[curr] = max(best[curr], furthest)

            # candidate answer
            if curr == 0:
                answer = max(answer, furthest - i)

        return answer

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Maximum Reachable Index Difference - https://www.geeksforgeeks.org/problems/maximum-reachable-index-difference/1

    testcase = [
        ["aaabcb", 5],
        ["xynjir", -1],
        ["abcbzzd", 6],
        ["dhoxjfrqfaa", 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxIndexDifference(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 21 of July 2026

    p1()

    p2()
