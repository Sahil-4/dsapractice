from bisect import bisect_right


class Solution1:
    def numberOfSets(self, N: int, K: int) -> int:
        MOD = 1000000007

        DP = [[0 for _ in range(N + 1)] for _ in range(K + 1)]

        # base case if k = 0: return 1
        DP[0] = [1 for _ in range(N)]

        # base case if i == 0: return 0
        # already handled by init

        for k in range(1, K + 1):

            _suffix_sum = [0] * (N + 1)
            for j in range(N - 1, -1, -1):
                _suffix_sum[j] = (_suffix_sum[j + 1] + DP[k - 1][j]) % MOD

            for i in range(N - 1, -1, -1):

                # skip
                skip = DP[k][i + 1] % MOD

                # take
                take = _suffix_sum[i + 1] % MOD

                DP[k][i] = (skip + take) % MOD

        return DP[K][0]

        # Complexity analysis
        # Time : (K * N * N)
        # Space : O(K * N * N)


def p1():
    # Problem 1 : POTD Leetcode 1621. Number of Sets of K Non-Overlapping Line Segments - https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/description/?envType=daily-question&envId=2026-09-16

    testcase = [
        [4, 2, 5],
        [3, 1, 3],
        [30, 7, 796297179],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.numberOfSets(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def dominantPairs(self, arr: list[int]) -> int:
        # code here
        N = len(arr)
        N2 = N // 2

        RM = 5

        left_half = sorted(arr[:N2])
        right_half = sorted(arr[N2:])

        for i in range(N2):
            right_half[i] *= RM

        count = 0

        for i in range(N2):
            num = left_half[i]

            # find last index of num in right_half
            last_index = bisect_right(right_half, num)

            count += last_index

        return count

        # Complexity analysis
        # Time : O(N2 * Log(N2))
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Dominant Pairs - https://www.geeksforgeeks.org/problems/dominant-pairs/1

    testcase = [
        [[10, 2, 2, 1], 2],
        [[10, 8, 2, 1, 1, 2], 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.dominantPairs(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def jump(self, nums: list[int]) -> int:
        N = len(nums)

        DP = [N] * N
        DP[N - 1] = 0

        for index in range(N - 2, -1, -1):
            jumps = N

            for jump_length in range(1, nums[index] + 1):
                next_index = index + jump_length
                _jumps = 1 + DP[next_index] if next_index < N else N
                jumps = min(jumps, _jumps)

            DP[index] = jumps

        return DP[0]

        # Complexity analysis
        # Time : O(N * MAX(nums))
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 45. Jump Game II - https://leetcode.com/problems/jump-game-ii/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[2, 3, 1, 1, 4], 2],
        [[2, 3, 0, 1, 4], 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.jump(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def permute(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)

        permutations = []

        def helper(idx: int, perm: list[int]):
            if idx == N:
                permutations.append(list(perm))
                return

            for swap_idx in range(idx, N):
                perm[idx], perm[swap_idx] = perm[swap_idx], perm[idx]

                helper(idx + 1, perm)

                perm[idx], perm[swap_idx] = perm[swap_idx], perm[idx]

        helper(0, list(nums))

        return permutations

        # Complexity analysis
        # Time : O(N ^ N)
        # Space : O(N) stack + O(N) perm array


def p4():
    # Problem 4 : NC150 Leetcode 46. Permutations - https://leetcode.com/problems/permutations/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]],
        [[0, 1], [[0, 1], [1, 0]]],
        [[1], [[1]]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.permute(*inputs)
        result.sort()
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4: result={result}")


if __name__ == "__main__":
    # Day 16 of September 2026

    p1()

    p2()

    p3()

    p4()
