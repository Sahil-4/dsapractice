class Solution1:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        result = []

        frequency = [0] * 26
        for char in s:
            frequency[ord(char) - ord("a")] += 1

        curr = []
        greater_found = False

        def solve(index: int, greater_found: bool) -> bool:
            nonlocal result

            if index == len(s):
                if greater_found:
                    result = curr[:]
                    return True
                return False

            for i in range(26):
                if frequency[i] == 0:
                    continue

                if not greater_found and i < ord(target[index]) - ord("a"):
                    continue

                curr.append(chr(i + ord("a")))
                frequency[i] -= 1

                greater_found = greater_found or (i > ord(target[index]) - ord("a"))

                if solve(index + 1, greater_found):
                    return True

                curr.pop()
                frequency[i] += 1

            return False

        greater_found = solve(0, False)

        return "".join(curr) if greater_found else ""

        # Complexity Analysis
        # Time : O(N * 26)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3720. Lexicographically Smallest Permutation Greater Than Target - https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/description/?envType=daily-question&envId=2026-08-27

    testcase = [
        ["abc", "bba", "bca"],
        ["leet", "code", "eelt"],
        ["baba", "bbaa", ""],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.lexGreaterPermutation(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxArea(self, mat: list[list[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        # heights[j] = consecutive 1s ending at the current row
        heights = [0] * m
        ans = 0

        for i in range(n):
            # Update column heights
            for j in range(m):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Count frequencies of each height.
            # Height is at most n.
            freq = [0] * (n + 1)
            for h in heights:
                freq[h] += 1

            # Process heights from largest to smallest.
            width = 0
            for h in range(n, 0, -1):
                width += freq[h]
                ans = max(ans, h * width)

        return ans

        # Complexity Analysis
        # Time : O(N * (N + M))
        # Space : O(N + M)


def p2():
    # Problem 2 : POTD Geeksforgeeks Largest Rectangle with Column Swaps - https://www.geeksforgeeks.org/problems/find-the-largest-rectangle-of-1s-with-swapping-of-columns-allowed0243/1

    testcase = [
        [[[0, 1, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 1, 0]], 6],
        [[[0, 1, 1, 0, 0], [1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 1]], 12],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxArea(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 27 of August 2026

    p1()

    p2()
