class Solution1:
    def specialTriplets(self, nums):
        MODO = 10**9 + 7
        N = len(nums)

        def count_double_left():
            # for every num, count 2*nums[i] on its left
            out = [0] * N
            freq = {}

            for i in range(N):
                out[i] = freq.get(nums[i] * 2, 0)
                freq[nums[i]] = freq.get(nums[i], 0) + 1

            return out

        def count_double_right():
            # for every num, count 2*nums[i] on its right
            out = [0] * N
            freq = {}

            for i in range(N - 1, -1, -1):
                out[i] = freq.get(nums[i] * 2, 0)
                freq[nums[i]] = freq.get(nums[i], 0) + 1

            return out

        ji = count_double_left()
        jk = count_double_right()

        triplets = 0
        for i in range(N):
            triplets = (triplets + ji[i] * jk[i]) % MODO

        return triplets

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3583. Count Special Triplets - https://leetcode.com/problems/count-special-triplets/description/?envType=daily-question&envId=2025-12-09

    testcase = [
        [[6, 3, 6], 1],
        [[0, 1, 0, 0], 1],
        [[8, 4, 2, 8, 4], 2],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.specialTriplets(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findDuplicates(self, arr):
        # code here
        N = len(arr)
        F = N + 1

        duplicates = []

        # add hash
        for i in range(N):
            e = (arr[i]) % F  # original element without hash
            arr[e - 1] += F  # index = element, apply hash to index el

        # check hash
        for i in range(N):
            if arr[i] // F >= 2:
                # hash was added twice at index i
                duplicates.append(i + 1)

        return duplicates

        # Complexity analysis
        # Time : O(2N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Array Duplicates - https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/1

    testcase = [
        [[1, 2, 6, 1, 5, 6, 7], [1, 6]],
        [[3, 2, 3], [3]],
        [[1, 2, 6, 1, 5, 6, 7], [1, 6]],
        [[3, 1, 2], []],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.findDuplicates(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 9 of December 2025

    p1()

    p2()
