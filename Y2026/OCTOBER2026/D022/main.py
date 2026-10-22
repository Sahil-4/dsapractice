class Solution1:
    def minOperations(self, nums: list[int]) -> int:
        N = len(nums)

        if N <= 1:
            return 0

        # check cyclically ascending or descending
        is_asc = True
        is_desc = True

        for i in range(N):
            nxt = (i + 1) % N
            if (nums[i] + 1) % N != nums[nxt]:
                is_asc = False
            if (nums[i] - 1 + N) % N != nums[nxt]:
                is_desc = False

        if not is_asc and not is_desc:
            return -1

        idx = nums.index(0)

        ans = float("inf")

        if is_asc:
            # 0 reverses: rotate left `idx` times
            cost_rot_only = idx
            # 2 reverses: reverse, rotate left (N - idx) % N times, reverse
            cost_two_rev = ((N - idx) % N) + 2
            ans = min(ans, cost_rot_only, cost_two_rev)

        if is_desc:
            # 1 reverse then left rotations
            cost_rev_then_rot = 1 + (N - 1 - idx)
            # Left rotations then 1 reverse
            cost_rot_then_rev = 1 + ((idx + 1) % N)
            ans = min(ans, cost_rev_then_rot, cost_rot_then_rev)

        return int(ans)

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3942. Minimum Operations to Sort a Permutation - https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/description/?envType=daily-question&envId=2026-10-22

    testcase = [
        [[0, 2, 1], 2],
        [[1, 0, 2], 2],
        [[2, 0, 1, 3], -1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minOperations(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minimumSum(self, s: str) -> int:
        is_alpha = lambda ch: "a" <= ch <= "z"

        s_arr = list(s)
        N = len(s_arr)

        # Step 1: Force palindrome
        left = 0
        right = N - 1

        while left <= right:
            if (
                is_alpha(s_arr[left])
                and is_alpha(s_arr[right])
                and s_arr[left] != s_arr[right]
            ):
                return -1

            if not is_alpha(s_arr[left]):
                s_arr[left] = s_arr[right]

            if not is_alpha(s_arr[right]):
                s_arr[right] = s_arr[left]

            left += 1
            right -= 1

        # Step 2: Greedy fill "?"
        # Find the VERY FIRST alpha in the entire string
        fill_alpha = "a"  # Default if the whole string is just "?????"
        for char in s_arr:
            if is_alpha(char):
                fill_alpha = char
                break

        # Fill greedy up to the middle (including middle for odd lengths)
        for i in range((N + 1) // 2):
            if not is_alpha(s_arr[i]):
                s_arr[i] = fill_alpha
                s_arr[N - 1 - i] = s_arr[i]  # Step 3: fill copy left -> right
            fill_alpha = s_arr[i]

        # Step 4: Calculate absolute differences across the whole string
        total_sum = 0
        for i in range(1, N):
            total_sum += abs(ord(s_arr[i]) - ord(s_arr[i - 1]))

        return total_sum

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Palindrome with Replacement - https://www.geeksforgeeks.org/problems/palindrome-with-minimum-sum--170648/1

    testcase = [
        ["a???c??c????", 4],
        ["a???c??c???c", -1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minimumSum(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def singleNumber(self, nums: list[int]) -> int:
        single = 0
        for num in nums:
            single ^= num

        return single

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 136. Single Number - https://leetcode.com/problems/single-number/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[2, 2, 1], 1],
        [[4, 1, 2, 1, 2], 4],
        [[1], 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.singleNumber(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 22 of October 2026

    p1()

    p2()

    p3()
