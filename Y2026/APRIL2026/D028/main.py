from typing import List


class Solution1:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat_grid = [num for row in grid for num in row]
        flat_grid.sort()

        # if meeting possible
        mod = flat_grid[0] % x
        for num in flat_grid:
            if num % x != mod:
                return -1

        # meeting point - with least operations [1 > 2 > 3 < 4 < 5]
        meeting_point = flat_grid[len(flat_grid) // 2]

        # total operations
        operations = 0
        for num in flat_grid:
            operations += abs(num - meeting_point) // x

        return operations

        # Complexity analysis
        # Time : O(glen * log(glen))
        # Space : O(glen)


def p1():
    # Problem 1 : POTD Leetcode 2033. Minimum Operations to Make a Uni-Value Grid - https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description/?envType=daily-question&envId=2026-04-28

    testcase = [
        [[[2, 4], [6, 8]], 2, 4],
        [[[1, 5], [2, 3]], 1, 5],
        [[[1, 2], [3, 4]], 2, -1],
    ]

    for line in testcase:
        [grid, x, expected] = line
        s1 = Solution1()
        result = s1.minOperations(grid, x)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def longestSubstr(self, s: str, k: int) -> int:
        # Code here

        if len(s) == k:
            return k

        llen = 0
        max_freq = 0
        character_freq = dict()

        left = 0

        for right in range(len(s)):
            character_freq[s[right]] = 1 + character_freq.get(s[right], 0)

            max_freq = max(max_freq, character_freq[s[right]])

            while (right - left + 1) - max_freq > k:
                character_freq[s[left]] -= 1
                left += 1

                for key in character_freq:
                    max_freq = max(max_freq, character_freq[key])

            if (right - left + 1 - max_freq) <= k:
                llen = max(llen, right - left + 1)

        return llen

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Longest Repeating Character Replacement - https://www.geeksforgeeks.org/problems/longest-repeating-character-replacement/1

    testcase = [
        ["ABBA", 2, 4],
        ["ADBD", 1, 3],
    ]

    for line in testcase:
        [s, k, expected] = line
        s2 = Solution2()
        result = s2.longestSubstr(s, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 28 of April 2026

    p1()

    p2()
