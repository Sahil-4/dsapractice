from functools import lru_cache


class Solution1:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # D = 2
        # start by index 0
        # go till N - 1
        # if s1[i] == s2[i]: continue
        # else
        # elif i >= N - D: return false
        # else swap any (s1[i], s1[i + D]) or (s2[i], s2[i + D])

        D = 2
        N = 4

        s1_arr = list(s1)
        s2_arr = list(s2)

        for i in range(N):
            # already equal
            if s1_arr[i] == s2_arr[i]:
                continue

            # make equal
            if i + D < N and (
                (s1_arr[i] == s2_arr[i + D] and s1_arr[i + D] == s2_arr[i])
            ):
                s1_arr[i], s1_arr[i + D] = s1_arr[i + D], s1_arr[i]
            else:
                # cant make equal
                return False

        return True

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2839. Check if Strings Can be Made Equal With Operations I - https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/description/?envType=daily-question&envId=2026-03-29

    testcase = [
        ["abcd", "cdab", True],
        ["abcd", "dacb", False],
    ]

    for line in testcase:
        [str1, str2, expected] = line
        s1 = Solution1()
        result = s1.canBeEqual(str1, str2)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def find_subsets_sum(self, arr, psum):
        N = len(arr)

        @lru_cache(maxsize=None)
        def recursion(index, csum):
            # base case
            if index == 0:
                count = 0
                if csum == psum:
                    count += 1
                if csum + arr[0] == psum:
                    count += 1
                return count

            # skip
            not_pick = recursion(index - 1, csum)

            # take
            pick = 0
            if csum + arr[index] <= psum:
                pick = recursion(index - 1, csum + arr[index])

            return pick + not_pick

            # Complexity analysis
            # Time : O(N * psum)
            # Space : O(N * psum) + O(N stack)

        return recursion(N - 1, 0)

    def countPartitions(self, arr, diff):
        # code here
        tsum = sum(arr)

        if tsum - diff < 0 or ((tsum - diff) & 1):
            return 0

        psum = (tsum - diff) // 2

        # now find number of subsets having sum exactly psum
        return self.find_subsets_sum(arr, psum)


def p2():
    # Problem 2 : POTD Geeksforgeeks Partitions with Given Difference - https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1

    testcase = [
        [[5, 2, 6, 4], 3, 1],
        [[1, 1, 1, 1], 0, 6],
        [[3, 2, 7, 1], 4, 0],
    ]

    for line in testcase:
        [arr, diff, expected] = line
        s2 = Solution2()
        result = s2.countPartitions(arr, diff)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 29 of March 2026

    p1()

    p2()
