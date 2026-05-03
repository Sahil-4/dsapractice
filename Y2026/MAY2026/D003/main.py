from typing import List


class Solution1:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False

        s2 = s + s
        return s2.find(goal) != -1

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 796. Rotate String - https://leetcode.com/problems/rotate-string/description/?envType=daily-question&envId=2026-05-03

    testcase = [
        ["abcde", "cdeab", True],
        ["abcde", "abced", False],
    ]

    for line in testcase:
        [s, goal, expected] = line
        s1 = Solution1()
        result = s1.rotateString(s, goal)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def sortBySetBitCount(self, arr: List[int]) -> List[int]:
        # code here
        arr.sort(key=lambda x: -bin(x).count("1"))
        return arr

        # Complexity analysis
        # Time : O(N * Log(N) * Log(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Sort by Set Bit Count - https://www.geeksforgeeks.org/problems/sort-by-set-bit-count1153/1

    testcase = [
        [[5, 2, 3, 9, 4, 6, 7, 15, 32], [15, 7, 5, 3, 9, 6, 2, 4, 32]],
        [[1, 2, 3, 4, 5, 6], [3, 5, 6, 1, 2, 4]],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.sortBySetBitCount(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 3 of May 2026

    p1()

    p2()
