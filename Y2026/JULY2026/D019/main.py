class Solution1:
    def smallestSubsequence(self, s: str) -> str:
        # traverse the s from left to right
        # prepare a map of character of s to last index of that character in s
        # use stack, visited set
        # put character in stack
        # pop last character while
        # last character in stack is larger than current
        # and it has another occurrence on right
        # push current
        # update the visited set

        last_occurrence = {c: i for i, c in enumerate(s)}

        included = set()
        stack = []

        for i, c in enumerate(s):
            if c in included:
                continue

            while stack and stack[-1] > c and last_occurrence[stack[-1]] >= i:
                included.remove(stack.pop())

            stack.append(c)
            included.add(c)

        return "".join(stack)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1081. Smallest Subsequence of Distinct Characters - https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/?envType=daily-question&envId=2026-07-19

    testcase = [
        ["bcabc", "abc"],
        ["cbacdcbc", "acdb"],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.smallestSubsequence(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def processQueries(self, arr: list[int], queries: list[list[int]]) -> list[bool]:
        # code here

        N = len(arr)

        decreasing = [0] * N
        decreasing[N - 1] = N - 1
        for i in range(N - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                decreasing[i] = decreasing[i + 1]
            else:
                decreasing[i] = i

        increasing = [0] * N
        increasing[0] = 0
        for i in range(1, N):
            if arr[i] <= arr[i - 1]:
                increasing[i] = increasing[i - 1]
            else:
                increasing[i] = i

        result = []
        for l, r in queries:
            result.append(decreasing[l] >= increasing[r])

        return result

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Mountain Subarray Queries - https://www.geeksforgeeks.org/problems/mountain-subarray-problem/1

    testcase = [
        [
            [2, 3, 2, 4, 4, 6, 3, 2],
            [
                [0, 2],
                [1, 3],
            ],
            [True, False],
        ],
        [
            [2, 2, 2, 2],
            [
                [0, 2],
                [1, 3],
            ],
            [True, True],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.processQueries(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 19 of July 2026

    p1()

    p2()
