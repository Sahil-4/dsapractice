class Solution1:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        N = len(encodedText)
        cols = N // rows

        originalText = []

        for i in range(cols):
            index = i

            while index < N:
                originalText.append(encodedText[index])
                index += cols + 1

        return "".join(originalText).rstrip()

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2075. Decode the Slanted Ciphertext - https://leetcode.com/problems/decode-the-slanted-ciphertext/description/?envType=daily-question&envId=2026-04-04

    testcase = [
        ["ch   ie   pr", 3, "cipher"],
        ["iveo    eed   l te   olc", 4, "i love leetcode"],
        ["coding", 1, "coding"],
        [" b  ac", 2, " abc"],
    ]

    for line in testcase:
        [encodedText, rows, expected] = line
        s1 = Solution1()
        result = s1.decodeCiphertext(encodedText, rows)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def graycode(self, n):
        # code here

        if n == 1:
            return ["0", "1"]

        left = self.graycode(n - 1)
        right = left.copy()
        right.reverse()

        for i in range(len(left)):
            left[i] = "0" + left[i]
            right[i] = "1" + right[i]

        return left + right

        # Complexity analysis
        # Time : O(2 ^ N)
        # Space : O(N) stack


def p2():
    # Problem 2 : POTD Geeksforgeeks Gray Code - https://www.geeksforgeeks.org/problems/gray-code-1611215248/1

    testcase = [
        [
            2,
            ["00", "01", "11", "10"],
        ],
        [
            3,
            ["000", "001", "011", "010", "110", "111", "101", "100"],
        ],
    ]

    for line in testcase:
        [n, expected] = line
        s2 = Solution2()
        result = s2.graycode(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 4 of April 2026

    p1()

    p2()
