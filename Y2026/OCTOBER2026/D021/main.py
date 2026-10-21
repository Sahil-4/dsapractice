class Solution1:
    def minOperations(self, s: str) -> int:
        # if string is already sorted: return 0
        # if length is 2: return -1 (proper substring is length 1, so no swap is possible)
        # 1 operation works:
        # if first character is the smallest:
        # sort everything except the first character -> return 1
        # if last character is the largest:
        # sort everything except the last character -> return 1
        # 3 operations are required:
        # if largest character is at the start and smallest character is at the end:
        # (and neither appears anywhere in the middle)
        # op 1: sort from start to second-to-last -> moves largest near the end
        # op 2: sort from second character to end  -> places largest at end, smallest near start
        # op 3: sort from start to second-to-last -> places smallest at start, string is sorted
        # return 3
        # otherwise:
        # 2 operations are always enough -> return 2

        N = len(s)

        # already sorted
        if all(s[i] <= s[i + 1] for i in range(N - 1)):
            return 0

        # impossible if length is 2 and unsorted
        if N == 2:
            return -1

        min_char = min(s)
        max_char = max(s)

        # can be sorted in 1 operation
        if s[0] == min_char or s[-1] == max_char:
            return 1

        # requires 3 operations
        # if min is strictly at the end AND max is strictly at the start
        if (
            s[0] == max_char
            and s[-1] == min_char
            and min_char not in s[:-1]
            and max_char not in s[1:]
        ):
            return 3

        # all other cases
        # can be solved in 2 operations
        return 2

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3863. Minimum Operations to Sort a String - https://leetcode.com/problems/minimum-operations-to-sort-a-string/description/?envType=daily-question&envId=2026-10-21

    testcase = [
        ["dog", 1],
        ["card", 2],
        ["gf", -1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minOperations(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minSubarraySum(self, arr: list[int]) -> int:
        # At each element x, you have two choices
        # Extend the previous subarray: current_min + x
        # Start a fresh subarray at the current element: x

        # init with the first element
        current_min = arr[0]
        result = arr[0]

        # iterate through the rest of the array
        for x in arr[1:]:
            current_min = min(x, current_min + x)
            result = min(result, current_min)

        return result

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Sum Subarray - https://www.geeksforgeeks.org/problems/smallest-sum-contiguous-subarray/1

    testcase = [
        [[3, -4, 2, -3, -1, 7, -5], -6],
        [[4, -6, 3, -2, 5, -8, 2], -8],
        [[2, 6, 8, 1, 4], 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minSubarraySum(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def countSubstrings(self, s: str) -> int:
        N = len(s)

        total_palindromes = 0

        def expand_and_count(left: int, right: int) -> int:
            count = 0

            while left >= 0 and right < N and s[left] == s[right]:
                count += 1

                left -= 1
                right += 1

            return count

        for i in range(N):
            # odd length palindromes (center at i)
            total_palindromes += expand_and_count(i, i)
            # even length palindromes (center between i and i + 1)
            total_palindromes += expand_and_count(i, i + 1)

        return total_palindromes

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 647. Palindromic Substrings - https://leetcode.com/problems/palindromic-substrings/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["abc", 3],
        ["aaa", 6],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.countSubstrings(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 21 of October 2026

    p1()

    p2()

    p3()
