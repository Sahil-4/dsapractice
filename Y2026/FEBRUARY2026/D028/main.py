class Solution1:
    def concatenatedBinary(self, n: int) -> int:
        MODO = 1000000007

        result = 0
        digits = 0

        for num in range(1, n + 1):
            if (num & (num - 1)) == 0:
                digits += 1

            result = (((result << digits) % MODO) + num) % MODO

        return result

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1680. Concatenation of Consecutive Binary Numbers - https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/description/?envType=daily-question&envId=2026-02-28

    testcase = [
        [1, 1],
        [3, 27],
        [12, 505379714],
    ]

    for line in testcase:
        [n, expected] = line
        s1 = Solution1()
        result = s1.concatenatedBinary(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findClosestPair(self, arr1, arr2, x):
        # code here
        # pick an element from arr1 say e
        # calculate f = x - e
        # find el2 <= f and el2 >= f
        # pick pair whichever gives closest sum
        # better approach will be to use two pointers
        # l starts from 0 go till n-1 for arr1
        # r starts from m-1 and go till 0 for arr2
        # shift pointer on the basis of diff compared to x

        print(arr1)
        print(arr2)

        N = len(arr1)
        M = len(arr2)

        l = 0
        r = M - 1

        diff = float("inf")
        closest_pair = [-1, -1]

        while l < N and r > -1:
            sum_val = arr1[l] + arr2[r]
            cdiff = abs(x - sum_val)

            if cdiff < diff:
                diff = cdiff
                closest_pair = [arr1[l], arr2[r]]

            if sum_val > x:
                r -= 1
            else:
                l += 1

        return closest_pair

        # Complexity analysis
        # Time : O(N + M)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Find the closest pair from two arrays - https://www.geeksforgeeks.org/problems/find-the-closest-pair-from-two-arrays4215/1

    testcase = [
        [
            [1, 4, 5, 7],
            [10, 20, 30, 40],
            32,
            [1, 30],
        ],
        [
            [1, 4, 5, 7],
            [10, 20, 30, 40],
            50,
            [7, 40],
        ],
    ]

    for line in testcase:
        [arr1, arr2, x, expected] = line
        s2 = Solution2()
        result = s2.findClosestPair(arr1, arr2, x)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 28 of February 2026

    p1()

    p2()
