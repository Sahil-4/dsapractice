class Solution1:
    def smallestPalindrome(self, s: str, k: int) -> str:
        def comb(n: int, r: int) -> int:
            r = min(r, n - r)
            res = 1

            for i in range(1, r + 1):
                res = res * (n - i + 1) // i
                if res > k:
                    return k + 1

            return res

        n = len(s)
        half = n // 2

        freq = [0] * 26
        for i in range(half):
            freq[ord(s[i]) - ord("a")] += 1

        def count_permutations(rem: int) -> int:
            ways = 1

            for cnt in freq:
                if cnt == 0:
                    continue

                ways *= comb(rem, cnt)
                if ways > k:
                    return k + 1

                rem -= cnt

            return ways

        left = []
        rank = 1

        for pos in range(half):
            for ch in range(26):
                if freq[ch] == 0:
                    continue

                freq[ch] -= 1

                ways = count_permutations(half - pos - 1)

                if rank + ways > k:
                    left.append(chr(ch + ord("a")))
                    break

                rank += ways
                freq[ch] += 1

        if len(left) != half:
            return ""

        left = "".join(left)
        mid = s[half] if n & 1 else ""

        return left + mid + left[::-1]

        # Complexity Analysis
        # Time : O(n * 26 * (26 + min(n, log k)))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3518. Smallest Palindromic Rearrangement II - https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/description/?envType=daily-question&envId=2026-07-29

    testcase = [
        ["abba", 2, "baab"],
        ["aa", 2, ""],
        ["bacab", 1, "abcba"],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.smallestPalindrome(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minSubsets(self, arr: list[int]) -> int:
        # code here

        arr_set = set(arr)

        subset_count = 0

        for e in arr:
            if (e - 1) not in arr_set:
                subset_count += 1

        return subset_count

        # Complexity Analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Split Array into Minimum Subsets - https://www.geeksforgeeks.org/problems/split-array-into-minimum-subsets/1

    testcase = [
        [[100, 56, 5, 6, 102, 58, 101, 57, 7, 103, 59], 3],
        [[10, 100, 105], 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minSubsets(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 29 of July 2026

    p1()

    p2()
