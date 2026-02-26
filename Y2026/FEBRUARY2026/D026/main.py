class Solution1:
    def numSteps(self, s: str) -> int:
        # if s represents even
        # we remove last bit (lsb)
        # else
        # we update first 0 bit to 1 bit, if there are no 0 bit then add 1 at msb
        # starting from lsb
        # if s contains 1 at lsb its odd
        # else its even
        # we have to perform this operation until we are left with a single bit that is 1

        steps = 0
        carry = 0

        # right to left (ignore the first bit)
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i])

            if bit + carry == 1:
                # Odd - add 1 (creates carry) + divide by 2
                steps += 2
                carry = 1
            else:
                # Even - just divide by 2
                steps += 1
                # carry stays the same if 0
                # stays 1 if bit+carry was 2

        # if carry is still 1 at the end,
        # we need one final step (111 -> 1000 -> ... )
        return steps + carry

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1404. Number of Steps to Reduce a Number in Binary Representation to One - https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/?envType=daily-question&envId=2026-02-26

    testcase = [
        ["1101", 6],
        ["10", 1],
        ["1", 0],
    ]

    for line in testcase:
        [s, expected] = line
        s1 = Solution1()
        result = s1.numSteps(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def areIsomorphic(self, str1: str, str2: str) -> bool:
        # code here
        s1_mapped = dict()
        s2_mapped = dict()

        N = len(str1)

        for i in range(N):
            ch1 = str1[i]
            ch2 = str2[i]

            if ch1 not in s1_mapped:
                s1_mapped[ch1] = ch2
            if ch2 not in s2_mapped:
                s2_mapped[ch2] = ch1

            if s1_mapped[ch1] != ch2:
                return False
            if s2_mapped[ch2] != ch1:
                return False

        return True

        # Complexity analysis
        # Time : O(N)
        # Space : O(2N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Isomorphic Strings - https://www.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1

    testcase = [
        ["aab", "xxy", True],
        ["aab", "xyz", False],
        ["abc", "xxz", False],
    ]

    for line in testcase:
        [str1, str2, expected] = line
        s2 = Solution2()
        result = s2.areIsomorphic(str1, str2)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 26 of February 2026

    p1()

    p2()
