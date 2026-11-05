from bisect import bisect_left


class Solution1:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        distance_value = 0

        arr2.sort()

        for el in arr1:
            _min = el - d
            _max = el + d

            # find _min in arr2
            # if element found is >= _min and <= _max
            # discard this element

            # find where _min would be inserted in arr2
            idx = bisect_left(arr2, _min)

            # check if the element at this index falls within
            # forbidden [_min, _max] range
            if idx < len(arr2) and arr2[idx] <= _max:
                # found an element too close,
                # so this num fails the test
                continue

            distance_value += 1

        return distance_value

        # Complexity analysis
        # Time : O(M * Log(M)) + O(N * Log(M))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1385. Find the Distance Value Between Two Arrays - https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/?envType=daily-question&envId=2026-11-05

    testcase = [
        [[4, 5, 8], [10, 9, 1, 8], 2, 2],
        [[1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3, 2],
        [[2, 1, 100, 3], [-5, -2, 10, -3, 7], 6, 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.findTheDistanceValue(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def getMinimumDays(self, s: str, p: list[int]) -> int:
        # code here
        N = len(s)

        max_min_days = 0

        days_2_pi_mapping = dict()
        for index, day in enumerate(p):
            days_2_pi_mapping[day] = index + 1  # days = 1 based

        for i in range(N - 1):
            # adjacent characters equal
            if s[i] == s[i + 1]:
                di = days_2_pi_mapping[i]
                dj = days_2_pi_mapping[i + 1]
                # have to pass any one day, will pass lower day

                max_min_days = max(max_min_days, min(di, dj))

        return max_min_days

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Days - https://www.geeksforgeeks.org/problems/minimum-days--170646/1

    testcase = [
        ["aabb", [2, 1, 3, 0], 2],
        ["abca", [3, 0, 2, 1], 0],
        ["aaaa", [2, 1, 3, 0], 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.getMinimumDays(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def hammingWeight(self, n: int) -> int:
        weight = 0

        for i in range(32):
            weight += (n >> i) & 1

        return weight

        # Complexity analysis
        # Time : O(1)
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 191. Number of 1 Bits - https://leetcode.com/problems/number-of-1-bits/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [11, 3],
        [128, 1],
        [2147483645, 30],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.hammingWeight(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)

        dp = [0] * (N + 1)

        # base cases
        dp[N] = 0
        dp[N - 1] = nums[N - 1]
        dp[N - 2] = nums[N - 2]

        # remain cases
        for i in range(N - 2, -1, -1):
            # take ith num and then any path starting after index i+1
            dp[i] = nums[i] + max(dp[i + 2 :])

        return max(dp)

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(N)


def p4():
    # Problem 4 : NC150 Leetcode 198. House Robber - https://leetcode.com/problems/house-robber/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[1, 2, 3, 1], 4],
        [[2, 7, 9, 3, 1], 12],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.rob(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


if __name__ == "__main__":
    # Day 5 of November 2026

    p1()

    p2()

    p3()

    p4()
