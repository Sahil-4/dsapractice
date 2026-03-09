from functools import lru_cache


class Solution1:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def solve(ones_left: int, zeros_left: int, last_one: bool) -> int:
            if ones_left < 0 or zeros_left < 0:
                return 0

            if ones_left == 0 and zeros_left == 0:
                return 1

            result = 0

            if last_one:
                for i in range(1, min(zeros_left, limit) + 1):
                    result += solve(ones_left, zeros_left - i, False) % MOD
            else:
                for i in range(1, min(ones_left, limit) + 1):
                    result += solve(ones_left - i, zeros_left, True) % MOD

            # tlimit = min(ones_left, limit) if last_one else min(zeros_left, limit)
            # for i in range(1, tlimit + 1):
            #     new_ones_left = ones_left - i if last_one else ones_left
            #     new_zeros_left = zeros_left - i if not last_one else zeros_left
            #     result += solve(new_ones_left, new_zeros_left, not last_one) % MOD

            return result % MOD

        output = 0
        output += solve(one, zero, False) % MOD
        output += solve(one, zero, True) % MOD

        return output % MOD

        # Complexity analysis
        # Time : O(Z * O * L)
        # Space : O(Z * O)


def p1():
    # Problem 1 : POTD Leetcode 3129. Find All Possible Stable Binary Arrays I - https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/description/?envType=daily-question&envId=2026-03-09

    testcase = [
        [1, 1, 2, 2],
        [1, 2, 1, 1],
        [3, 3, 2, 14],
        [20, 15, 75, 247943139],
    ]

    for line in testcase:
        [zero, one, limit, expected] = line
        s1 = Solution1()
        result = s1.numberOfStableArrays(zero, one, limit)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def largestSwap(self, s: str):
        # code here
        # find largest element on right for each element
        # from index 0 try to swap it with element on right
        # if right element is greater

        sarr = list(s)

        N = len(sarr)

        right_max = [N - 1] * N
        right_max[N - 1] = N - 1
        for i in range(N - 2, -1, -1):
            right_max[i] = i if sarr[i] > sarr[right_max[i + 1]] else right_max[i + 1]

        for i in range(0, N):
            if sarr[i] < sarr[right_max[i]]:
                [sarr[i], sarr[right_max[i]]] = [sarr[right_max[i]], sarr[i]]
                break

        return "".join(sarr)

        # Complexity analysis
        # Time : O(2N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Largest number in one swap - https://www.geeksforgeeks.org/problems/largest-number-in-one-swap1520/1

    testcase = [
        ["768", "867"],
        ["333", "333"],
        ["3033", "3330"],
    ]

    for line in testcase:
        [s, expected] = line
        s2 = Solution2()
        result = s2.largestSwap(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 9 of March 2026

    p1()

    p2()
