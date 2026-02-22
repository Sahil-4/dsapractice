class Solution1:
    def binaryGap(self, n: int) -> int:
        lgap = 0

        prev = -1
        curr = 0
        while n > 0:
            if n & 1:
                lgap = max(lgap, curr - prev) if prev != -1 else lgap
                prev = curr

            curr += 1
            n = n >> 1

        return lgap

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 868. Binary Gap - https://leetcode.com/problems/binary-gap/description/?envType=daily-question&envId=2026-02-22

    testcase = [
        [22, 2],
        [8, 0],
        [5, 2],
    ]

    for line in testcase:
        [n, expected] = line
        s1 = Solution1()
        result = s1.binaryGap(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def subarrayXor(self, arr, k):
        # code here
        count = 0

        xr = 0
        mp = dict()

        mp[xr] = 1

        for el in arr:
            xr = xr ^ el
            x = xr ^ k
            count += mp[x] if x in mp else 0
            if xr not in mp:
                mp[xr] = 0
            mp[xr] += 1

        return count

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count Subarrays with given XOR - https://www.geeksforgeeks.org/problems/count-subarray-with-given-xor/1

    testcase = [
        [[4, 2, 2, 6, 4], 6, 4],
        [[5, 6, 7, 8, 9], 5, 2],
        [[1, 1, 1, 1], 0, 4],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.subarrayXor(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 22 of February 2026

    p1()

    p2()
