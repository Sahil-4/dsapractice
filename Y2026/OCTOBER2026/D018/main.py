import math


class Solution1:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def solve(arr: list[int]) -> int:
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            # Ways to interleave left and right elements: comb(len(left) + len(right), len(left))
            interleave = math.comb(len(left) + len(right), len(left)) % MOD

            return (interleave * solve(left) % MOD * solve(right) % MOD) % MOD

        # Subtract 1 to exclude the original array ordering
        return (solve(nums) - 1 + MOD) % MOD

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(N*N)


def p1():
    # Problem 1 : POTD Leetcode 1569. Number of Ways to Reorder Array to Get Same BST - https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/description/?envType=daily-question&envId=2026-10-18

    testcase = [
        [[2, 1, 3], 1],
        [[3, 4, 5, 1, 2], 5],
        [[1, 2, 3], 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.numOfWays(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minimumStep(self, n: int) -> int:
        # code here

        # traverse from right to left n -> 1
        # if n % 3 == 0, divide n by 3
        # else decrement n by 1

        steps = 0

        while n != 1:
            if n % 3 == 0:
                n //= 3
            else:
                n -= 1

            steps += 1

        return steps

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Shortest Path From 1 To n - https://www.geeksforgeeks.org/problems/shortest-path-from-1-to-n0156/1

    testcase = [
        [4, 2],
        [9, 2],
        [15, 4],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minimumStep(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def partition(self, s: str) -> list[list[str]]:
        N = len(s)

        result = []

        def is_palindrome(l: int, h: int) -> bool:
            while l < h:
                if s[l] != s[h]:
                    return False

                l += 1
                h -= 1

            return True

        palindromes = []

        def solve(i: int) -> None:
            if i == N:
                result.append(list(palindromes))
                return

            for l in range(1, N - i + 1):
                check = is_palindrome(i, i + l - 1)
                if not check:
                    continue

                string = s[i : i + l]
                palindromes.append(string)

                solve(i + l)

                palindromes.pop()

            return

        solve(0)

        return result

        # Complexity analysis
        # Time : O(N * 2^N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 131. Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["aab", [["a", "a", "b"], ["aa", "b"]]],
        ["a", [["a"]]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.partition(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 18 of October 2026

    p1()

    p2()

    p3()
