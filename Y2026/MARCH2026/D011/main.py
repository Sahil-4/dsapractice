from typing import List, Callable


class Solution1:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        not_n = ~n
        mask = 0

        while n != 0:
            mask = mask << 1
            mask = mask | 1
            n = n >> 1

        return not_n & mask

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1009. Complement of Base 10 Integer - https://leetcode.com/problems/complement-of-base-10-integer/description/?envType=daily-question&envId=2026-03-11

    testcase = [
        [5, 2],
        [7, 0],
        [10, 5],
    ]

    for line in testcase:
        [n, expected] = line
        s1 = Solution1()
        result = s1.bitwiseComplement(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def sumSubMins(self, arr: List[int]):
        # code here
        # arr = [1, 2, 3, 4]
        # sml = [-1, 0, 1, 2]
        # smr = [N, N, N, N]
        # sum += (i - l) * (r - i)
        # subarray using el 1 = (0 + 1) * (4 - 0) = 4
        # sum contribution = 4 * 1

        N = len(arr)

        def nextSmall(
            initial: int,
            start: int,
            end: int,
            increment: int,
            func: Callable[[int, int], int],
        ) -> List[int]:
            out = [initial] * N
            stack = []

            i = start
            while i != end:
                while stack and func(arr[stack[-1]], arr[i]):
                    stack.pop()

                out[i] = stack[-1] if stack else initial

                stack.append(i)

                i += increment

            return out

        sml = nextSmall(-1, 0, N, +1, lambda a, b: a >= b)
        smr = nextSmall(N, N - 1, -1, -1, lambda a, b: a > b)

        tsum = 0

        for i in range(0, N):
            count = (i - sml[i]) * (smr[i] - i)
            contribution = count * arr[i]
            tsum += contribution

        return tsum

        # Complexity analysis
        # Time : O(3N)
        # Space : O(2N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Sum of subarray minimums - https://www.geeksforgeeks.org/problems/sum-of-subarray-minimum/1

    testcase = [
        [[10, 20], 40],
        [[1, 2, 3, 4], 20],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.sumSubMins(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 11 of March 2026

    p1()

    p2()
