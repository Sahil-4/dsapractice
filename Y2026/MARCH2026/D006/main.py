class Solution1:
    def checkOnesSegment(self, s: str) -> bool:
        # traverse from i = 1 to i < N
        # init segments = 1
        # if s[i] == 1 and s[i-1] != 1
        # increment count of segments
        # finally count of segments should be 1 only

        N = len(s)

        segments = 1

        for i in range(1, N):
            if s[i] == "1" and s[i - 1] != "1":
                segments += 1

        return segments == 1

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1784. Check if Binary String Has at Most One Segment of Ones - https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description/?envType=daily-question&envId=2026-03-06

    testcase = [
        ["1001", False],
        ["110", True],
        ["1000", True],
        ["1111110000000", True],
        ["1111110010001", False],
    ]

    for line in testcase:
        [s, expected] = line
        s1 = Solution1()
        result = s1.checkOnesSegment(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def smallestWindow(self, s: str, p: str) -> str:
        # sliding window problem

        def char2index(char):
            return ord(char) - ord("a")

        smap = [0] * 26
        pmap = [0] * 26

        def valid_window():
            for i in range(26):
                if pmap[i] > smap[i]:
                    return False
            return True

        start, end = 0, len(s)

        # populate pmap
        for ch in p:
            pmap[char2index(ch)] += 1

        l = 0

        for r in range(len(s)):
            smap[char2index(s[r])] += 1

            while l <= r and valid_window():

                # update answer
                if (end - start) > (r - l):
                    start = l
                    end = r

                # shrink window
                smap[char2index(s[l])] -= 1
                l += 1

        if end == len(s):
            return ""

        return s[start : end + 1]

        # Complexity analysis
        # Time : O(N + M)
        # Space : O(N + M)


def p2():
    # Problem 2 : POTD Geeksforgeeks Smallest window containing all characters - https://www.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1

    testcase = [
        ["timetopractice", "toc", "toprac"],
        ["zoomlazapzo", "oza", "apzo"],
        ["zoom", "zooe", ""],
    ]

    for line in testcase:
        [s, p, expected] = line
        s2 = Solution2()
        result = s2.smallestWindow(s, p)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 6 of March 2026

    p1()

    p2()
