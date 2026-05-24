from typing import List


class Solution1:
    def maxJumps(self, arr: List[int], d: int) -> int:
        N = len(arr)

        t = [1] * N

        # Sort (value, index) pairs ascending — smaller values resolved first
        sorted_indices = sorted(range(N), key=lambda i: arr[i])

        for i in sorted_indices:
            # scan left: i-1 down to max(0, i-d)
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:  # blocking condition - path obstructed
                    break
                t[i] = max(t[i], 1 + t[j])

            # scan right: i+1 up to min(N-1, i+d)
            for j in range(i + 1, min(N, i + d + 1)):
                if arr[j] >= arr[i]:  # blocking condition
                    break
                t[i] = max(t[i], 1 + t[j])

        return max(t)

        # Complexity Analysis:
        # Time : O(N * D)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1340. Jump Game V - https://leetcode.com/problems/jump-game-v/description/?envType=daily-question&envId=2026-05-24

    testcase = [
        [[6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2, 4],
        [[3, 3, 3, 3, 3], 3, 1],
        [[7, 6, 5, 4, 3, 2, 1], 1, 7],
    ]

    for line in testcase:
        [arr, d, expected] = line
        s1 = Solution1()
        result = s1.maxJumps(arr, d)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def coin(self, arr: list[int]) -> int:
        # code here
        left, right = 0, len(arr) - 1

        while left < right:
            if arr[left] < arr[right]:
                right -= 1
            else:
                left += 1

        return arr[left]

        # Complexity Analysis:
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Last Coin in a Game of Alternates - https://www.geeksforgeeks.org/problems/last-coin-in-a-game-of-alternates/1

    testcase = [
        [[5, 3, 1, 6, 9], 1],
        [[5, 9, 2, 5], 2],
        [[11], 11],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.coin(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 24 of May 2026

    p1()

    p2()
