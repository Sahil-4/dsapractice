from typing import List


class Solution1:
    def longestBalanced(self, s: str) -> int:
        llen = 0

        N = len(s)

        def is_valid_window(frequency: List[int]) -> bool:
            minn = 10001
            maxx = -10001

            for i in range(26):
                if frequency[i] == 0:
                    continue
                minn = min(minn, frequency[i])
                maxx = max(maxx, frequency[i])

            return minn == maxx

        for i in range(N):
            frequency = [0] * 26

            for j in range(i, N):
                frequency[ord(s[j]) - ord("a")] += 1

                if is_valid_window(frequency):
                    llen = max(llen, j - i + 1)

        return llen

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(26)


def p1():
    # Problem 1 : POTD Leetcode 3713. Longest Balanced Substring I - https://leetcode.com/problems/longest-balanced-substring-i/description/?envType=daily-question&envId=2026-02-12

    testcase = [
        ["abbac", 4],
        ["zzabccy", 4],
        ["aba", 2],
    ]

    for line in testcase:
        [s, expected] = line
        s1 = Solution1()
        result = s1.longestBalanced(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def can_make_min(self, arr: List[int], k: int, w: int, limit: int) -> bool:
        n = len(arr)
        water = [0] * n

        for i in range(n):
            # prefix sum (difference array effect)
            if i > 0:
                water[i] += water[i - 1]

            curr_height = arr[i] + water[i]

            # remove effect outside window
            if i >= w:
                curr_height -= water[i - w]

            if curr_height < limit:
                need = limit - curr_height
                water[i] += need
                k -= need

                if k < 0:
                    return False

        return True

    def maxMinHeight(self, arr: List[int], k: int, w: int) -> int:
        low = min(arr)
        high = low + k
        output = low

        while low <= high:
            mid = (low + high) // 2

            if self.can_make_min(arr, k, w, mid):
                output = mid
                low = mid + 1
            else:
                high = mid - 1

        return output

        # Complexity analysis
        # Time : O(N * Log(E))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Max min Height - https://www.geeksforgeeks.org/problems/max-min-height--170647/1

    testcase = [
        [[2, 3, 4, 5, 1], 2, 2, 2],
        [[5, 8], 5, 1, 9],
    ]

    for line in testcase:
        [arr, k, w, expected] = line
        s2 = Solution2()
        result = s2.maxMinHeight(arr, k, w)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 12 of February 2026

    p1()

    p2()
