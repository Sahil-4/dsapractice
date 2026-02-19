class Solution1:
    def countBinarySubstrings(self, s: str) -> int:
        N = len(s)

        result = 0

        prev = 0
        curr = 1
        for i in range(1, N):
            if s[i - 1] != s[i]:
                result += min(prev, curr)
                prev = curr
                curr = 1
            else:
                curr += 1

        return result + min(prev, curr)

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 696. Count Binary Substrings - https://leetcode.com/problems/count-binary-substrings/description/?envType=daily-question&envId=2026-02-19

    testcase = [
        ["00110011", 6],
        ["10101", 4],
    ]

    for line in testcase:
        [s, expected] = line
        s1 = Solution1()
        result = s1.countBinarySubstrings(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def missingRange(self, arr, low, high):
        # code here
        # put all array elements into a set
        # iterate from low to high
        # if number not in set
        # add to result
        # else skip

        present = set(arr)
        missing = []

        for num in range(low, high + 1):
            if num not in present:
                missing.append(num)

        return missing

        # Complexity analysis
        # Time : O(N + D)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Missing Element in Range - https://www.geeksforgeeks.org/problems/missing-element-in-range/1

    testcase = [
        [[10, 12, 11, 15], 10, 15, [13, 14]],
        [[1, 4, 11, 51, 15], 50, 55, [50, 52, 53, 54, 55]],
    ]

    for line in testcase:
        [arr, low, high, expected] = line
        s2 = Solution2()
        result = s2.missingRange(arr, low, high)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 19 of February 2026

    p1()

    p2()
