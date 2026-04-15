from typing import List


class Solution1:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        N = len(words)

        for i in range(N):
            left = (startIndex - i + N) % N
            right = (startIndex + i + N) % N

            if words[left] == target or words[right] == target:
                return i

        return -1

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2515. Shortest Distance to Target String in a Circular Array - https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/description/?envType=daily-question&envId=2026-04-15

    testcase = [
        [["hello", "i", "am", "leetcode", "hello"], "hello", 1, 1],
        [["a", "b", "leetcode"], "leetcode", 0, 1],
        [["i", "eat", "leetcode"], "ate", 0, -1],
    ]

    for line in testcase:
        [words, target, startIndex, expected] = line
        s1 = Solution1()
        result = s1.closestTarget(words, target, startIndex)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def URLify(self, s):
        # code here
        splits = s.split(" ")
        return "%20".join(splits)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks URLify a given string - https://www.geeksforgeeks.org/problems/urlify-a-given-string--141625/1

    testcase = [
        ["i love programming", "i%20love%20programming"],
        ["Mr Benedict Cumberbatch", "Mr%20Benedict%20Cumberbatch"],
    ]

    for line in testcase:
        [s, expected] = line
        s2 = Solution2()
        result = s2.URLify(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 15 of April 2026

    p1()

    p2()
