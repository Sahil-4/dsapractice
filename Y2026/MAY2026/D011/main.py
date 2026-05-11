from typing import List


class Solution1:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(digit) for num in nums for digit in str(num)]

        # Complexity analysis
        # Time : O(K)
        # Space : O(K)


def p1():
    # Problem 1 : POTD Leetcode 2553. Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/?envType=daily-question&envId=2026-05-11

    testcase = [
        [[13, 25, 83, 77], [1, 3, 2, 5, 8, 3, 7, 7]],
        [[7, 1, 3, 9], [7, 1, 3, 9]],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.separateDigits(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def palindromePair(self, arr: List[str]) -> bool:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        # reversed words -> indices
        reversed_words = {}

        for index, word in enumerate(arr):
            reversed_words[word[::-1]] = index

        # check every possible split
        for index, word in enumerate(arr):
            left = ""

            for split in range(len(word)):
                left += word[split]
                right = word[split + 1 :]

                # left is palindrome, need reverse(right)
                if (
                    left
                    and is_palindrome(left)
                    and right in reversed_words
                    and reversed_words[right] != index
                ):
                    return True

                # right is palindrome, need reverse(left)
                if (
                    is_palindrome(right)
                    and left in reversed_words
                    and reversed_words[left] != index
                ):
                    return True

        return False

        # Complexity Analysis
        # Time  : O(N * K * K)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Palindrome Pairs - https://www.geeksforgeeks.org/problems/palindrome-pairs/1

    testcase = [
        [["geekf", "geeks", "or", "keeg", "abc", "bc"], True],
        [["abc", "xyxcba", "geekst", "or", "bc"], True],
        [["aa"], False],
        [["aa", "aa", "bb"], True],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.palindromePair(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 11 of May 2026

    p1()

    p2()
