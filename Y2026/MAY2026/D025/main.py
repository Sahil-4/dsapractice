class Solution1:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        N = len(s)

        dp = [0] * N
        prefix_sum = [0] * N

        dp[0] = 1

        for i in range(minJump):
            prefix_sum[i] = 1

        for i in range(minJump, N):
            left, right = i - maxJump, i - minJump

            if s[i] == "0":
                total = prefix_sum[right] - (0 if left <= 0 else prefix_sum[left - 1])
                dp[i] = int(total != 0)

            prefix_sum[i] = prefix_sum[i - 1] + dp[i]

        return bool(dp[N - 1])

        # Complexity Analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1871. Jump Game VII - https://leetcode.com/problems/jump-game-vii/description/?envType=daily-question&envId=2026-05-25

    testcase = [
        ["011010", 2, 3, True],
        ["01101110", 2, 3, False],
    ]

    for line in testcase:
        [s, minJump, maxJump, expected] = line
        s1 = Solution1()
        result = s1.canReach(s, minJump, maxJump)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def checkElements(self, start: int, end: int, arr: list) -> bool:
        # code here

        N = len(arr)

        # base
        if N < (end - start + 1):
            return False

        rlen = end - start

        # mark
        for i in range(N):
            val = abs(arr[i])

            if start <= val <= end:
                hash_index = val - start

                if hash_index < N and arr[hash_index] > 0:
                    arr[hash_index] = -arr[hash_index]

        # verify
        for i in range(min(rlen + 1, N)):
            if arr[i] > 0:
                return False

        return True

        # Complexity Analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Elements in the Range - https://www.geeksforgeeks.org/problems/elements-in-the-range2834/1

    testcase = [
        [2, 5, [1, 4, 5, 2, 7, 8, 3], True],
        [2, 6, [1, 4, 5, 2, 7, 8, 3], False],
    ]

    for line in testcase:
        [start, end, arr, expected] = line
        s2 = Solution2()
        result = s2.checkElements(start, end, arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 25 of May 2026

    p1()

    p2()
