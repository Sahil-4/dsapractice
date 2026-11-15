class Solution1:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 1000000007

        N = len(arr)

        count = 0

        odd = 0
        even = 1

        prefix_sum = 0

        for i in range(N):
            prefix_sum += arr[i]

            if prefix_sum & 1:
                count = (count + even) % MOD
                odd += 1
            else:
                count = (count + odd) % MOD
                even += 1

        return count

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1524. Number of Sub-arrays With Odd Sum - https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/?envType=daily-question&envId=2026-11-15

    testcase = [
        [[1, 3, 5], 4],
        [[2, 4, 6], 0],
        [[1, 2, 3, 4, 5, 6, 7], 16],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.numOfSubarrays(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def subsequenceSum(self, s: str) -> int:
        """code here"""
        MOD = 1000000007
        N = len(s)

        occurrences = pow(2, N - 1, MOD)

        _sum = 0

        for i in range(N):
            _sum = (_sum + int(s[i]) * occurrences) % MOD

        return _sum

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Sum of All Digit Subsequences - https://www.geeksforgeeks.org/problems/sum-of-all-sub-sequences-of-a-number3437/1

    testcase = [
        ["123", 24],
        ["405", 36],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.subsequenceSum(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 217. Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[1, 2, 3, 1], True],
        [[1, 2, 3, 4], False],
        [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.containsDuplicate(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 15 of November 2026

    p1()

    p2()

    p3()
