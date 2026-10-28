class Solution1:
    def minXorPath(self, grid: list[list[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        # reachable[j] = set of every xor value obtainable on a path from (0, 0) to (i, j),
        # values are at most 1023, so a set never holds more than 1024 numbers;
        # only the previous row is needed
        reachable = [set() for _ in range(N)]

        for i in range(M):
            for j in range(N):
                value = grid[i][j]

                if i == 0 and j == 0:
                    reachable[j] = {value}
                    continue

                # from above (reachable[j] still holds the previous row), or from the left
                previous = set()
                if i > 0:
                    previous |= reachable[j]
                if j > 0:
                    previous |= reachable[j - 1]

                reachable[j] = {x ^ value for x in previous}

        return min(reachable[N - 1])

        # Complexity analysis
        # Time : O(M * N * 1024)
        # Space : O(N * 1024)


def p1():
    # Problem 1 : POTD Leetcode 3882. Minimum XOR Path in a Grid - https://leetcode.com/problems/minimum-xor-path-in-a-grid/?envType=daily-question&envId=2026-10-28

    testcase = [
        [[[1, 2], [3, 4]], 6],
        [[[6, 7], [5, 8]], 9],
        [[[2, 7, 5]], 0],
        [[[9]], 9],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minXorPath(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def nthCharacter(self, n):
        # code here

        # numbers with D digits : 9 * 10^(D - 1) of them, starting at 10^(D - 1);
        # skip whole groups while n lies beyond them
        digits = 1
        count = 9
        start = 1

        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10

        # n is now a 1-based position inside the current group
        number = start + (n - 1) // digits
        index = (n - 1) % digits

        return str(number)[index]

        # Complexity analysis
        # Time : O(log(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Nth in Concatenated Decimal String - https://www.geeksforgeeks.org/problems/nth-character-in-concatenated-decimal-string0245/1

    testcase = [
        [10, "1"],
        [11, "0"],
        [3, "3"],
        [9, "9"],
        [190, "1"],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.nthCharacter(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1

        # the minimum is the rotation point; compare mid with the right end:
        # mid > high means the drop lies to the right of mid, otherwise mid itself
        # or something to its left is the minimum
        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 153. Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[3, 4, 5, 1, 2], 1],
        [[4, 5, 6, 7, 0, 1, 2], 0],
        [[11, 13, 15, 17], 11],
        [[2, 1], 1],
        [[1], 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.findMin(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 28 of October 2026

    p1()

    p2()

    p3()
