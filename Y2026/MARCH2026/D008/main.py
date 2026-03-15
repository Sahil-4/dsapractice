from typing import List


class Solution1:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # we just have to make one char different

        N = len(nums)

        output = [""] * N

        for i in range(N):
            output[i] = "1" if nums[i][i] == "0" else "0"

        return "".join(output)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1980. Find Unique Binary String - https://leetcode.com/problems/find-unique-binary-string/description/?envType=daily-question&envId=2026-03-08

    testcase = [
        [["01", "10"], "11"],
        [["00", "01"], "10"],
        [["111", "011", "001"], "000"],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.findDifferentBinaryString(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def pythagoreanTriplet(self, arr):
        # code here

        N = len(arr)

        if N < 3:
            return False

        T = max(arr)

        count = [0] * (T + 1)
        for el in arr:
            count[el] += 1

        for a in range(1, T + 1):
            for b in range(a + 1, T + 1):
                if count[a] < 1 or count[b] < 1:
                    continue

                asquare = a * a
                bsquare = b * b

                csquare = asquare + bsquare

                c = int(csquare**0.5)

                if c * c == csquare and c <= T and count[c] > 0:
                    return True

        return False

        # Complexity analysis
        # Time : O(N)
        # Space : O(T)


def p2():
    # Problem 2 : POTD Geeksforgeeks Pythagorean Triplet - https://www.geeksforgeeks.org/problems/pythagorean-triplet3018/1

    testcase = [
        [[3, 2, 4, 6, 5], True],
        [[3, 8, 5], False],
        [[1, 1, 1], False],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.pythagoreanTriplet(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 8 of March 2026

    p1()

    p2()
