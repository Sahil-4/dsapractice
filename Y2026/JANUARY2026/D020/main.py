from typing import List


class Solution1:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        """
        ans[i] or (ans[i] + 1) == nums[i]
        nums[i] = ans[i] or (ans[i] + 1)
        by observation
        if x = (101001)
        (x+1) = (101010)
        x or (x+1) ie. 101001 or 101010
        101001 or 101010 = 101011
        update last zero bit to one
        reverse engineering
        on (101011) iterate from least significant bit
        find first zero bit and update bit before this to zero
        this will get us x
        now from x we can get (x+1)
        """

        result = []

        for num in nums:
            if num == 2:
                result.append(-1)
                continue

            found = False
            for j in range(1, 32):
                if (num & (1 << j)) > 0:
                    continue

                result.append(num ^ (1 << (j - 1)))
                found = True
                break

            if not found:
                result.append(-1)

        return result

        # Complexity analysis
        # Time : O(N * 32)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3314. Construct the Minimum Bitwise Array I - https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/description/?envType=daily-question&envId=2026-01-20

    testcase = [
        [[2, 3, 5, 7], [-1, 1, 4, 3]],
        [[11, 13, 31], [9, 12, 15]],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.minBitwiseArray(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def __init__(self):
        # primary stack to store output of  read
        self.primary = []
        # after undo characters will be stores in this for redo
        self.undone = []
        self.flag = False

    def append(self, x):
        # append x into document
        self.primary.append(x)
        if self.flag:
            self.undone.clear()
            self.flag = False

    def undo(self):
        # undo last change
        if len(self.primary) == 0:
            return
        self.undone.append(self.primary.pop())
        self.flag = True

    def redo(self):
        # redo changes
        if len(self.undone) == 0:
            return
        self.primary.append(self.undone.pop())

    def read(self):
        # read the document
        return "".join(self.primary)

    # Complexity analysis
    # Time : O(2N)
    # Space : O(N)


def p2():
    # Problem 2 : Implement UNDO & REDO

    testcases = [
        ([[1, "A"], [1, "B"], [1, "C"], [2], [4], [3], [4]], ["AB", "ABC"]),
        ([[1, "D"], [2], [4]], [""]),
    ]

    for arr, expected_output in testcases:
        s2 = Solution2()
        result = []

        for q in arr:
            if q[0] == 1:
                s2.append(q[1])
            elif q[0] == 2:
                s2.undo()
            elif q[0] == 3:
                s2.redo()
            elif q[0] == 4:
                result.append(s2.read())

        assert result == expected_output, f"Expected {expected_output}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 20 of January 2026

    p1()

    p2()
