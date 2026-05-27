class Solution1:
    def numberOfSpecialChars(self, word: str) -> int:
        occurrence_map = dict()

        for i, char in enumerate(word):
            if char >= "a" and char <= "z":
                # last occurrence of lower char is at index i
                occurrence_map[char] = i
            elif char >= "A" and char <= "Z" and char not in occurrence_map:
                # first occurrence of upper char is at index i
                occurrence_map[char] = i

        special_character_count = 0
        for char in range(ord("A"), ord("Z") + 1):
            upper_char = chr(char)
            lower_char = chr(char + 32)

            if upper_char in occurrence_map and lower_char in occurrence_map:
                if occurrence_map[lower_char] < occurrence_map[upper_char]:
                    special_character_count += 1

        return special_character_count

        # Complexity Analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3121. Count the Number of Special Characters II - https://leetcode.com/problems/count-the-number-of-special-characters-ii/description/?envType=daily-question&envId=2026-05-27

    testcase = [
        ["aaAbcBC", 3],
        ["abc", 0],
        ["AbBCab", 0],
    ]

    for line in testcase:
        [word, expected] = line
        s1 = Solution1()
        result = s1.numberOfSpecialChars(word)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def wifiRange(self, s: str, x: int) -> bool:
        # code here

        N = len(s)

        cover = [0] * (N + 1)

        for i in range(N):
            if s[i] == "1":
                left = max(0, i - x)
                right = min(N - 1, i + x)

                cover[left] += 1

                if right + 1 < N:
                    cover[right + 1] -= 1

        curr = 0

        for i in range(N):
            curr += cover[i]

            if curr <= 0:
                return False

        return True

        # Complexity Analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Wifi Range - https://www.geeksforgeeks.org/problems/wifi-range--170647/1

    testcase = [
        [0, "010", False],
        [1, "10010", True],
    ]

    for line in testcase:
        [x, s, expected] = line
        s2 = Solution2()
        result = s2.wifiRange(s, x)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 27 of May 2026

    p1()

    p2()
