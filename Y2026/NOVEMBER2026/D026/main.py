from collections import defaultdict


class Solution1:
    def canAliceWin(self, n: int) -> bool:
        result = False
        remove = 10

        while remove != 0 and n >= remove:
            n -= remove
            result = not result
            remove -= 1

        return result

        # Complexity analysis
        # Time : O(10) -> O(1)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3360. Stone Removal Game - https://leetcode.com/problems/stone-removal-game/description/?envType=daily-question&envId=2026-11-26

    testcase = [
        [12, True],
        [1, False],
        [50, True],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.canAliceWin(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        # code here
        SN = len(s)
        QN = len(queries)

        VOWELS = set(["a", "e", "i", "o", "u"])

        result = [0] * QN

        prefix_sum = [0] * (SN + 1)

        for si in range(SN):
            prefix_sum[si + 1] = prefix_sum[si] + (1 if s[si] in VOWELS else 0)

        for qi in range(QN):
            l, r = queries[qi]

            vowels_count = prefix_sum[r + 1] - prefix_sum[l]
            result[qi] = vowels_count

        return result

        # Complexity analysis
        # Time : O(S + Q)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Range Vowel Count Queries - https://www.geeksforgeeks.org/problems/range-vowel-count-queries-static/1

    testcase = [
        ["geeksforgeeks", [[1, 3], [2, 4], [1, 9]], [2, 1, 4]],
        ["helloworld", [[0, 4], [5, 9], [0, 9]], [2, 1, 3]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.countVowels(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        character_frequency_s = defaultdict(int)
        for c in s:
            character_frequency_s[c] = character_frequency_s.get(c, 0) + 1

        for c in t:
            character_frequency_s[c] = character_frequency_s.get(c, 0) - 1

            if character_frequency_s.get(c) == 0:
                character_frequency_s.pop(c)

            if character_frequency_s.get(c) == -1:
                return False

        return len(character_frequency_s.keys()) == 0

        # Complexity analysis
        # Time : O(N + M)
        # Space : O(N + M)


def p3():
    # Problem 3 : NC150 Leetcode 242. Valid Anagram - https://leetcode.com/problems/valid-anagram/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["anagram", "nagaram", True],
        ["rat", "car", False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.isAnagram(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 26 of November 2026

    p1()

    p2()

    p3()
