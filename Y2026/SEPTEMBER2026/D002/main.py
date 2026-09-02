class Solution1:
    def uniformArray(self, nums1: list[int]) -> bool:
        # N = len(nums1)

        # count of even, odd
        # even_count, odd_count = 0, 0
        # for num in nums1:
        #     even_count += 1 if not (num & 1) else 0
        #     odd_count += 1 if (num & 1) else 0

        # either all even or all odds - return as it is
        # if even_count == N or odd_count == N:
        #     return True

        # how to make all odds - subtract one odd from all evens; even - odd = odd

        # how to make all even - subtract one even from all odds; odd - odd = even

        # hence its always possible to construct an answer

        return True

        # Complexity analysis
        # Time: O(1)
        # Space: O(1)


def p1():
    # Problem 1 : POTD Leetcode 3875. Construct Uniform Parity Array I - https://leetcode.com/problems/construct-uniform-parity-array-i/description/?envType=daily-question&envId=2026-09-02

    testcase = [
        [[2, 3], True],
        [[4, 6], True],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.uniformArray(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def solve(self, n: int, s: str) -> int:
        # code here

        N = len(s)

        free = n
        occupied_by = set()
        rejected = set()

        count = 0

        free -= 1
        occupied_by.add(s[0])

        for i in range(1, N):
            c = s[i]

            if c in rejected:
                rejected.remove(c)
                continue

            if c in occupied_by:
                occupied_by.remove(c)
                free += 1
            elif free > 0:
                occupied_by.add(c)
                free -= 1
            else:
                rejected.add(c)
                count += 1

        return count

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Unoccupied Computers - https://www.geeksforgeeks.org/problems/unoccupied-computers-1646661078/1

    testcase = [
        [3, "GACCBDDBAGEE", 1],
        [1, "ABCBAC", 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.solve(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        llen = 0

        seen = set()
        l_index = 0

        for r_index, character in enumerate(s):
            while character in seen:
                seen.remove(s[l_index])
                l_index += 1

            llen = max(llen, r_index - l_index + 1)
            seen.add(character)

        return llen

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 3. Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["abcabcbb", 3],
        ["bbbbb", 1],
        ["pwwkew", 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.lengthOfLongestSubstring(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


class Solution4:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # median = middle value after sorting (odd array length)
        # sum of two middle values // 2 (even array length)

        M = len(nums1)
        N = len(nums2)

        # obstacle
        nums1.append(1000000000)
        nums2.append(1000000000)

        increment_needed = (M + N - 1) // 2

        p1 = 0
        p2 = 0

        while increment_needed > 0:
            if nums1[p1] <= nums2[p2]:
                p1 += 1
            else:
                p2 += 1

            increment_needed -= 1

        # odd elements case - will reuse in even elements case as well
        median = min(nums1[p1], nums2[p2]) * 1.0

        # even elements case
        if not ((M + N) & 1):
            if nums1[p1] <= nums2[p2]:
                p1 += 1
            else:
                p2 += 1

            # ...,a,b,...
            median = (median + min(nums1[p1], nums2[p2])) / 2.0

        # remove obstacles added
        nums1.pop()
        nums2.pop()

        return median

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(1)


def p4():
    # Problem 4 : NC150 Leetcode 4. Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[1, 3], [2], 2.00000],
        [[1, 2], [3, 4], 2.50000],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s4 = Solution4()
        result = s4.findMedianSortedArrays(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P4): result={result}")


class Solution5:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)

        pi = 0
        llen = 1

        for i in range(N):
            # odd length s[i] in middle
            l, r = i, i
            while l >= 0 and r < N and s[l] == s[r]:
                if llen < r - l + 1:
                    pi = l
                    llen = r - l + 1

                l -= 1
                r += 1

            # even length s[i],s[i+1] in middle
            l, r = i, i + 1
            while l >= 0 and r < N and s[l] == s[r]:
                if llen < r - l + 1:
                    pi = l
                    llen = r - l + 1

                l -= 1
                r += 1

        return s[pi : pi + llen]

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(1)


def p5():
    # Problem 5 : NC150 Leetcode 5. Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["babad", "bab"],
        ["cbbd", "bb"],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s5 = Solution5()
        result = s5.longestPalindrome(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P5): result={result}")


if __name__ == "__main__":
    # Day 2 of September 2026

    p1()

    p2()

    p3()

    p4()

    p5()
