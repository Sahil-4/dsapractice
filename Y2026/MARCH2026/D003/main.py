import math


class Solution1:
    def findKthBit(self, n: int, k: int) -> str:
        # si = S(i-1) + "1" + reverse(invert(S(i-1)))
        # s1 = '0'
        # s2 = '0' + '1' + '1'
        # s2 = '011'
        # s3 = '011' + '1' + '001'
        # s3 = '0111001'

        if n == 1:
            return "0"

        len = (1 << n) - 1
        h = math.ceil(len / 2)

        if k < h:
            return self.findKthBit(n - 1, k)
        elif k == h:
            return "1"
        else:
            return str(int(not int(self.findKthBit(n - 1, len - (k - 1)))))

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1545. Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/?envType=daily-question&envId=2026-03-03

    testcase = [
        [3, 1, "0"],
        [4, 11, "1"],
        [4, 12, "0"],
    ]

    for line in testcase:
        [n, k, expected] = line
        s1 = Solution1()
        result = s1.findKthBit(n, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def totalElements(self, arr):
        # Code here

        K = 2
        N = len(arr)

        llen = 0

        mp = dict()
        distinct = 0

        l = 0
        for r in range(N):
            if arr[r] not in mp or mp[arr[r]] == 0:
                mp[arr[r]] = 0
                distinct += 1

            mp[arr[r]] += 1

            while distinct > K:
                mp[arr[l]] -= 1

                if mp[arr[l]] == 0:
                    distinct -= 1

                l += 1

            llen = max(llen, r - l + 1)

        return llen

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Longest subarray with Atmost two distinct integers - https://www.geeksforgeeks.org/problems/fruit-into-baskets-1663137462/1

    testcase = [
        [[2, 1, 2], 3],
        [[3, 1, 2, 2, 2, 2], 5],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.totalElements(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 3 of March 2026

    p1()

    p2()
