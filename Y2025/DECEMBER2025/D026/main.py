class Solution1:
    def bestClosingTime(self, customers: str) -> int:
        # penalty(j) = (# of 'N' before j) + (# of 'Y' from j onward)
        # use prefix and suffix sum

        penalty = customers.count("Y")
        min_penalty = penalty
        best_hour = 0

        for i, c in enumerate(customers):
            if c == "Y":
                penalty -= 1
            else:
                penalty += 1

            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = i + 1

        return best_hour

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2483. Minimum Penalty for a Shop - https://leetcode.com/problems/minimum-penalty-for-a-shop/description/?envType=daily-question&envId=2025-12-26

    testcase = [
        ["YYNY", 2],
        ["NNNNN", 0],
        ["YYYY", 4],
    ]

    for line in testcase:
        [customers, expected] = line
        s1 = Solution1()
        result = s1.bestClosingTime(customers)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def kthMissing(self, arr, k):
        n = len(arr)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            missing = arr[mid] - (mid + 1)

            if missing < k:
                left = mid + 1
            else:
                right = mid - 1

        return left + k

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Kth Missing Positive Number in a Sorted Array - https://www.geeksforgeeks.org/problems/kth-missing-positive-number-in-a-sorted-array/1

    testcase = [
        [[2, 3, 4, 7, 11], 5, 9],
        [[1, 2, 3], 2, 5],
        [[3, 5, 9, 10, 11, 12], 2, 2],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.kthMissing(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 26 of December 2025

    p1()

    p2()
