class Solution1:
    def maximumLengthSubstring(self, s: str) -> int:
        DELTA = 2
        N = len(s)

        max_subarray_length = 0
        frequency = dict()

        l = 0
        for r in range(N):
            if s[r] not in frequency:
                frequency[s[r]] = 0

            frequency[s[r]] += 1

            while frequency[s[r]] > DELTA:
                frequency[s[l]] -= 1
                l += 1

            max_subarray_length = max(max_subarray_length, r - l + 1)

        return max_subarray_length

        # Complexity analysis
        # Time : O(2N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3090. Maximum Length Substring With Two Occurrences - https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/?envType=daily-question&envId=2026-08-14

    testcase = [
        ["bcbbbcba", 4],
        ["aaaa", 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.maximumLengthSubstring(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def isPossible(self, arr: list[int], s: int, x: int) -> bool:
        if x == 0:
            return True

        # generate the sequence written on the paper
        seq = [s]
        paper_sum = s

        for val in arr:
            current = paper_sum + val
            seq.append(current)
            paper_sum += current

            # no generated number after this can be <= x
            if current > x:
                break

        # greedily select from largest to smallest
        target = x

        for i in range(len(seq) - 1, -1, -1):
            if seq[i] <= target:
                target -= seq[i]

                if target == 0:
                    return True

        return False

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Subset Sum on Generated Sequence - https://www.geeksforgeeks.org/problems/tricky-subset-problem1557/1

    testcase = [
        [[1, 2, 4, 2], 1, 7, True],
        [[51, 88], 100, 500, False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.isPossible(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 14 of August 2026

    p1()

    p2()
