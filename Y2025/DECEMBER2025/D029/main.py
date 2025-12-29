from typing import List


class Solution1:
    def __init__(self):
        self.memo = {}

    def solve(self, curr, mp, idx, above):
        # pyramid formed
        if len(curr) == 1:
            return True

        key = f"{curr}_{idx}_{above}"
        if key in self.memo:
            return self.memo[key]

        # move to next row
        if idx == len(curr) - 1:
            self.memo[key] = self.solve(above, mp, 0, "")
            return self.memo[key]

        pair = curr[idx : idx + 2]
        if pair not in mp:
            self.memo[key] = False
            return False

        # try all possible characters
        for ch in mp[pair]:
            if self.solve(curr, mp, idx + 1, above + ch):
                self.memo[key] = True
                return True

        self.memo[key] = False
        return False

    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = {}

        for pattern in allowed:
            pair = pattern[:2]
            ch = pattern[2]
            mp.setdefault(pair, []).append(ch)

        return self.solve(bottom, mp, 0, "")

        # Complexity analysis
        # Time : O((L^n))
        # Space : O(N^2)


def p1():
    # Problem 1 : POTD Leetcode 756. Pyramid Transition Matrix - https://leetcode.com/problems/pyramid-transition-matrix/description/?envType=daily-question&envId=2025-12-29

    testcase = [
        ["BCD", ["BCC", "CDE", "CEA", "FFF"], True],
        ["AAAA", ["AAB", "AAC", "BCD", "BBE", "DEF"], False],
    ]

    for line in testcase:
        [bottom, allowed, expected] = line
        s1 = Solution1()
        result = s1.pyramidTransition(bottom, allowed)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def kthElement(self, a, b, k):
        if len(a) > len(b):
            return self.kthElement(b, a, k)

        n, m = len(a), len(b)
        low = max(0, k - m)
        high = min(k, n)

        while low <= high:
            cutA = (low + high) // 2
            cutB = k - cutA

            leftA = float("-inf") if cutA == 0 else a[cutA - 1]
            leftB = float("-inf") if cutB == 0 else b[cutB - 1]

            rightA = float("inf") if cutA == n else a[cutA]
            rightB = float("inf") if cutB == m else b[cutB]

            if leftA <= rightB and leftB <= rightA:
                return max(leftA, leftB)
            elif leftA > rightB:
                high = cutA - 1
            else:
                low = cutA + 1

        # Complexity analysis
        # Time : O(Log(Min(a, b)))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks K-th element of two Arrays - https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1

    testcase = [
        [[2, 3, 6, 7, 9], [1, 4, 8, 10], 5, 6],
        [[1, 4, 8, 10, 12], [5, 7, 11, 15, 17], 6, 10],
    ]

    for line in testcase:
        [a, b, k, expected] = line
        s2 = Solution2()
        result = s2.kthElement(a, b, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 29 of December 2025

    p1()

    p2()
