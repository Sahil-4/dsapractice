from typing import List
from functools import cmp_to_key


class Solution1:
    def makeLargestSpecial(self, s: str) -> str:
        specials = []

        start = 0
        count = 0

        for i in range(len(s)):
            if s[i] == "1":
                count += 1
            else:
                count -= 1

            # upon balance
            if count == 0:
                # recursion for sub problem
                inner = s[start + 1 : i]
                specials.append("1" + self.makeLargestSpecial(inner) + "0")
                start = i + 1

        # sort DESC
        specials.sort(reverse=True)

        # return largest
        return "".join(specials)

        # Complexity analysis
        # Time : O(N*N)
        # Time : O(N)


def p1():
    # Problem 1 : POTD Leetcode 761. Special Binary String - https://leetcode.com/problems/special-binary-string/description/?envType=daily-question&envId=2026-02-20

    testcase = [
        ["11011000", "11100100"],
        ["10", "10"],
    ]

    for line in testcase:
        [s, expected] = line
        s1 = Solution1()
        result = s1.makeLargestSpecial(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findLargest(self, arr: List[int]) -> str:
        # Code here

        # custom comparator
        def comparator(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1

        # convert integers to strings
        strs = list(map(str, arr))

        # sort using custom comparator
        strs.sort(key=cmp_to_key(comparator))

        # handle leading zeros (e.g., [0, 0])
        if strs[0] == "0":
            return "0"

        # join and return result
        return "".join(strs)

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Form the Largest Number - https://www.geeksforgeeks.org/problems/largest-number-formed-from-an-array1117/1

    testcase = [
        [[3, 30, 34, 5, 9], "9534330"],
        [[54, 546, 548, 60], "6054854654"],
        [[3, 4, 6, 5, 9], "96543"],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.findLargest(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 20 of February 2026

    p1()

    p2()
