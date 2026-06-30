from bisect import bisect_left


class Solution1:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0

        frequency = {"a": 0, "b": 0, "c": 0}

        N = len(s)
        l = r = 0

        while r < N:
            frequency[s[r]] += 1

            while frequency["a"] > 0 and frequency["b"] > 0 and frequency["c"] > 0:
                count += N - r
                frequency[s[l]] -= 1
                l += 1

            r += 1

        return count

        # Complexity analysis
        # Time : O(2N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1358. Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/?envType=daily-question&envId=2026-06-30

    testcase = [
        ["abcabc", 10],
        ["aaacb", 3],
        ["abc", 1],
    ]

    for line in testcase:
        [s, expected] = line
        s1 = Solution1()
        result = s1.numberOfSubstrings(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minInsAndDel(self, a: list[int], b: list[int]) -> int:
        # code here

        # map b to its index
        index = {value: i for i, value in enumerate(b)}

        # convert a into the corresponding index sequence
        sequence = []
        for value in a:
            if value in index:
                sequence.append(index[value])

        # compute LIS length
        lis = []
        for value in sequence:
            pos = bisect_left(lis, value)
            if pos == len(lis):
                lis.append(value)
            else:
                lis[pos] = value

        lcs = len(lis)

        return (len(a) - lcs) + (len(b) - lcs)

        # Complexity analysis
        # Time : O((N + M) * log(M))
        # Space : O(M)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Insert and Delete to Convert - https://www.geeksforgeeks.org/problems/minimum-insertions-to-make-two-arrays-equal/1

    testcase = [
        [[1, 2, 5, 3, 1], [1, 3, 5], 4],
        [[1, 4], [1, 4], 0],
    ]

    for line in testcase:
        [a, b, expected] = line
        s2 = Solution2()
        result = s2.minInsAndDel(a, b)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 30 of June 2026

    p1()

    p2()
