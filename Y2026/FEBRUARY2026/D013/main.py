class Solution1:
    def helper(self, s: str, ch1: str, ch2: str) -> int:
        diff_map = {}
        max_len = 0

        count1 = 0
        count2 = 0

        for i, ch in enumerate(s):
            # reset if other character appears
            if ch != ch1 and ch != ch2:
                diff_map.clear()
                count1 = count2 = 0
                continue

            if ch == ch1:
                count1 += 1
            if ch == ch2:
                count2 += 1

            if count1 == count2:
                max_len = max(max_len, count1 + count2)

            diff = count1 - count2

            if diff in diff_map:
                max_len = max(max_len, i - diff_map[diff])
            else:
                diff_map[diff] = i

        return max_len

    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0

        # Case 1: single repeated char (aaaa)
        count = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                count += 1
            else:
                max_len = max(max_len, count)
                count = 1
        max_len = max(max_len, count)

        # Case 2: two-character balance
        max_len = max(max_len, self.helper(s, "a", "b"))
        max_len = max(max_len, self.helper(s, "a", "c"))
        max_len = max(max_len, self.helper(s, "b", "c"))

        # Case 3: three-character balance
        countA = countB = countC = 0
        diff_map = {}

        for i, ch in enumerate(s):
            if ch == "a":
                countA += 1
            elif ch == "b":
                countB += 1
            else:
                countC += 1

            if countA == countB == countC:
                max_len = max(max_len, countA + countB + countC)

            diffAB = countA - countB
            diffAC = countA - countC
            key = (diffAB, diffAC)  # tuple instead of string (faster)

            if key in diff_map:
                max_len = max(max_len, i - diff_map[key])
            else:
                diff_map[key] = i

        return max_len

        # Complexity analysis
        # Time : O(n * log(n))
        # Space : O(n)


def p1():
    # Problem 1 : POTD Leetcode 3714. Longest Balanced Substring II - https://leetcode.com/problems/longest-balanced-substring-ii/description/?envType=daily-question&envId=2026-02-13

    testcase = [
        ["abbac", 4],
        ["aabcc", 3],
        ["aba", 2],
    ]

    for line in testcase:
        [s, expected] = line
        s1 = Solution1()
        result = s1.longestBalanced(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def isGreater(self, val, d):
        digitSum = 0
        tmp = val

        while tmp > 0:
            digitSum += tmp % 10
            tmp //= 10

        return val - digitSum >= d

    def getCount(self, n, d):
        # code here
        # binary search on answer

        mini = n + 1
        s = 1
        e = n

        while s <= e:
            mid = s + (e - s) // 2
            if self.isGreater(mid, d):
                mini = mid
                e = mid - 1
            else:
                s = mid + 1

        return n + 1 - mini

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks All numbers with specific difference - https://www.geeksforgeeks.org/problems/all-numbers-with-specific-difference3558/1

    testcase = [
        [13, 2, 4],
        [14, 3, 5],
    ]

    for line in testcase:
        [n, d, expected] = line
        s2 = Solution2()
        result = s2.getCount(n, d)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 13 of February 2026

    p1()

    p2()
