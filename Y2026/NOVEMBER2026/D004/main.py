from collections import defaultdict
from heapq import heappop, heappush
from itertools import accumulate
from operator import add


class Solution1:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        N = len(nums)

        l_size = x // 2
        odd = x & 1

        # Initialize the first window of size x
        first_win = sorted(nums[:x])
        left = [-v for v in reversed(first_win[:l_size])]
        right = first_win[l_size:]
        left_sum = sum(first_win[:l_size])
        right_sum = sum(first_win[l_size:])

        delayed_left = defaultdict(int)
        delayed_right = defaultdict(int)

        cost = [0] * (N - x + 1)
        cost[0] = right_sum - left_sum - (right[0] if odd else 0)

        # Slide the window across the array
        for i in range(x, N):
            in_val = nums[i]
            out_val = nums[i - x]
            balance = 0

            # 1. Insert the incoming element (does not change -left[0])
            if in_val <= -left[0]:
                heappush(left, -in_val)
                left_sum += in_val
                balance += 1
            else:
                heappush(right, in_val)
                right_sum += in_val
                balance -= 1

            # 2. Mark the outgoing element for lazy deletion
            if out_val <= -left[0]:
                left_sum -= out_val
                delayed_left[out_val] += 1
                balance -= 1
            else:
                right_sum -= out_val
                delayed_right[out_val] += 1
                balance += 1

            # 3. Rebalance active sizes of left and right heaps
            if balance > 0:
                while delayed_left[-left[0]]:
                    delayed_left[-heappop(left)] -= 1
                v = -heappop(left)
                left_sum -= v
                right_sum += v
                heappush(right, v)

            elif balance < 0:
                while delayed_right[right[0]]:
                    delayed_right[heappop(right)] -= 1
                v = heappop(right)
                right_sum -= v
                left_sum += v
                heappush(left, -v)

            # 4. Prune expired elements at the heap tops
            while delayed_left[-left[0]]:
                delayed_left[-heappop(left)] -= 1
            while delayed_right[right[0]]:
                delayed_right[heappop(right)] -= 1

            cost[i - x + 1] = right_sum - left_sum - (right[0] if odd else 0)

        # DP to pick k non-overlapping subarrays of length x
        L = N - k * x + 1
        dp = list(accumulate(cost[:L], min))
        for r in range(1, k):
            dp = list(accumulate(map(add, dp, cost[r * x : r * x + L]), min))

        return dp[-1]

        # Complexity analysis
        # Time : O(N * Log(X) + N * K)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3505. Minimum Operations to Make Elements Within K Subarrays Equal - https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/description/?envType=daily-question&envId=2026-11-04

    testcase = [
        [[5, -2, 1, 3, 7, 3, 6, 4, -1], 3, 2, 8],
        [[9, -2, -2, -2, 1, 5], 2, 2, 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minOperations(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def subarrayXor(self, arr: list[int]) -> int:
        # code here

        # count of contribution of any element = (i + 1) * (N - i)
        # ie. number of starting points * number of ending points
        # in XOR element will become 0 if N is even, else element will remain as it is
        # if N is even, all element will come even number of times hence answer will be 0
        # else, each element at even indices will only contribute one time

        N = len(arr)

        if not (N & 1):
            return 0

        final_xor = 0
        for i in range(0, N, 2):
            # contribution = (i + 1) * (N - i)
            # if contribution & 1: final_xor ^= arr[i]

            final_xor ^= arr[i]

        return final_xor

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks XOR of All Subarray XORs - https://www.geeksforgeeks.org/problems/game-of-xor1541/1

    testcase = [
        [[1, 2, 3], 2],
        [[1, 2], 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.subarrayXor(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def reverseBits(self, N: int) -> int:
        rev = 0

        for i in range(32):
            bit = (N >> i) & 1
            rev = rev << 1
            rev = rev | bit

        return rev

        # Complexity analysis
        # Time : O(1)
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 190. Reverse Bits - https://leetcode.com/problems/reverse-bits/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [43261596, 964176192],
        [2147483644, 1073741822],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.reverseBits(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 4 of November 2026

    p1()

    p2()

    p3()
