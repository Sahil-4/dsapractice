class Solution1:
    def numberOfSpecialChars(self, word: str) -> int:
        character_set = set()
        special_characters = set()

        for char in word:
            if char.upper() in special_characters:
                continue

            if char >= "A" and char <= "Z":
                if char.lower() in character_set:
                    special_characters.add(char)
            elif char >= "a" and char <= "z":
                if char.upper() in character_set:
                    special_characters.add(char.upper())

            character_set.add(char)

        return len(special_characters)

        # Complexity Analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3120. Count the Number of Special Characters I - https://leetcode.com/problems/count-the-number-of-special-characters-i/description/?envType=daily-question&envId=2026-05-26

    testcase = [
        ["aaAbcBC", 3],
        ["abc", 0],
        ["abBCab", 1],
    ]

    for line in testcase:
        [word, expected] = line
        s1 = Solution1()
        result = s1.numberOfSpecialChars(word)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minToggle(self, arr: list[int]) -> int:
        # code here

        N = len(arr)

        min_operations = N

        zeroes = 0
        ones = 0

        for i in range(N):
            if arr[i] == 0:
                zeroes += 1

        min_operations = min(min_operations, zeroes + ones)

        for i in range(N):
            if arr[i] == 0:
                zeroes -= 1
            else:
                ones += 1

            min_operations = min(min_operations, zeroes + ones)

        return min_operations

        # Complexity Analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Toggle to Partition - https://www.geeksforgeeks.org/problems/minimum-toogles-to-partition0135/1

    testcase = [
        [[1, 0, 1, 1, 0], 2],
        [[0, 1, 0, 0, 1, 1, 1], 1],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.minToggle(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 26 of May 2026

    p1()

    p2()
