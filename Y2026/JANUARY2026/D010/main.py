from functools import lru_cache


class Solution1:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # LCS problem
        # HINT: delete characters which are not common
        # use LCS algorithm (modified)
        # here we dont just have to find LCS we have to find unmatching characters
        # on deleting them we get least ASCII sum and both strings becomes equal
        # start traversing both string s1i, s2i
        # if s1[s1i] == s2[s2i] we dont need to delete this
        # continue to (s1i + 1, s2i + 1)
        # else we can delete either s1[s1i], s2[s2i]
        # we will delete whichever gives minimum ASCII sum

        s1N = len(s1)
        s2N = len(s2)

        @lru_cache(None)
        def recursion_memoized(s1i: int, s2i: int) -> int:
            if s1i == s1N:
                sum = 0
                for i in range(s2i, s2N):
                    sum += ord(s2[i])
                return sum
            if s2i == s2N:
                sum = 0
                for i in range(s1i, s1N):
                    sum += ord(s1[i])
                return sum

            if s1[s1i] == s2[s2i]:
                return recursion_memoized(s1i + 1, s2i + 1)
            else:
                case1 = ord(s1[s1i]) + recursion_memoized(s1i + 1, s2i)  # delete s1i
                case2 = ord(s2[s2i]) + recursion_memoized(s1i, s2i + 1)  # delete s2i
                return min(case1, case2)

            # Complexity analysis
            # Time : O(2*N*M)
            # Space : O(N*M) + O(N+M)

        def tabulation():
            dp_states = [[0] * (s2N + 1) for _ in range(s1N + 1)]

            # base cases
            for i in range(s1N - 1, -1, -1):
                dp_states[i][s2N] = dp_states[i + 1][s2N] + ord(s1[i])

            for j in range(s2N - 1, -1, -1):
                dp_states[s1N][j] = dp_states[s1N][j + 1] + ord(s2[j])

            for s1i in range(s1N - 1, -1, -1):
                for s2i in range(s2N - 1, -1, -1):
                    if s1[s1i] == s2[s2i]:
                        dp_states[s1i][s2i] = dp_states[s1i + 1][s2i + 1]
                    else:
                        case1 = ord(s1[s1i]) + dp_states[s1i + 1][s2i]  # delete s1i
                        case2 = ord(s2[s2i]) + dp_states[s1i][s2i + 1]  # delete s2i
                        dp_states[s1i][s2i] = min(case1, case2)

            return dp_states[0][0]

            # Complexity analysis
            # Time : O(N*M)
            # Space : O(N*M)

        # return recursion_memoized(0, 0)
        return tabulation()


def p1():
    # Problem 1 : POTD Leetcode 712. Minimum ASCII Delete Sum for Two Strings - https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/?envType=daily-question&envId=2026-01-10

    testcase = [
        ["sea", "eat", 231],
        ["delete", "leet", 403],
    ]

    for line in testcase:
        [s1, s2, expected] = line
        s = Solution1()
        result = s.minimumDeleteSum(s1, s2)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def at_most(self, s, k):
        subarrays_count = 0

        N = len(s)

        frequency = dict()
        distincts = 0

        left = 0
        for right in range(N):
            if s[right] not in frequency or frequency[s[right]] == 0:
                frequency[s[right]] = 0
                distincts += 1

            frequency[s[right]] += 1

            while distincts > k:
                frequency[s[left]] -= 1
                if frequency[s[left]] == 0:
                    distincts -= 1
                left += 1

            subarrays_count += right - left + 1

        return subarrays_count

    def countSubstr(self, s, k):
        # Code here
        # find count of subarrays with at most k distinct characters say count_k
        # then find count of subarrays with at most (k - 1) distinct characters say count_k_1
        # answer would be count_k - count_k_1
        # i.e. count of subarrays with exactly k distinct characters

        return self.at_most(s, k) - self.at_most(s, k - 1)

        # Complexity analysis
        # Time : O(2N)
        # Space : O(26)


def p2():
    # Problem 2 : POTD Geeksforgeeks Substrings with K Distinct - https://www.geeksforgeeks.org/problems/count-number-of-substrings4528/1

    testcase = [
        ["abc", 2, 2],
        ["aba", 2, 3],
        ["aa", 1, 3],
    ]

    for line in testcase:
        [s, k, expected] = line
        s2 = Solution2()
        result = s2.countSubstr(s, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 10 of January 2026

    p1()

    p2()
