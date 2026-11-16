class Solution1:
    def digitSum(self, s: str, k: int) -> str:
        # Input: s = "11111222223", k = 3
        # Input: s = "135", k = 3

        prev = list(s)

        def get_digits_sum_array(arr: list[str], s: int, k: int) -> list[int]:
            k_sum = 0

            for it in range(s, min(s + k, len(arr))):
                k_sum += int(arr[it])

            sum_array = []
            while k_sum > 0:
                _digit = k_sum % 10
                k_sum = int(k_sum / 10)

                sum_array.append(_digit)

            sum_array.reverse()

            return sum_array if sum_array else [0]

        while len(prev) > k:
            curr = []

            for i in range(0, len(prev), k):
                k_sum_array = get_digits_sum_array(prev, i, k)
                curr.extend(k_sum_array)

            prev = curr

        return "".join([str(d) for d in prev])

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2243. Calculate Digit Sum of a String - https://leetcode.com/problems/calculate-digit-sum-of-a-string/description/?envType=daily-question&envId=2026-11-16

    testcase = [
        ["11111222223", 3, "135"],
        ["00000000", 3, "000"],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.digitSum(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findKthSmall(self, arr, k):
        # code here
        arr.sort()
        N = len(arr)

        kth_small = k

        i = 0
        while i < N and arr[i] <= kth_small:
            i += 1
            kth_small += 1

        return kth_small

        # Complexity analysis
        # Time : O(N * Log(N)) + O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks K-th Missing in Natural Numbers - https://www.geeksforgeeks.org/problems/k-th-missing-element-in-natural-numbers/1

    testcase = [
        [[1, 9, 5, 2], 6, 10],
        [[1, 2, 3, 4], 1, 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.findKthSmall(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 217. Contains Duplicate - https://leetcode.com/problems/contains-duplicate/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[1, 2, 3, 1], True],
        [[1, 2, 3, 4], False],
        [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.containsDuplicate(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 16 of November 2026

    p1()

    p2()

    p3()
