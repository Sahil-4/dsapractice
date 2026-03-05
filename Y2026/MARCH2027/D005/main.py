class Solution1:
    def minOperations(self, s: str) -> int:
        # only possible altering string can be
        # 1010... 1 on odd positions 0 on even positions
        # 0101... 0 on odd positions 1 on even positions
        # try both and calculate cost to build
        # finally return min cost

        cost1 = 0  # 0101...
        cost2 = 0  # 1010...

        N = len(s)

        for i in range(N):
            # if i & 1:
            #     cost1 += 1 if s[i] == "0" else 0
            #     cost2 += 1 if s[i] == "1" else 0
            # else:
            #     cost1 += 1 if s[i] == "1" else 0
            #     cost2 += 1 if s[i] == "0" else 0

            cost1 += (i & 1) if s[i] == "0" else int(not (i & 1))
            cost2 += (i & 1) if s[i] == "1" else int(not (i & 1))

        return min(cost1, cost2)

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1758. Minimum Changes To Make Alternating Binary String - https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/?envType=daily-question&envId=2026-03-05

    testcase = [
        ["0100", 1],
        ["10", 0],
        ["1111", 2],
    ]

    for line in testcase:
        [s, expected] = line
        s1 = Solution1()
        result = s1.minOperations(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def longestKSubstr(self, s, k):
        # code here

        N = len(s)

        llen = -1

        uniques = 0
        frequency_map = dict()

        l = 0
        for r in range(N):
            if s[r] not in frequency_map or frequency_map[s[r]] == 0:
                frequency_map[s[r]] = 0
                uniques += 1

            frequency_map[s[r]] += 1

            while uniques > k:
                frequency_map[s[l]] -= 1
                if frequency_map[s[l]] == 0:
                    uniques -= 1
                l += 1

            if uniques == k:
                llen = max(llen, r - l + 1)

        return llen

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Longest Substring with K Uniques - https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

    testcase = [
        ["aabacbebebe", 3, 7],
        ["aaaa", 2, -1],
        ["aabaaab", 2, 7],
    ]

    for line in testcase:
        [s, k, expected] = line
        s2 = Solution2()
        result = s2.longestKSubstr(s, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 5 of March 2026

    p1()

    p2()
