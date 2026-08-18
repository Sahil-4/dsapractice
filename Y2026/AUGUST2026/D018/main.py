class Solution1:
    def largestInteger(self, nums: list[int], k: int) -> int:
        # frequency[x] = number of size-k subarrays
        # in which x appears
        # We use a set for every window because if x appears
        # multiple times in the same window, it should still
        # be counted as appearing in only ONE subarray

        N = len(nums)

        frequency = {}

        for i in range(N - k + 1):
            window = set(nums[i : i + k])

            for x in window:
                frequency[x] = frequency.get(x, 0) + 1

        largest_almost_missing = -1

        for x, count in frequency.items():
            if count == 1:
                largest_almost_missing = max(largest_almost_missing, x)

        return largest_almost_missing

        # Complexity analysis
        # Time : O((N - k + 1) * k)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3471. Find the Largest Almost Missing Integer - https://leetcode.com/problems/find-the-largest-almost-missing-integer/description/?envType=daily-question&envId=2026-08-18

    testcase = [
        [[3, 9, 2, 1, 7], 3, 7],
        [[3, 9, 7, 2, 1, 7], 4, 3],
        [[0, 0], 1, -1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.largestInteger(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def compress(self, s: str) -> str:
        # code here

        # prefix[i] = length of the longest proper prefix
        # of s[0:i+1] which is also a suffix
        # using KMP prefix function to identify prefixes
        # that can be compressed using '*'

        N = len(s)

        prefix = [0] * N

        # build KMP prefix function
        for i in range(1, N):
            j = prefix[i - 1]

            while j > 0 and s[i] != s[j]:
                j = prefix[j - 1]

            if s[i] == s[j]:
                j += 1

            prefix[i] = j

        result = []

        i = N - 1

        while i >= 0:
            length = i + 1

            # '*' can replace the second half only when
            # the current prefix has an even length
            if i % 2 == 1:
                half = length // 2

                # check whether the prefix can be represented
                # as two identical halves
                period = length - prefix[i]

                if prefix[i] >= half and length % (2 * period) == 0:
                    result.append("*")

                    # only need to encode its first half
                    # not complete string
                    i = half - 1
                    continue

            # current prefix cannot be compressed.
            result.append(s[i])
            i -= 1

        return "".join(reversed(result))

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Secret Cipher - https://www.geeksforgeeks.org/problems/secret-cipher--141631/1

    testcase = [
        ["ababcababcd", "ab*c*d"],
        ["zzzzzzz", "z*z*z"],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.compress(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 18 of August 2026

    p1()

    p2()
