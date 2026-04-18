class Solution1:
    def mirrorDistance(self, n: int) -> int:
        u = int(str(n)[::-1])
        return abs(n - u)

        # Complexity analysis
        # Time : (Log(N))
        # Space : O(Log(N))


def p1():
    # Problem 1 : POTD Leetcode 3783. Mirror Distance of an Integer - https://leetcode.com/problems/mirror-distance-of-an-integer/description/?envType=daily-question&envId=2026-04-18

    testcase = [
        [25, 27],
        [10, 9],
        [7, 0],
    ]

    for line in testcase:
        [n, expected] = line
        s1 = Solution1()
        result = s1.mirrorDistance(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def kadane_max_subarray_sum(self, arr: list[int]) -> int:
        ans = 0
        curr_sum = 0

        for num in arr:
            curr_sum += num
            ans = max(ans, curr_sum)
            curr_sum = max(curr_sum, 0)

        return ans

    def maxOnes(self, arr: list[int]) -> int:
        # code here
        N = len(arr)

        ones_count = 0

        # count 1s and modify input
        for i in range(N):
            if arr[i] == 1:
                ones_count += 1
                arr[i] = -1
            else:
                arr[i] = 1

        max_sum = self.kadane_max_subarray_sum(arr)

        # fix modified input
        for i in range(N):
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1

        return ones_count + max_sum

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Flip to Maximize 1s - https://www.geeksforgeeks.org/problems/flip-bits0240/1

    testcase = [
        [[1, 0, 0, 1, 0], 4],
        [[1, 0, 0, 1, 0, 0, 1], 6],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.maxOnes(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 18 of April 2026

    p1()

    p2()
